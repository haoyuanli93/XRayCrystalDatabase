"""
This notebook contains chi0, chih sigma and chih pi for
8,9,10,11 keV X-ray photon energies for silicon, diamond
and germanium crystals.

The data are from https://x-server.gmca.aps.anl.gov/x0h.html
"""
#################################################################
#               Silicon
#################################################################
silicon_8kev = {"1,1,1": {"chi0": complex(-0.15310E-04, 0.35783E-06),
                          "chih sigma": complex(-0.80928E-05, 0.24938E-06),
                          "chih pi": complex(-0.71042E-05, 0.21783E-06)},

                "2,2,0": {"chi0": complex(-0.15310E-04, 0.35783E-06),
                          "chih sigma": complex(-0.93209E-05, 0.34424E-06),
                          "chih pi": complex(-0.62847E-05, 0.22972E-06)},

                "3,3,3": {"chi0": complex(-0.15310E-04, 0.35783E-06),
                          "chih sigma": complex(-0.45519E-05, 0.22284E-06),
                          "chih pi": complex(-0.45239E-06, 0.26309E-07)},

                "4,4,0": {"chi0": complex(-0.15310E-04, 0.35783E-06),
                          "chih sigma": complex(-0.59269E-05, 0.31001E-06),
                          "chih pi": complex(-0.17957E-05, 0.98232E-07)}}

silicon_9kev = {"1,1,1": {"chi0": complex(-0.12073E-04, 0.22532E-06),
                          "chih sigma": complex(-0.63776E-05, 0.15706E-06),
                          "chih pi": complex(-0.57621E-05, 0.14127E-06)},

                "2,2,0": {"chi0": complex(-0.12073E-04, 0.22532E-06),
                          "chih sigma": complex(-0.73415E-05, 0.21687E-06),
                          "chih pi": complex(-0.54520E-05, 0.15891E-06)},

                "3,3,3": {"chi0": complex(-0.12073E-04, 0.22532E-06),
                          "chih sigma": complex(-0.35815E-05, 0.14003E-06),
                          "chih pi": complex(-0.47043E-06, 0.21358E-07)},

                "4,4,0": {"chi0": complex(-0.12073E-04, 0.22532E-06),
                          "chih sigma": complex(-0.46620E-05, 0.19361E-06),
                          "chih pi": complex(-0.13757E-06, 0.10033E-07)}}

silicon_10kev = {"1,1,1": {"chi0": complex(-0.97631E-05, 0.14871E-06),
                           "chih sigma": complex(-0.51546E-05, 0.10368E-06),
                           "chih pi": complex(-0.47516E-05, 0.95183E-07)},

                 "2,2,0": {"chi0": complex(-0.97631E-05, 0.14871E-06),
                           "chih sigma": complex(-0.59310E-05, 0.14320E-06),
                           "chih pi": complex(-0.46945E-05, 0.11201E-06)},

                 "3,3,3": {"chi0": complex(-0.97631E-05, 0.14871E-06),
                           "chih sigma": complex(-0.28908E-05, 0.92567E-07),
                           "chih pi": complex(-0.85681E-06, 0.29160E-07)},

                 "4,4,0": {"chi0": complex(-0.97631E-05, 0.14871E-06),
                           "chih sigma": complex(-0.37621E-05, 0.12785E-06),
                           "chih pi": complex(-0.62487E-06, 0.24211E-07)}}

silicon_11kev = {"1,1,1": {"chi0": complex(-0.80575E-05, 0.10198E-06),
                           "chih sigma": complex(-0.42522E-05, 0.71108E-07),
                           "chih pi": complex(-0.39775E-05, 0.66266E-07)},

                 "2,2,0": {"chi0": complex(-0.80575E-05, 0.10198E-06),
                           "chih sigma": complex(-0.48909E-05, 0.98241E-07),
                           "chih pi": complex(-0.40482E-05, 0.80452E-07)},

                 "3,3,3": {"chi0": complex(-0.80575E-05, 0.10198E-06),
                           "chih sigma": complex(-0.23820E-05, 0.63565E-07),
                           "chih pi": complex(-0.99688E-06, 0.27454E-07)},

                 "4,4,0": {"chi0": complex(-0.80575E-05, 0.10198E-06),
                           "chih sigma": complex(-0.30994E-05, 0.87817E-07),
                           "chih pi": complex(-0.96336E-06, 0.29061E-07)}}

silicon = {"8keV": silicon_8kev,
           "9keV": silicon_9kev,
           "10keV": silicon_10kev,
           "11keV": silicon_11kev}

