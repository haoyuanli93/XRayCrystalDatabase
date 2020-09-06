def get_debye_temperature(atom_type):
    if atom_type in list(debye_temperature.keys()):
        return debye_temperature[atom_type]
    else:
        raise Exception("Currently, the Debye temperature for the following elements are in " +
                        "this database: \n" +
                        "{}".format(list(debye_temperature.keys())))


debye_temperature = {"Al": 428.,
                     "Be": 1440.,
                     "Cd": 209.,
                     "Cs": 38.,
                     "C": 2230.,
                     "Cr": 630.,
                     "Cu": 343.,
                     "Ge": 374.,
                     "Au": 170.,
                     "Fe": 470.,
                     "Pb": 105.,
                     "Mn": 410.,
                     "Ni": 450.,
                     "Pt": 240.,
                     "Rb": 56.,
                     "Se": 90.,
                     "Si": 645.,
                     "Ag": 215.,
                     "Ta": 240.,
                     "Sn": 200.,
                     "Ti": 420.,
                     "W": 400.,
                     "Zn": 327.}
