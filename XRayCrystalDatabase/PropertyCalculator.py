import numpy as np
from XRayCrystalDatabase import util


############################################################
#         Define crystals
############################################################
class Diamond:
    def __init__(self):
        # Define properties for the unit cell
        self.a = 3.567 / 1e4  # um
        self.b = self.a
        self.c = self.a
        self.volume = self.a * self.b * self.c

        # Atom positions
        self.atom_arrangement = [["C", np.array([0., 0., 0.])],
                                 ["C", np.array([0.25, 0.25, 0.25]) * self.a]]


class Silicon:
    def __init__(self):
        # Define properties for the unit cell
        self.a = 5.43095 / 1e4  # um
        self.b = self.a
        self.c = self.a
        self.volume = self.a * self.b * self.c

        # Atom positions
        self.atom_arrangement = [["Si", np.array([0., 0., 0.])],
                                 ["Si", np.array([0.25, 0.25, 0.25]) * self.a]]


class Germanium:
    def __init__(self):
        # Define properties for the unit cell
        self.a = 5.658 / 1e4  # um
        self.b = self.a
        self.c = self.a
        self.volume = self.a * self.b * self.c

        # Atom positions
        self.atom_arrangement = [["Ge", np.array([0., 0., 0.])],
                                 ["Ge", np.array([0.25, 0.25, 0.25]) * self.a]]


############################################################
#      Define functions to analyze the crystals
############################################################
def get_recirpocal_lattice(crystal_type, miller_idx):
    """
    Convert the miller index to the corresponding reciprocal lattice

    :param miller_idx:
    :param crystal_type:
    :return:
    """
    return np.array(miller_idx[0] / crystal_type.a,
                    miller_idx[1] / crystal_type.b,
                    miller_idx[2] / crystal_type.c)


def get_atomic_plane_distance(crystal_type, miller_idx):
    """

    :param miller_idx:
    :param crystal_type:
    :return:
    """
    h = crystal_type.get_recirpocal_lattice(miller_idx=miller_idx)
    distance = 1. / np.sqrt((h[0] / crystal_type.a) ** 2 +
                            (h[1] / crystal_type.b) ** 2 +
                            (h[2] / crystal_type.c) ** 2)
    return distance


def get_chi0_and_chih(crystal_type, xray_energy_kev, miller_idx, temp=293.):
    """
    Get the chi0 and chih value for the specific wave length an the reciprocal lattice.

    :param crystal_type:
    :param miller_idx:
    :param xray_energy_kev:
    :param temp: The temperature in K.
    :return:
    """
    # Get the atomic plane distance
    distance = get_atomic_plane_distance(crystal_type=crystal_type, miller_idx=miller_idx)

    # Get reciprocal lattice
    reciprocal_lattice = get_recirpocal_lattice(crystal_type=crystal_type, miller_idx=miller_idx)

    # Find the atom number in the unit cell of this atom
    atom_num = len(crystal_type.atom_positions)

    # Create holders for different parameters
    f0_holder = []  # Form factor for wave vector 0
    f_holder = []  # Form factor for wave length lambda
    fp_holder = []  # Real part of the anormalous dispersion
    fpp_holder = []  # Imaginary part of the anormalous dispersion
    sigma_d_holder = []  # Dipole photoelectric cross-section
    db_holder = []  # The Debye-Waller factor
    phase_holder = []  # The Phase for different atoms

    # Loop through the atoms in this unit cell
    for atom_idx in range(atom_num):
        # Find the atom
        atom_type = crystal_type.atom_arrangement[atom_idx][0]
        atom_position = crystal_type.atom_arrangement[atom_idx][1]

        ####################################################
        #   Step 1 Get Debye-Waller factor
        ####################################################
        # Get the Debye-Waller factor
        db_factor = util.get_debye_waller_factor(s=0.5 / distance,
                                                 atom_type=atom_type,
                                                 temp=temp)
        db_holder.append(db_factor)

        ####################################################
        #   Step 2 Get phase
        ####################################################
        # Get the phase
        phase_holder.append(np.exp(1.j * np.dot(reciprocal_lattice, atom_position)))

        ####################################################
        #   Step 3 Get f0, f, fp, fpp and sigma D
        ####################################################
        f0, f, fp, fpp, sigma_d = util.get_f0_f_fp_fpp_and_sigma_d(atom_type=atom_type,
                                                                   energies=xray_energy_kev)
        f0_holder.append(f0)
        f_holder.append(f)
        fp_holder.append(fp)
        fpp_holder.append(fpp)
        sigma_d_holder.append(sigma_d)

    ####################################################
    #   Calculate the chi0
    ####################################################
    # Get wave length
    wavelength = 2. * np.pi / util.kev_to_wave_number(energy=xray_energy_kev)

    chi0r = 0.
    for idx in range(atom_num):
        chi0r += f0_holder[idx] + fp_holder[idx]
    chi0r *= - (wavelength ** 2) * util.r0 / np.pi / crystal_type.volume

    chi0i = 0.
    for idx in range(atom_num):
        chi0i += sigma_d_holder[idx]
    chi0i *= - wavelength / (2 * np.pi * crystal_type.volume)

    chi0 = chi0r + 1.j * chi0i

    ####################################################
    #   Calculate the chi0
    ####################################################
    # Get wave length
    wavelength = 2. * np.pi / util.kev_to_wave_number(energy=xray_energy_kev)

    chihr = 0.
    for idx in range(atom_num):
        chihr += (f_holder[idx] + fp_holder[idx]) * phase_holder[idx] * db_holder[idx]
    chihr *= - (wavelength ** 2) * util.r0 / np.pi / crystal_type.volume

    chihi = 0.
    for idx in range(atom_num):
        chihi += sigma_d_holder[idx] * db_holder[idx] * phase_holder[idx]
    chihi *= - wavelength / (2 * np.pi * crystal_type.volume)

    chih = chihr + 1.j * chihi
    return chi0, chih
