import numpy as np
from scipy import interpolate
from scipy import special

from XRayCrystalDatabase.Database import DebyeDatabase, AtomDatabase

"""
The unit system in this package is 
kg, m, s

Especially, eV is only used for the incident photon energy
"""
# Define constant
pi = np.pi
two_pi = 2. * np.pi

h = 6.62607015 * 1e-34  # Planck constant
hbar = h / two_pi

c = 299792458.  # The speed of light
k = 1.38064852 * 1e-23  # The Boltzmann constant
na = 6.02214076 * 1e23  # The Avogadro's number
r0 = 2.8179403262 * 1e-15  # The classical radius of electron


# Define some conversion functions to remove dependence
def kev_to_wave_number(energy_kev):
    # Convert keV to Joule
    energy = energy_kev * 1.6021773e-16
    return energy / hbar / c


def atomic_mass_to_kg(atomic_mass):
    return atomic_mass * 1.6605402 * 1e-27


#####################################################################################
#          Database functions
#####################################################################################

def get_atomic_form_factor(atom_type, s):
    """
    Get the atomic form factor for a specific atom for an array of different q values
    Here, q is defined as 2 pi / wave-length.

    Currently, the available atom types are

    silicon
    carbon

    :param atom_type:
    :param s: Wave vector in m
    :return:
    """
    # Get the coefficient from the table
    [a1, a2, a3, a4, a5,
     c0, b1, b2, b3, b4, b5] = AtomDatabase.get_wk_coefficient(atom_type=atom_type)

    # Fit with the coefficient to get the form factors
    s_square = s ** 2
    form_factors = (a1 * np.exp(-b1 * s_square) +
                    a2 * np.exp(-b2 * s_square) +
                    a3 * np.exp(-b3 * s_square) +
                    a4 * np.exp(-b4 * s_square) +
                    a5 * np.exp(-b5 * s_square) + c0)

    return form_factors


def get_f0_f_fp_fpp_and_sigma_d(atom_type, energy_kev, s):
    """
    Get the f, fp, and fpp value for the specific q value

    :param atom_type:
    :param energy_kev:
    :param s: Assume that the lattice plane distance is d. Then s = 1/2d
    :return:
    """

    # Get if the atom is in the data base
    if not (atom_type in AtomDatabase.atom_name_list):
        raise Exception("Sorry, at present, only the following elements can be \n "
                        "processed automatically:{}".format(AtomDatabase.atom_name_list))

    # Get the atomic form factor
    f = get_atomic_form_factor(atom_type=atom_type, s=s)

    # Get f0
    f0 = float(AtomDatabase.get_atomic_number(atom_type=atom_type))

    # Get the reference data from the data base
    energies_ref = AtomDatabase.atom_info[atom_type]["chantler energies"]
    fp_ref = AtomDatabase.atom_info[atom_type]["fp values"]
    fpp_ref = AtomDatabase.atom_info[atom_type]["fpp values"]
    # mu_rho_ref = AtomDatabase.atom_info[atom_type]["mu over rho"]

    # Use interpolation to find the desired value for the desired q value.
    fp_spl = interpolate.splrep(x=energies_ref, y=fp_ref)
    fp = interpolate.splev(energy_kev, fp_spl)

    fpp_spl = interpolate.splrep(x=energies_ref, y=fpp_ref)
    fpp = interpolate.splev(energy_kev, fpp_spl)

    # mu_rho_spl = interpolate.splrep(x=energies_ref, y=mu_rho_ref)
    # mu_rho = interpolate.splev(energy_kev, mu_rho_spl)

    # Get the atomic weight
    # mass_amu = AtomDatabase.get_atomic_mass(atom_type=atom_type)
    # sigma_d = mu_rho * mass_amu / na

    # Get wave length
    wavelength = 2. * np.pi / kev_to_wave_number(energy_kev=energy_kev)
    sigma_d = fpp * 2 * wavelength * r0

    return f0, f, fp, fpp, sigma_d


def get_debye_coefficient(atom_type, temp=293.):
    # Get Debye temperature
    db_temp = DebyeDatabase.get_debye_temperature(atom_type=atom_type)

    # Get ratio x
    x = float(temp) / db_temp

    # Get atomic mass
    mass = AtomDatabase.get_atomic_mass(atom_type=atom_type)
    mass_kg = atomic_mass_to_kg(atomic_mass=mass)

    # Get the coefficient B
    coef = 12. * (h ** 2) / (mass_kg * k * db_temp) * (special.erf(x) / x + 0.25)
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
    # print("s = 1/2d = ", s)

    coef = get_debye_coefficient(atom_type=atom_type, temp=temp)
    return np.exp(-coef * (s ** 2))