silicon_info = {"8keV": [8,
                         [(1, 1, 1), "1,1,1"],
                         [(2, 2, 0), "2,2,0"],
                         [(3, 3, 3), "3,3,3"],
                         [(4, 4, 0), "4,4,0"],
                         ],
                "9keV": [9,
                         [(1, 1, 1), "1,1,1"],
                         [(2, 2, 0), "2,2,0"],
                         [(3, 3, 3), "3,3,3"],
                         [(4, 4, 0), "4,4,0"],
                         ],
                "10keV": [10,
                          [(1, 1, 1), "1,1,1"],
                          [(2, 2, 0), "2,2,0"],
                          [(3, 3, 3), "3,3,3"],
                          [(4, 4, 0), "4,4,0"],
                          ],
                "11keV": [11,
                          [(1, 1, 1), "1,1,1"],
                          [(2, 2, 0), "2,2,0"],
                          [(3, 3, 3), "3,3,3"],
                          [(4, 4, 0), "4,4,0"],
                          ],
                }

#################################################################
#               Diamond
#################################################################
diamond_8kev = {"1,1,1": {"chi0": complex(-0.22852E-04, 0.31321E-07),
                          "chih sigma": complex(-0.83283E-05, 0.21743E-07),
                          "chih pi": complex(-0.59698E-05, 0.15338E-07)},

                "2,2,0": {"chi0": complex(-0.22852E-04, 0.31321E-07),
                          "chih sigma": complex(-0.73012E-05, 0.29817E-07),
                          "chih pi": complex(-0.17874E-05, 0.78801E-08)},
                }

diamond_9kev = {"1,1,1": {"chi0": complex(-0.18046E-04, 0.19136E-07),
                          "chih sigma": complex(-0.65734E-05, 0.13294E-07),
                          "chih pi": complex(-0.51025E-05, 0.10180E-07)},

                "2,2,0": {"chi0": complex(-0.18046E-04, 0.19136E-07),
                          "chih sigma": complex(-0.57591E-05, 0.18253E-07),
                          "chih pi": complex(-0.23227E-05, 0.76110E-08)},
                }

diamond_10kev = {"1,1,1": {"chi0": complex(-0.14606E-04, 0.12304E-07),
                           "chih sigma": complex(-0.53168E-05, 0.85529E-08),
                           "chih pi": complex(-0.43532E-05, 0.69200E-08)},

                 "2,2,0": {"chi0": complex(-0.14606E-04, 0.12304E-07),
                           "chih sigma": complex(-0.46544E-05, 0.11755E-07),
                           "chih pi": complex(-0.24048E-05, 0.61429E-08)},

                 "3,3,3": {"chi0": complex(-0.14606E-04, 0.12304E-07),
                           "chih sigma": complex(-0.21709E-05, 0.77402E-08),
                           "chih pi": complex(-0.13703E-05, 0.48411E-08)},

                 "4,4,0": {"chi0": complex(-0.14606E-04, 0.12304E-07),
                           "chih sigma": complex(-0.28673E-05, 0.10829E-07),
                           "chih pi": complex(-0.26760E-05, 0.10066E-07)}
                 }

diamond_11kev = {"1,1,1": {"chi0": complex(-0.12067E-04, 0.82462E-08),
                           "chih sigma": complex(-0.43910E-05, 0.57349E-08),
                           "chih pi": complex(-0.37333E-05, 0.48247E-08)},

                 "2,2,0": {"chi0": complex(-0.12067E-04, 0.82462E-08),
                           "chih sigma": complex(-0.38424E-05, 0.78886E-08),
                           "chih pi": complex(-0.23076E-05, 0.47166E-08)},

                 "3,3,3": {"chi0": complex(-0.12067E-04, 0.82462E-08),
                           "chih sigma": complex(-0.17914E-05, 0.51343E-08),
                           "chih pi": complex(-0.62358E-06, 0.18943E-08)},

                 "4,4,0": {"chi0": complex(-0.12067E-04, 0.82462E-08),
                           "chih sigma": complex(-0.23658E-05, 0.71779E-08),
                           "chih pi": complex(-0.14142E-05, 0.42738E-08)}
                 }

diamond = {"8keV": diamond_8kev,
           "9keV": diamond_9kev,
           "10keV": diamond_10kev,
           "11keV": diamond_11kev}

diamond_info = {"8keV": [8,
                         [(1, 1, 1), "1,1,1"],
                         [(2, 2, 0), "2,2,0"],
                         ],
                "9keV": [9,
                         [(1, 1, 1), "1,1,1"],
                         [(2, 2, 0), "2,2,0"],
                         ],
                "10keV": [10,
                          [(1, 1, 1), "1,1,1"],
                          [(2, 2, 0), "2,2,0"],
                          [(3, 3, 3), "3,3,3"],
                          [(4, 4, 0), "4,4,0"],
                          ],
                "11keV": [11,
                          [(1, 1, 1), "1,1,1"],
                          [(2, 2, 0), "2,2,0"],
                          [(3, 3, 3), "3,3,3"],
                          [(4, 4, 0), "4,4,0"],
                          ],
                }

