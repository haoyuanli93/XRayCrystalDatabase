"""
This notebook contains chi0, chih sigma and chih pi for
8,9,10,11 keV X-ray photon energies for silicon, diamond
and germanium crystals.

The data are from https://x-server.gmca.aps.anl.gov/x0h.html
"""

silicon_8kev = {"1,1,1", {"chi0": complex(-0.15310E-04, 0.35783E-06),
                          "chih sigma": complex(-0.80928E-05, 0.24938E-06),
                          "chih pi": complex(-0.71042E-05, 0.21783E-06)},

                "2,2,0", {"chi0": complex(-0.15310E-04, 0.35783E-06),
                          "chih sigma": complex(-0.93209E-05, 0.34424E-06),
                          "chih pi": complex(-0.62847E-05, 0.22972E-06)},

                "3,3,3", {"chi0": complex(-0.15310E-04, 0.35783E-06),
                          "chih sigma": complex(-0.45519E-05, 0.22284E-06),
                          "chih pi": complex(-0.45239E-06, 0.26309E-07)},

                "4,4,0", {"chi0": complex(-0.15310E-04, 0.35783E-06),
                          "chih sigma": complex(-0.59269E-05, 0.31001E-06),
                          "chih pi": complex(-0.17957E-05, 0.98232E-07)}}

silicon_9kev = {"1,1,1", {"chi0": complex(-0.12073E-04, 0.22532E-06),
                          "chih sigma": complex(-0.63776E-05, 0.15706E-06),
                          "chih pi": complex(-0.57621E-05, 0.14127E-06)},

                "2,2,0", {"chi0": complex(-0.12073E-04, 0.22532E-06),
                          "chih sigma": complex(-0.73415E-05, 0.21687E-06),
                          "chih pi": complex(-0.54520E-05, 0.15891E-06)},

                "3,3,3", {"chi0": complex(-0.12073E-04, 0.22532E-06),
                          "chih sigma": complex(-0.35815E-05, 0.14003E-06),
                          "chih pi": complex(-0.47043E-06, 0.21358E-07)},

                "4,4,0", {"chi0": complex(-0.12073E-04, 0.22532E-06),
                          "chih sigma": complex(-0.46620E-05, 0.19361E-06),
                          "chih pi": complex(-0.13757E-06, 0.10033E-07)}}

silicon_10kev = {"1,1,1", {"chi0": complex(-0.97631E-05, 0.14871E-06),
                           "chih sigma": complex(-0.51546E-05, 0.10368E-06),
                           "chih pi": complex(-0.47516E-05, 0.95183E-07)},

                 "2,2,0", {"chi0": complex(-0.97631E-05, 0.14871E-06),
                           "chih sigma": complex(-0.59310E-05, 0.14320E-06),
                           "chih pi": complex(-0.46945E-05, 0.11201E-06)},

                 "3,3,3", {"chi0": complex(-0.97631E-05, 0.14871E-06),
                           "chih sigma": complex(-0.28908E-05, 0.92567E-07),
                           "chih pi": complex(-0.85681E-06, 0.29160E-07)},

                 "4,4,0", {"chi0": complex(-0.97631E-05, 0.14871E-06),
                           "chih sigma": complex(-0.37621E-05, 0.12785E-06),
                           "chih pi": complex(-0.62487E-06, 0.24211E-07)}}

silicon_11kev = {"1,1,1", {"chi0": complex(-0.80575E-05, 0.10198E-06),
                           "chih sigma": complex(-0.42522E-05, 0.71108E-07),
                           "chih pi": complex(-0.39775E-05, 0.66266E-07)},

                 "2,2,0", {"chi0": complex(-0.80575E-05, 0.10198E-06),
                           "chih sigma": complex(-0.48909E-05, 0.98241E-07),
                           "chih pi": complex(-0.40482E-05, 0.80452E-07)},

                 "3,3,3", {"chi0": complex(-0.80575E-05, 0.10198E-06),
                           "chih sigma": complex(-0.23820E-05, 0.63565E-07),
                           "chih pi": complex(-0.99688E-06, 0.27454E-07)},

                 "4,4,0", {"chi0": complex(-0.80575E-05, 0.10198E-06),
                           "chih sigma": complex(-0.30994E-05, 0.87817E-07),
                           "chih pi": complex(-0.96336E-06, 0.29061E-07)}}

# TODO: Get the data for Diamond and Germanium
