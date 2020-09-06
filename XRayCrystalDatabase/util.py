import numpy as np
from scipy import interpolate
from scipy import special

from XRayCrystalDatabase.Database import DebyeDatabase, AtomDatabase

# Define constant
pi = np.pi
two_pi = 2. * np.pi

hbar = 0.0006582119514  # This is the reduced planck constant in keV/fs
h = hbar / two_pi

c = 299792458. * 1e-9  # The speed of light in um / fs
k = 8.617333262145 * 1e-8  # The Boltzmann constant in keV/K
na = 6.02214076 * 1e23  # The Avogadro's number
r0 = 2.8179403227 * 1e-9  # The classical radius of electron


# Define some conversion functions to remove dependence
def kev_to_petahertz_frequency(energy):
    return energy / hbar * 2 * pi


def kev_to_petahertz_angular_frequency(energy):
    return energy / hbar


def kev_to_wave_number(energy):
    return energy / hbar / c


def petahertz_frequency_to_kev(frequency):
    return hbar * 2 * pi * frequency


def petahertz_angular_frequency_to_kev(angular_frequency):
    return hbar * angular_frequency


def petahertz_angular_frequency_to_wave_number(angular_frequency):
    return angular_frequency / c


def wave_number_to_kev(wavevec):
    return wavevec * hbar * c


def atomic_mass_to_kev(atomic_mass):
    return atomic_mass * 9.3149410242 * 1e5


#####################################################################################
#          Database functions
#####################################################################################

def get_atomic_form_factor(atom_type, q_array):
    """
    Get the atomic form factor for a specific atom for an array of different q values
    Here, q is defined as 2 pi / wave-length.

    Currently, the available atom types are

    silicon
    carbon

    :param atom_type:
    :param q_array:
    :return:
    """
    # Get the coefficient from the table
    [a1, a2, a3, a4, a5,
     c0, b1, b2, b3, b4, b5] = AtomDatabase.get_wk_coefficient(atom_type=atom_type)

    # Fit with the coefficient to get the form factors
    form_factors = (a1 * np.exp(-b1 * q_array ** 2) +
                    a2 * np.exp(-b2 * q_array ** 2) +
                    a3 * np.exp(-b3 * q_array ** 2) +
                    a4 * np.exp(-b4 * q_array ** 2) +
                    a5 * np.exp(-b5 * q_array ** 2) + c0)

    return form_factors


def get_f0_f_fp_fpp_and_sigma_d(atom_type, energies):
    """
    Get the f, fp, and fpp value for the specific q value

    :param atom_type:
    :param energies:
    :return:
    """

    # Get if the atom is in the data base
    if not (atom_type in AtomDatabase.atom_name_list):
        raise Exception("Sorry, at present, only the following elements can be \n "
                        "processed automatically:{}".format(AtomDatabase.atom_name_list))

    q_array = kev_to_wave_number(energy=energies)
    # Get the atomic form factor
    f = get_atomic_form_factor(atom_type=atom_type, q_array=q_array)

    # Get f0
    f0 = float(AtomDatabase.get_atomic_number(atom_type=atom_type))

    # Get the reference data from the data base
    energies_ref = AtomDatabase.atom_info[atom_type]["chantler energies"]

    fp_ref = AtomDatabase.atom_info[atom_type]["fp values"]
    fpp_ref = AtomDatabase.atom_info[atom_type]["fpp values"]
    mu_rho_ref = AtomDatabase.atom_info[atom_type]["mu over rho"]
    q_ref = kev_to_wave_number(energy=energies_ref)

    # Use interpolation to find the desired value for the desired q value.
    fp_spl = interpolate.splrep(x=q_ref, y=fp_ref)
    fp = interpolate.splev(q_array, fp_spl)

    fpp_spl = interpolate.splrep(x=q_ref, y=fpp_ref)
    fpp = interpolate.splev(q_array, fpp_spl)

    mu_rho_spl = interpolate.splrep(x=q_ref, y=mu_rho_ref)
    mu_rho = interpolate.splev(q_array, mu_rho_spl)

    # Get the atomic weight
    mass_amu = AtomDatabase.get_atomic_mass(atom_type=atom_type)
    sigma_d = mu_rho * mass_amu / na

    return f0, f, fp, fpp, sigma_d


def get_debye_coefficient(atom_type, temp=293.):
    # Get Debye temperature
    db_temp = DebyeDatabase.get_debye_temperature(atom_type=atom_type)

    # Get ratio x
    x = float(temp) / db_temp

    # Get atomic mass
    mass = AtomDatabase.get_atomic_mass(atom_type=atom_type)
    mass_kev = atomic_mass_to_kev(atomic_mass=mass)

    # Get the coefficient B
    coef = 12. * (h ** 2) / (mass_kev * k * db_temp) * (special.erf(x) / x + 0.25)
    return coef


def get_debye_waller_factor(s, atom_type, temp=293.):
    """
    Assume that the reciprocal lattice corresponds to a plane distance of d.
    Then s=1/(2d).

    :param s:
    :param atom_type:
    :param temp:
    :return:
    """
    coef = get_debye_coefficient(atom_type=atom_type, temp=temp)
    return np.exp(-coef * (s ** 2))