#################################################################
#               Germanium
#################################################################
germanium_8kev = {"1,1,1": {"chi0": complex(-0.29188E-04, 0.83651E-06),
                            "chih sigma": complex(-0.17348E-04, 0.58374E-06),
                            "chih pi": complex(-0.15396E-04, 0.51539E-06)},

                  "2,2,0": {"chi0": complex(-0.29188E-04, 0.83651E-06),
                            "chih sigma": complex(-0.20796E-04, 0.80755E-06),
                            "chih pi": complex(-0.14555E-04, 0.55703E-06)},

                  "3,3,3": {"chi0": complex(-0.29188E-04, 0.83651E-06),
                            "chih sigma": complex(-0.97802E-05, 0.52540E-06),
                            "chih pi": complex(-0.12666E-06, 0.18260E-07)},

                  "4,4,0": {"chi0": complex(-0.29188E-04, 0.83651E-06),
                            "chih sigma": complex(-0.12645E-04, 0.73275E-06),
                            "chih pi": complex(-0.25358E-05, 0.16094E-06)}}

germanium_9kev = {"1,1,1": {"chi0": complex(-0.22831E-04, 0.52915E-06),
                            "chih sigma": complex(-0.13545E-04, 0.36935E-06),
                            "chih pi": complex(-0.12341E-04, 0.33498E-06)},

                  "2,2,0": {"chi0": complex(-0.22831E-04, 0.52915E-06),
                            "chih sigma": complex(-0.16207E-04, 0.51117E-06),
                            "chih pi": complex(-0.12363E-04, 0.38475E-06)},

                  "3,3,3": {"chi0": complex(-0.22831E-04, 0.52915E-06),
                            "chih sigma": complex(-0.75790E-05, 0.33292E-06),
                            "chih pi": complex(-0.15131E-05, 0.73703E-07)},

                  "4,4,0": {"chi0": complex(-0.22831E-04, 0.52915E-06),
                            "chih sigma": complex(-0.97850E-05, 0.46073E-06),
                            "chih pi": complex(-0.50324E-06, 0.35022E-07)}}

germanium_10kev = {"1,1,1": {"chi0": complex(-0.18164E-04, 0.35107E-06),
                             "chih sigma": complex(-0.10742E-04, 0.24510E-06),
                             "chih pi": complex(-0.99678E-05, 0.22652E-06)},

                   "2,2,0": {"chi0": complex(-0.18164E-04, 0.35107E-06),
                             "chih sigma": complex(-0.12808E-04, 0.33933E-06),
                             "chih pi": complex(-0.10348E-04, 0.27095E-06)},

                   "3,3,3": {"chi0": complex(-0.18164E-04, 0.35107E-06),
                             "chih sigma": complex(-0.59279E-05, 0.22130E-06),
                             "chih pi": complex(-0.20849E-05, 0.81661E-07)},

                   "4,4,0": {"chi0": complex(-0.18164E-04, 0.35107E-06),
                             "chih sigma": complex(-0.76327E-05, 0.30637E-06),
                             "chih pi": complex(-0.17682E-05, 0.78064E-07)}}

germanium_11kev = {"1,1,1": {"chi0": complex(-0.13836E-04, 0.24210E-06),
                             "chih sigma": complex(-0.80552E-05, 0.16905E-06),
                             "chih pi": complex(-0.75757E-05, 0.15841E-06)},

                   "2,2,0": {"chi0": complex(-0.13836E-04, 0.24210E-06),
                             "chih sigma": complex(-0.94430E-05, 0.23412E-06),
                             "chih pi": complex(-0.79440E-05, 0.19490E-06)},

                   "3,3,3": {"chi0": complex(-0.13836E-04, 0.24210E-06),
                             "chih sigma": complex(-0.41450E-05, 0.15286E-06),
                             "chih pi": complex(-0.19242E-05, 0.72595E-07)},

                   "4,4,0": {"chi0": complex(-0.13836E-04, 0.24210E-06),
                             "chih sigma": complex(-0.52606E-05, 0.21168E-06),
                             "chih pi": complex(-0.19202E-05, 0.81120E-07)}}

germanium = {"8keV": germanium_8kev,
             "9keV": germanium_9kev,
             "10keV": germanium_10kev,
             "11keV": germanium_11kev}

germanium_info = {"8keV": [8,
                           [(1, 1, 1), "1,1,1"],
                           [(2, 2, 0), "2,2,0"],
                           ],
                  "9keV": [9,
                           [(1, 1, 1), "1,1,1"],
                           [(2, 2, 0), "2,2,0"],
                           ],
                  "10keV": [10,
                            [(1, 1, 1), "1,1,1"],
                            [(2, 2, 0), "2,2,0"],
                            [(3, 3, 3), "3,3,3"],
                            [(4, 4, 0), "4,4,0"],
                            ],
                  "11keV": [11,
                            [(1, 1, 1), "1,1,1"],
                            [(2, 2, 0), "2,2,0"],
                            [(3, 3, 3), "3,3,3"],
                            [(4, 4, 0), "4,4,0"],
                            ],
                  }
