'''
Produce the constants table for the help files.  The constant's name
will be printed with its short-form uncertainty and units.
 
The data were downloaded Mon 30 Nov 2020 from 
https://physics.nist.gov/cuu/Constants/Table/allascii.txt
 
The title was
    Fundamental Physical Constants --- Complete Listing
    2018 CODATA adjustment
    From:  http://physics.nist.gov/constants
'''
if 1:  # Copyright, license
    # These "trigger strings" can be managed with trigger.py
    #∞copyright∞# Copyright (C) 2020 Don Peterson #∞copyright∞#
    #∞contact∞# gmail.com@someonesdad1 #∞contact∞#
    #∞license∞#
    #   Licensed under the Open Software License version 3.0.
    #   See http://opensource.org/licenses/OSL-3.0.
    #∞license∞#
    #∞what∞#
    # Print physical constants
    #∞what∞#
    #∞test∞# #∞test∞#
    pass
if 1:   # Standard imports
    import getopt
    import os
    import sys
    from uncertainties import ufloat
    from pdb import set_trace as xx
if 1:   # Custom imports
    from wrap import dedent
    from sig import sig
    from format_numbers import FormatNumber, FormatUnits
    from roundoff import RoundOff
    if 0:
        import debug
        debug.SetDebugger()  # Start debugger on unhandled exception
if 1:   # Global variables
    '''
    The table has been modified by the addition of an integer 1, 2, 3 to
    indicate the level of importance of the constant in my opinion.  The
    script will print level 1 constants by default.
 
    Ruler for column numbers
    0         1         2         3         4         5         6         7         8         9         10        11        12
    |....+....|....+....|....+....|....+....|....+....|....+....|....+....|....+....|....+....|....+....|....+....|....+....|
    '''
    data = dedent('''
    alpha particle-electron mass ratio                     2    7294.299 541 42          0.000 000 24             
    alpha particle mass                                    1    6.644 657 3357 e-27      0.000 000 0020 e-27      kg
    alpha particle mass energy equivalent                  2    5.971 920 1914 e-10      0.000 000 0018 e-10      J
    alpha particle mass energy equivalent in MeV           2    3727.379 4066            0.000 0011               MeV
    alpha particle mass in u                               2    4.001 506 179 127        0.000 000 000 063        u
    alpha particle molar mass                              2    4.001 506 1777 e-3       0.000 000 0012 e-3       kg mol^-1
    alpha particle-proton mass ratio                       2    3.972 599 690 09         0.000 000 000 22         
    alpha particle relative atomic mass                    2    4.001 506 179 127        0.000 000 000 063        
    Angstrom star                                          2    1.000 014 95 e-10        0.000 000 90 e-10        m
    atomic mass constant                                   1    1.660 539 066 60 e-27    0.000 000 000 50 e-27    kg
    atomic mass constant energy equivalent                 1    1.492 418 085 60 e-10    0.000 000 000 45 e-10    J
    atomic mass constant energy equivalent in MeV          2    931.494 102 42           0.000 000 28             MeV
    atomic mass unit-electron volt relationship            2    9.314 941 0242 e8        0.000 000 0028 e8        eV
    atomic mass unit-hartree relationship                  2    3.423 177 6874 e7        0.000 000 0010 e7        E_h
    atomic mass unit-hertz relationship                    2    2.252 342 718 71 e23     0.000 000 000 68 e23     Hz
    atomic mass unit-inverse meter relationship            2    7.513 006 6104 e14       0.000 000 0023 e14       m^-1
    atomic mass unit-kelvin relationship                   2    1.080 954 019 16 e13     0.000 000 000 33 e13     K
    atomic unit of 1st hyperpolarizability                 3    3.206 361 3061 e-53      0.000 000 0015 e-53      C^3 m^3 J^-2
    atomic unit of 2nd hyperpolarizability                 3    6.235 379 9905 e-65      0.000 000 0038 e-65      C^4 m^4 J^-3
    atomic unit of action                                  1    1.054 571 817... e-34    (exact)                  J s
    atomic unit of charge                                  1    1.602 176 634 e-19       (exact)                  C
    atomic unit of charge density                          2    1.081 202 384 57 e12     0.000 000 000 49 e12     C m^-3
    atomic unit of current                                 2    6.623 618 237 510 e-3    0.000 000 000 013 e-3    A
    atomic unit of electric dipole mom.                    2    8.478 353 6255 e-30      0.000 000 0013 e-30      C m
    atomic unit of electric field                          2    5.142 206 747 63 e11     0.000 000 000 78 e11     V m^-1
    atomic unit of electric field gradient                 2    9.717 362 4292 e21       0.000 000 0029 e21       V m^-2
    atomic unit of electric polarizability                 2    1.648 777 274 36 e-41    0.000 000 000 50 e-41    C^2 m^2 J^-1
    atomic unit of electric potential                      2    27.211 386 245 988       0.000 000 000 053        V
    atomic unit of electric quadrupole mom.                2    4.486 551 5246 e-40      0.000 000 0014 e-40      C m^2
    atomic unit of energy                                  2    4.359 744 722 2071 e-18  0.000 000 000 0085 e-18  J
    atomic unit of force                                   2    8.238 723 4983 e-8       0.000 000 0012 e-8       N
    atomic unit of length                                  2    5.291 772 109 03 e-11    0.000 000 000 80 e-11    m
    atomic unit of mag. dipole mom.                        2    1.854 802 015 66 e-23    0.000 000 000 56 e-23    J T^-1
    atomic unit of mag. flux density                       2    2.350 517 567 58 e5      0.000 000 000 71 e5      T
    atomic unit of magnetizability                         2    7.891 036 6008 e-29      0.000 000 0048 e-29      J T^-2
    atomic unit of mass                                    2    9.109 383 7015 e-31      0.000 000 0028 e-31      kg
    atomic unit of momentum                                2    1.992 851 914 10 e-24    0.000 000 000 30 e-24    kg m s^-1
    atomic unit of permittivity                            2    1.112 650 055 45 e-10    0.000 000 000 17 e-10    F m^-1
    atomic unit of time                                    2    2.418 884 326 5857 e-17  0.000 000 000 0047 e-17  s
    atomic unit of velocity                                2    2.187 691 263 64 e6      0.000 000 000 33 e6      m s^-1
    Avogadro constant                                      1    6.022 140 76 e23         (exact)                  mol^-1
    Bohr magneton                                          2    9.274 010 0783 e-24      0.000 000 0028 e-24      J T^-1
    Bohr magneton in eV/T                                  2    5.788 381 8060 e-5       0.000 000 0017 e-5       eV T^-1
    Bohr magneton in Hz/T                                  2    1.399 624 493 61 e10     0.000 000 000 42 e10     Hz T^-1
    Bohr magneton in inverse meter per tesla               2    46.686 447 783           0.000 000 014            m^-1 T^-1
    Bohr magneton in K/T                                   2    0.671 713 815 63         0.000 000 000 20         K T^-1
    Bohr radius                                            1    5.291 772 109 03 e-11    0.000 000 000 80 e-11    m
    Boltzmann constant                                     1    1.380 649 e-23           (exact)                  J K^-1
    Boltzmann constant in eV/K                             2    8.617 333 262... e-5     (exact)                  eV K^-1
    Boltzmann constant in Hz/K                             2    2.083 661 912... e10     (exact)                  Hz K^-1
    Boltzmann constant in inverse meter per kelvin         2    69.503 480 04...         (exact)                  m^-1 K^-1
    characteristic impedance of vacuum                     1    376.730 313 668          0.000 000 057            ohm
    classical electron radius                              2    2.817 940 3262 e-15      0.000 000 0013 e-15      m
    Compton wavelength                                     2    2.426 310 238 67 e-12    0.000 000 000 73 e-12    m
    conductance quantum                                    2    7.748 091 729... e-5     (exact)                  S
    conventional value of ampere-90                        2    1.000 000 088 87...      (exact)                  A
    conventional value of coulomb-90                       2    1.000 000 088 87...      (exact)                  C
    conventional value of farad-90                         2    0.999 999 982 20...      (exact)                  F
    conventional value of henry-90                         2    1.000 000 017 79...      (exact)                  H
    conventional value of Josephson constant               2    483 597.9 e9             (exact)                  Hz V^-1
    conventional value of ohm-90                           2    1.000 000 017 79...      (exact)                  ohm
    conventional value of volt-90                          2    1.000 000 106 66...      (exact)                  V
    conventional value of von Klitzing constant            2    25 812.807               (exact)                  ohm
    conventional value of watt-90                          2    1.000 000 195 53...      (exact)                  W
    Copper x unit                                          2    1.002 076 97 e-13        0.000 000 28 e-13        m
    deuteron-electron mag. mom. ratio                      2    -4.664 345 551 e-4       0.000 000 012 e-4        
    deuteron-electron mass ratio                           2    3670.482 967 88          0.000 000 13             
    deuteron g factor                                      2    0.857 438 2338           0.000 000 0022           
    deuteron mag. mom.                                     2    4.330 735 094 e-27       0.000 000 011 e-27       J T^-1
    deuteron mag. mom. to Bohr magneton ratio              2    4.669 754 570 e-4        0.000 000 012 e-4        
    deuteron mag. mom. to nuclear magneton ratio           2    0.857 438 2338           0.000 000 0022           
    deuteron mass                                          2    3.343 583 7724 e-27      0.000 000 0010 e-27      kg
    deuteron mass energy equivalent                        2    3.005 063 231 02 e-10    0.000 000 000 91 e-10    J
    deuteron mass energy equivalent in MeV                 2    1875.612 942 57          0.000 000 57             MeV
    deuteron mass in u                                     2    2.013 553 212 745        0.000 000 000 040        u
    deuteron molar mass                                    2    2.013 553 212 05 e-3     0.000 000 000 61 e-3     kg mol^-1
    deuteron-neutron mag. mom. ratio                       2    -0.448 206 53            0.000 000 11             
    deuteron-proton mag. mom. ratio                        2    0.307 012 209 39         0.000 000 000 79         
    deuteron-proton mass ratio                             2    1.999 007 501 39         0.000 000 000 11         
    deuteron relative atomic mass                          2    2.013 553 212 745        0.000 000 000 040        
    deuteron rms charge radius                             2    2.127 99 e-15            0.000 74 e-15            m
    electron charge to mass quotient                       1    -1.758 820 010 76 e11    0.000 000 000 53 e11     C kg^-1
    electron-deuteron mag. mom. ratio                      2    -2143.923 4915           0.000 0056               
    electron-deuteron mass ratio                           2    2.724 437 107 462 e-4    0.000 000 000 096 e-4    
    electron g factor                                      2    -2.002 319 304 362 56    0.000 000 000 000 35     
    electron gyromag. ratio                                2    1.760 859 630 23 e11     0.000 000 000 53 e11     s^-1 T^-1
    electron gyromag. ratio in MHz/T                       2    28 024.951 4242          0.000 0085               MHz T^-1
    electron-helion mass ratio                             2    1.819 543 074 573 e-4    0.000 000 000 079 e-4    
    electron mag. mom.                                     1    -9.284 764 7043 e-24     0.000 000 0028 e-24      J T^-1
    electron mag. mom. anomaly                             2    1.159 652 181 28 e-3     0.000 000 000 18 e-3     
    electron mag. mom. to Bohr magneton ratio              2    -1.001 159 652 181 28    0.000 000 000 000 18     
    electron mag. mom. to nuclear magneton ratio           2    -1838.281 971 88         0.000 000 11             
    electron mass                                          1    9.109 383 7015 e-31      0.000 000 0028 e-31      kg
    electron mass energy equivalent                        2    8.187 105 7769 e-14      0.000 000 0025 e-14      J
    electron mass energy equivalent in MeV                 2    0.510 998 950 00         0.000 000 000 15         MeV
    electron mass in u                                     2    5.485 799 090 65 e-4     0.000 000 000 16 e-4     u
    electron molar mass                                    2    5.485 799 0888 e-7       0.000 000 0017 e-7       kg mol^-1
    electron-muon mag. mom. ratio                          2    206.766 9883             0.000 0046               
    electron-muon mass ratio                               2    4.836 331 69 e-3         0.000 000 11 e-3         
    electron-neutron mag. mom. ratio                       2    960.920 50               0.000 23                 
    electron-neutron mass ratio                            2    5.438 673 4424 e-4       0.000 000 0026 e-4       
    electron-proton mag. mom. ratio                        2    -658.210 687 89          0.000 000 20             
    electron-proton mass ratio                             1    5.446 170 214 87 e-4     0.000 000 000 33 e-4     
    electron relative atomic mass                          2    5.485 799 090 65 e-4     0.000 000 000 16 e-4     
    electron-tau mass ratio                                2    2.875 85 e-4             0.000 19 e-4             
    electron to alpha particle mass ratio                  2    1.370 933 554 787 e-4    0.000 000 000 045 e-4    
    electron to shielded helion mag. mom. ratio            2    864.058 257              0.000 010                
    electron to shielded proton mag. mom. ratio            2    -658.227 5971            0.000 0072               
    electron-triton mass ratio                             2    1.819 200 062 251 e-4    0.000 000 000 090 e-4    
    electron volt                                          1    1.602 176 634 e-19       (exact)                  J
    electron volt-atomic mass unit relationship            2    1.073 544 102 33 e-9     0.000 000 000 32 e-9     u
    electron volt-hartree relationship                     2    3.674 932 217 5655 e-2   0.000 000 000 0071 e-2   E_h
    electron volt-hertz relationship                       2    2.417 989 242... e14     (exact)                  Hz
    electron volt-inverse meter relationship               2    8.065 543 937... e5      (exact)                  m^-1
    electron volt-joule relationship                       2    1.602 176 634 e-19       (exact)                  J
    electron volt-kelvin relationship                      2    1.160 451 812... e4      (exact)                  K
    electron volt-kilogram relationship                    2    1.782 661 921... e-36    (exact)                  kg
    elementary charge                                      1    1.602 176 634 e-19       (exact)                  C
    elementary charge over h-bar                           2    1.519 267 447... e15     (exact)                  A J^-1
    Faraday constant                                       1    96 485.332 12...         (exact)                  C mol^-1
    Fermi coupling constant                                2    1.166 3787 e-5           0.000 0006 e-5           GeV^-2
    fine-structure constant                                2    7.297 352 5693 e-3       0.000 000 0011 e-3       
    first radiation constant                               2    3.741 771 852... e-16    (exact)                  W m^2
    first radiation constant for spectral radiance         2    1.191 042 972... e-16    (exact)                  W m^2 sr^-1
    hartree-atomic mass unit relationship                  2    2.921 262 322 05 e-8     0.000 000 000 88 e-8     u
    hartree-electron volt relationship                     2    27.211 386 245 988       0.000 000 000 053        eV
    Hartree energy                                         2    4.359 744 722 2071 e-18  0.000 000 000 0085 e-18  J
    Hartree energy in eV                                   2    27.211 386 245 988       0.000 000 000 053        eV
    hartree-hertz relationship                             2    6.579 683 920 502 e15    0.000 000 000 013 e15    Hz
    hartree-inverse meter relationship                     2    2.194 746 313 6320 e7    0.000 000 000 0043 e7    m^-1
    hartree-joule relationship                             2    4.359 744 722 2071 e-18  0.000 000 000 0085 e-18  J
    hartree-kelvin relationship                            2    3.157 750 248 0407 e5    0.000 000 000 0061 e5    K
    hartree-kilogram relationship                          2    4.850 870 209 5432 e-35  0.000 000 000 0094 e-35  kg
    helion-electron mass ratio                             2    5495.885 280 07          0.000 000 24             
    helion g factor                                        2    -4.255 250 615           0.000 000 050            
    helion mag. mom.                                       2    -1.074 617 532 e-26      0.000 000 013 e-26       J T^-1
    helion mag. mom. to Bohr magneton ratio                2    -1.158 740 958 e-3       0.000 000 014 e-3        
    helion mag. mom. to nuclear magneton ratio             2    -2.127 625 307           0.000 000 025            
    helion mass                                            2    5.006 412 7796 e-27      0.000 000 0015 e-27      kg
    helion mass energy equivalent                          2    4.499 539 4125 e-10      0.000 000 0014 e-10      J
    helion mass energy equivalent in MeV                   2    2808.391 607 43          0.000 000 85             MeV
    helion mass in u                                       2    3.014 932 247 175        0.000 000 000 097        u
    helion molar mass                                      2    3.014 932 246 13 e-3     0.000 000 000 91 e-3     kg mol^-1
    helion-proton mass ratio                               2    2.993 152 671 67         0.000 000 000 13         
    helion relative atomic mass                            2    3.014 932 247 175        0.000 000 000 097        
    helion shielding shift                                 2    5.996 743 e-5            0.000 010 e-5            
    hertz-atomic mass unit relationship                    2    4.439 821 6652 e-24      0.000 000 0013 e-24      u
    hertz-electron volt relationship                       2    4.135 667 696... e-15    (exact)                  eV
    hertz-hartree relationship                             2    1.519 829 846 0570 e-16  0.000 000 000 0029 e-16  E_h
    hertz-inverse meter relationship                       2    3.335 640 951... e-9     (exact)                  m^-1
    hertz-joule relationship                               2    6.626 070 15 e-34        (exact)                  J
    hertz-kelvin relationship                              2    4.799 243 073... e-11    (exact)                  K
    hertz-kilogram relationship                            2    7.372 497 323... e-51    (exact)                  kg
    hyperfine transition frequency of Cs-133               1    9 192 631 770            (exact)                  Hz
    inverse fine-structure constant                        2    137.035 999 084          0.000 000 021            
    inverse meter-atomic mass unit relationship            2    1.331 025 050 10 e-15    0.000 000 000 40 e-15    u
    inverse meter-electron volt relationship               2    1.239 841 984... e-6     (exact)                  eV
    inverse meter-hartree relationship                     2    4.556 335 252 9120 e-8   0.000 000 000 0088 e-8   E_h
    inverse meter-hertz relationship                       2    299 792 458              (exact)                  Hz
    inverse meter-joule relationship                       2    1.986 445 857... e-25    (exact)                  J
    inverse meter-kelvin relationship                      2    1.438 776 877... e-2     (exact)                  K
    inverse meter-kilogram relationship                    2    2.210 219 094... e-42    (exact)                  kg
    inverse of conductance quantum                         2    12 906.403 72...         (exact)                  ohm
    Josephson constant                                     2    483 597.848 4... e9      (exact)                  Hz V^-1
    joule-atomic mass unit relationship                    2    6.700 535 2565 e9        0.000 000 0020 e9        u
    joule-electron volt relationship                       2    6.241 509 074... e18     (exact)                  eV
    joule-hartree relationship                             2    2.293 712 278 3963 e17   0.000 000 000 0045 e17   E_h
    joule-hertz relationship                               2    1.509 190 179... e33     (exact)                  Hz
    joule-inverse meter relationship                       2    5.034 116 567... e24     (exact)                  m^-1
    joule-kelvin relationship                              2    7.242 970 516... e22     (exact)                  K
    joule-kilogram relationship                            2    1.112 650 056... e-17    (exact)                  kg
    kelvin-atomic mass unit relationship                   2    9.251 087 3014 e-14      0.000 000 0028 e-14      u
    kelvin-electron volt relationship                      2    8.617 333 262... e-5     (exact)                  eV
    kelvin-hartree relationship                            2    3.166 811 563 4556 e-6   0.000 000 000 0061 e-6   E_h
    kelvin-hertz relationship                              2    2.083 661 912... e10     (exact)                  Hz
    kelvin-inverse meter relationship                      2    69.503 480 04...         (exact)                  m^-1
    kelvin-joule relationship                              2    1.380 649 e-23           (exact)                  J
    kelvin-kilogram relationship                           2    1.536 179 187... e-40    (exact)                  kg
    kilogram-atomic mass unit relationship                 2    6.022 140 7621 e26       0.000 000 0018 e26       u
    kilogram-electron volt relationship                    2    5.609 588 603... e35     (exact)                  eV
    kilogram-hartree relationship                          2    2.061 485 788 7409 e34   0.000 000 000 0040 e34   E_h
    kilogram-hertz relationship                            2    1.356 392 489... e50     (exact)                  Hz
    kilogram-inverse meter relationship                    2    4.524 438 335... e41     (exact)                  m^-1
    kilogram-joule relationship                            2    8.987 551 787... e16     (exact)                  J
    kilogram-kelvin relationship                           2    6.509 657 260... e39     (exact)                  K
    lattice parameter of silicon                           2    5.431 020 511 e-10       0.000 000 089 e-10       m
    lattice spacing of ideal Si (220)                      2    1.920 155 716 e-10       0.000 000 032 e-10       m
    Loschmidt constant (273.15 K, 100 kPa)                 2    2.651 645 804... e25     (exact)                  m^-3
    Loschmidt constant (273.15 K, 101.325 kPa)             2    2.686 780 111... e25     (exact)                  m^-3
    luminous efficacy                                      2    683                      (exact)                  lm W^-1
    mag. flux quantum                                      2    2.067 833 848... e-15    (exact)                  Wb
    molar gas constant                                     1    8.314 462 618...         (exact)                  J mol^-1 K^-1
    molar mass constant                                    1    0.999 999 999 65 e-3     0.000 000 000 30 e-3     kg mol^-1
    molar mass of carbon-12                                2    11.999 999 9958 e-3      0.000 000 0036 e-3       kg mol^-1
    molar Planck constant                                  2    3.990 312 712... e-10    (exact)                  J Hz^-1 mol^-1
    molar volume of ideal gas (273.15 K, 100 kPa)          2    22.710 954 64... e-3     (exact)                  m^3 mol^-1
    molar volume of idl. gas (273.15 K, 101.325 kPa)       2    22.413 969 54... e-3     (exact)                  m^3 mol^-1
    molar volume of silicon                                2    1.205 883 199 e-5        0.000 000 060 e-5        m^3 mol^-1
    Molybdenum x unit                                      2    1.002 099 52 e-13        0.000 000 53 e-13        m
    muon Compton wavelength                                2    1.173 444 110 e-14       0.000 000 026 e-14       m
    muon-electron mass ratio                               2    206.768 2830             0.000 0046               
    muon g factor                                          2    -2.002 331 8418          0.000 000 0013           
    muon mag. mom.                                         2    -4.490 448 30 e-26       0.000 000 10 e-26        J T^-1
    muon mag. mom. anomaly                                 2    1.165 920 89 e-3         0.000 000 63 e-3         
    muon mag. mom. to Bohr magneton ratio                  2    -4.841 970 47 e-3        0.000 000 11 e-3         
    muon mag. mom. to nuclear magneton ratio               2    -8.890 597 03            0.000 000 20             
    muon mass                                              2    1.883 531 627 e-28       0.000 000 042 e-28       kg
    muon mass energy equivalent                            2    1.692 833 804 e-11       0.000 000 038 e-11       J
    muon mass energy equivalent in MeV                     2    105.658 3755             0.000 0023               MeV
    muon mass in u                                         2    0.113 428 9259           0.000 000 0025           u
    muon molar mass                                        2    1.134 289 259 e-4        0.000 000 025 e-4        kg mol^-1
    muon-neutron mass ratio                                2    0.112 454 5170           0.000 000 0025           
    muon-proton mag. mom. ratio                            2    -3.183 345 142           0.000 000 071            
    muon-proton mass ratio                                 2    0.112 609 5264           0.000 000 0025           
    muon-tau mass ratio                                    2    5.946 35 e-2             0.000 40 e-2             
    natural unit of action                                 2    1.054 571 817... e-34    (exact)                  J s
    natural unit of action in eV s                         2    6.582 119 569... e-16    (exact)                  eV s
    natural unit of energy                                 2    8.187 105 7769 e-14      0.000 000 0025 e-14      J
    natural unit of energy in MeV                          2    0.510 998 950 00         0.000 000 000 15         MeV
    natural unit of length                                 2    3.861 592 6796 e-13      0.000 000 0012 e-13      m
    natural unit of mass                                   2    9.109 383 7015 e-31      0.000 000 0028 e-31      kg
    natural unit of momentum                               2    2.730 924 530 75 e-22    0.000 000 000 82 e-22    kg m s^-1
    natural unit of momentum in MeV/c                      2    0.510 998 950 00         0.000 000 000 15         MeV/c
    natural unit of time                                   2    1.288 088 668 19 e-21    0.000 000 000 39 e-21    s
    natural unit of velocity                               2    299 792 458              (exact)                  m s^-1
    neutron Compton wavelength                             2    1.319 590 905 81 e-15    0.000 000 000 75 e-15    m
    neutron-electron mag. mom. ratio                       2    1.040 668 82 e-3         0.000 000 25 e-3         
    neutron-electron mass ratio                            1    1838.683 661 73          0.000 000 89             
    neutron g factor                                       2    -3.826 085 45            0.000 000 90             
    neutron gyromag. ratio                                 2    1.832 471 71 e8          0.000 000 43 e8          s^-1 T^-1
    neutron gyromag. ratio in MHz/T                        2    29.164 6931              0.000 0069               MHz T^-1
    neutron mag. mom.                                      2    -9.662 3651 e-27         0.000 0023 e-27          J T^-1
    neutron mag. mom. to Bohr magneton ratio               2    -1.041 875 63 e-3        0.000 000 25 e-3         
    neutron mag. mom. to nuclear magneton ratio            2    -1.913 042 73            0.000 000 45             
    neutron mass                                           1    1.674 927 498 04 e-27    0.000 000 000 95 e-27    kg
    neutron mass energy equivalent                         2    1.505 349 762 87 e-10    0.000 000 000 86 e-10    J
    neutron mass energy equivalent in MeV                  2    939.565 420 52           0.000 000 54             MeV
    neutron mass in u                                      2    1.008 664 915 95         0.000 000 000 49         u
    neutron molar mass                                     2    1.008 664 915 60 e-3     0.000 000 000 57 e-3     kg mol^-1
    neutron-muon mass ratio                                2    8.892 484 06             0.000 000 20             
    neutron-proton mag. mom. ratio                         2    -0.684 979 34            0.000 000 16             
    neutron-proton mass difference                         2    2.305 574 35 e-30        0.000 000 82 e-30        kg
    neutron-proton mass difference energy equivalent       2    2.072 146 89 e-13        0.000 000 74 e-13        J
    neutron-proton mass diff energy equiv. in MeV          2    1.293 332 36             0.000 000 46             MeV
    neutron-proton mass difference in u                    2    1.388 449 33 e-3         0.000 000 49 e-3         u
    neutron-proton mass ratio                              2    1.001 378 419 31         0.000 000 000 49         
    neutron relative atomic mass                           2    1.008 664 915 95         0.000 000 000 49         
    neutron-tau mass ratio                                 2    0.528 779                0.000 036                
    neutron to shielded proton mag. mom. ratio             2    -0.684 996 94            0.000 000 16             
    Newtonian constant of gravitation                      1    6.674 30 e-11            0.000 15 e-11            m^3 kg^-1 s^-2
    Newtonian constant of gravitation over h-bar c         2    6.708 83 e-39            0.000 15 e-39            c^4/GeV^-2
    nuclear magneton                                       2    5.050 783 7461 e-27      0.000 000 0015 e-27      J T^-1
    nuclear magneton in eV/T                               2    3.152 451 258 44 e-8     0.000 000 000 96 e-8     eV T^-1
    nuclear magneton in inverse meter per tesla            2    2.542 623 413 53 e-2     0.000 000 000 78 e-2     m^-1 T^-1
    nuclear magneton in K/T                                2    3.658 267 7756 e-4       0.000 000 0011 e-4       K T^-1
    nuclear magneton in MHz/T                              2    7.622 593 2291           0.000 000 0023           MHz T^-1
    Planck constant                                        1    6.626 070 15 e-34        (exact)                  J Hz^-1
    Planck constant in eV/Hz                               2    4.135 667 696... e-15    (exact)                  eV Hz^-1
    Planck length                                          2    1.616 255 e-35           0.000 018 e-35           m
    Planck mass                                            2    2.176 434 e-8            0.000 024 e-8            kg
    Planck mass energy equivalent in GeV                   2    1.220 890 e19            0.000 014 e19            GeV
    Planck temperature                                     2    1.416 784 e32            0.000 016 e32            K
    Planck time                                            2    5.391 247 e-44           0.000 060 e-44           s
    proton charge to mass quotient                         2    9.578 833 1560 e7        0.000 000 0029 e7        C kg^-1
    proton Compton wavelength                              2    1.321 409 855 39 e-15    0.000 000 000 40 e-15    m
    proton-electron mass ratio                             1    1836.152 673 43          0.000 000 11             
    proton g factor                                        2    5.585 694 6893           0.000 000 0016           
    proton gyromag. ratio                                  2    2.675 221 8744 e8        0.000 000 0011 e8        s^-1 T^-1
    proton gyromag. ratio in MHz/T                         2    42.577 478 518           0.000 000 018            MHz T^-1
    proton mag. mom.                                       2    1.410 606 797 36 e-26    0.000 000 000 60 e-26    J T^-1
    proton mag. mom. to Bohr magneton ratio                2    1.521 032 202 30 e-3     0.000 000 000 46 e-3     
    proton mag. mom. to nuclear magneton ratio             2    2.792 847 344 63         0.000 000 000 82         
    proton mag. shielding correction                       2    2.5689 e-5               0.0011 e-5               
    proton mass                                            1    1.672 621 923 69 e-27    0.000 000 000 51 e-27    kg
    proton mass energy equivalent                          2    1.503 277 615 98 e-10    0.000 000 000 46 e-10    J
    proton mass energy equivalent in MeV                   2    938.272 088 16           0.000 000 29             MeV
    proton mass in u                                       2    1.007 276 466 621        0.000 000 000 053        u
    proton molar mass                                      2    1.007 276 466 27 e-3     0.000 000 000 31 e-3     kg mol^-1
    proton-muon mass ratio                                 2    8.880 243 37             0.000 000 20             
    proton-neutron mag. mom. ratio                         2    -1.459 898 05            0.000 000 34             
    proton-neutron mass ratio                              2    0.998 623 478 12         0.000 000 000 49         
    proton relative atomic mass                            2    1.007 276 466 621        0.000 000 000 053        
    proton rms charge radius                               2    8.414 e-16               0.019 e-16               m
    proton-tau mass ratio                                  2    0.528 051                0.000 036                
    quantum of circulation                                 2    3.636 947 5516 e-4       0.000 000 0011 e-4       m^2 s^-1
    quantum of circulation times 2                         2    7.273 895 1032 e-4       0.000 000 0022 e-4       m^2 s^-1
    reduced Compton wavelength                             2    3.861 592 6796 e-13      0.000 000 0012 e-13      m
    reduced muon Compton wavelength                        2    1.867 594 306 e-15       0.000 000 042 e-15       m
    reduced neutron Compton wavelength                     2    2.100 194 1552 e-16      0.000 000 0012 e-16      m
    reduced Planck constant                                2    1.054 571 817... e-34    (exact)                  J s
    reduced Planck constant in eV s                        2    6.582 119 569... e-16    (exact)                  eV s
    reduced Planck constant times c in MeV fm              2    197.326 980 4...         (exact)                  MeV fm
    reduced proton Compton wavelength                      2    2.103 089 103 36 e-16    0.000 000 000 64 e-16    m
    reduced tau Compton wavelength                         2    1.110 538 e-16           0.000 075 e-16           m
    Rydberg constant                                       2    10 973 731.568 160       0.000 021                m^-1
    Rydberg constant times c in Hz                         2    3.289 841 960 2508 e15   0.000 000 000 0064 e15   Hz
    Rydberg constant times hc in eV                        2    13.605 693 122 994       0.000 000 000 026        eV
    Rydberg constant times hc in J                         2    2.179 872 361 1035 e-18  0.000 000 000 0042 e-18  J
    Sackur-Tetrode constant (1 K, 100 kPa)                 2    -1.151 707 537 06        0.000 000 000 45         
    Sackur-Tetrode constant (1 K, 101.325 kPa)             2    -1.164 870 523 58        0.000 000 000 45         
    second radiation constant                              2    1.438 776 877... e-2     (exact)                  m K
    shielded helion gyromag. ratio                         2    2.037 894 569 e8         0.000 000 024 e8         s^-1 T^-1
    shielded helion gyromag. ratio in MHz/T                2    32.434 099 42            0.000 000 38             MHz T^-1
    shielded helion mag. mom.                              2    -1.074 553 090 e-26      0.000 000 013 e-26       J T^-1
    shielded helion mag. mom. to Bohr magneton rat.        2    -1.158 671 471 e-3       0.000 000 014 e-3        
    shielded helion mag. mom. to nucl. magneton rat.       2    -2.127 497 719           0.000 000 025            
    shielded helion to proton mag. mom. rat.               2    -0.761 766 5618          0.000 000 0089           
    shielded helion to shielded proton mag mom rat         2    -0.761 786 1313          0.000 000 0033           
    shielded proton gyromag. ratio                         2    2.675 153 151 e8         0.000 000 029 e8         s^-1 T^-1
    shielded proton gyromag. ratio in MHz/T                2    42.576 384 74            0.000 000 46             MHz T^-1
    shielded proton mag. mom.                              2    1.410 570 560 e-26       0.000 000 015 e-26       J T^-1
    shielded proton mag. mom. to Bohr magneton rat.        2    1.520 993 128 e-3        0.000 000 017 e-3        
    shielded proton mag. mom. to nucl. magnetn rat.        2    2.792 775 599            0.000 000 030            
    shielding difference of d and p in HD                  2    2.0200 e-8               0.0020 e-8               
    shielding difference of t and p in HT                  2    2.4140 e-8               0.0020 e-8               
    speed of light in vacuum                               1    299 792 458              (exact)                  m s^-1
    standard acceleration of gravity                       1    9.806 65                 (exact)                  m s^-2
    standard atmosphere                                    1    101 325                  (exact)                  Pa
    standard-state pressure                                2    100 000                  (exact)                  Pa
    Stefan-Boltzmann constant                              1    5.670 374 419... e-8     (exact)                  W m^-2 K^-4
    tau Compton wavelength                                 2    6.977 71 e-16            0.000 47 e-16            m
    tau-electron mass ratio                                2    3477.23                  0.23                     
    tau energy equivalent                                  2    1776.86                  0.12                     MeV
    tau mass                                               2    3.167 54 e-27            0.000 21 e-27            kg
    tau mass energy equivalent                             2    2.846 84 e-10            0.000 19 e-10            J
    tau mass in u                                          2    1.907 54                 0.000 13                 u
    tau molar mass                                         2    1.907 54 e-3             0.000 13 e-3             kg mol^-1
    tau-muon mass ratio                                    2    16.8170                  0.0011                   
    tau-neutron mass ratio                                 2    1.891 15                 0.000 13                 
    tau-proton mass ratio                                  2    1.893 76                 0.000 13                 
    Thomson cross section                                  2    6.652 458 7321 e-29      0.000 000 0060 e-29      m^2
    triton-electron mass ratio                             2    5496.921 535 73          0.000 000 27             
    triton g factor                                        2    5.957 924 931            0.000 000 012            
    triton mag. mom.                                       2    1.504 609 5202 e-26      0.000 000 0030 e-26      J T^-1
    triton mag. mom. to Bohr magneton ratio                2    1.622 393 6651 e-3       0.000 000 0032 e-3       
    triton mag. mom. to nuclear magneton ratio             2    2.978 962 4656           0.000 000 0059           
    triton mass                                            2    5.007 356 7446 e-27      0.000 000 0015 e-27      kg
    triton mass energy equivalent                          2    4.500 387 8060 e-10      0.000 000 0014 e-10      J
    triton mass energy equivalent in MeV                   2    2808.921 132 98          0.000 000 85             MeV
    triton mass in u                                       2    3.015 500 716 21         0.000 000 000 12         u
    triton molar mass                                      2    3.015 500 715 17 e-3     0.000 000 000 92 e-3     kg mol^-1
    triton-proton mass ratio                               2    2.993 717 034 14         0.000 000 000 15         
    triton relative atomic mass                            2    3.015 500 716 21         0.000 000 000 12         
    triton to proton mag. mom. ratio                       2    1.066 639 9191           0.000 000 0021           
    unified atomic mass unit                               1    1.660 539 066 60 e-27    0.000 000 000 50 e-27    kg
    vacuum electric permittivity                           1    8.854 187 8128 e-12      0.000 000 0013 e-12      F m^-1
    vacuum magnetic permeability                           1    1.256 637 062 12 e-6     0.000 000 000 19 e-6     N A^-2
    von Klitzing constant                                  2    25 812.807 45...         (exact)                  ohm
    weak mixing angle                                      2    0.222 90                 0.000 30                 
    Wien frequency displacement law constant               2    5.878 925 757... e10     (exact)                  Hz K^-1
    Wien wavelength displacement law constant              2    2.897 771 955... e-3     (exact)                  m K
    W to Z mass ratio                                      2    0.881 53                 0.000 17                 
    '''.rstrip())
def Error(msg, status=1):
    print(msg, file=sys.stderr)
    exit(status)
def Usage(d, status=1):
    name = sys.argv[0]
    s = f'''
Usage:  {name} [options] [regex1 [regex2 ...]]
  Print fundamental physical constants with their uncertainties and
  physical units.  If regular expressions are given, display all entries
  that contain the regular expression.
Options:
  -d n      Print n significant figures
  -l n      Print the indicated level (1 == default, 2 == more, 3 == all)
'''[1:-1]
    print(s)
    exit(status)
def ParseCommandLine(d):
    d["-d"] = None      # Significant figures
    d["-l"] = 1         # Level to print
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:l:")
    except getopt.GetoptError as e:
        print(str(e))
        exit(1)
    for o, a in opts:
        if o == "-d":
            try:
                d["-d"] = int(a)
                if not (1 <= d["-d"] <= 15):
                    raise ValueError()
            except ValueError:
                msg = ("-d option's argument must be an integer between "
                       "1 and 15")
                Error(msg)
        elif o == "-l":
            msg = ("-l option's argument must be an integer between "
                    "1 and 3 inclusive")
            try:
                d["-l"] = int(a)
                if not (1 <= d["-l"] <= 3):
                    raise ValueError()
            except ValueError:
                Error(msg)
    return args
def GetFloat(s):
    'Return s converted to a float'
    s = s.replace(" ", "")
    s = s.replace("...", "")
    if s == "(exact)":
        return 0.0
    return float(s)
def GetData():
    'Parse the raw data to get the constants'
    constants = []
    for line in data.split("\n"):
        line = line.strip()
        if not line or line[0] == "#":
            continue
        name = line[:55].strip()
        name = name[0].upper() + name[1:]
        level = int(line[55])
        val = line[60:84].strip().replace(" ", "").replace("...", "")
        unc = line[85:109].strip().replace(" ", "")
        exact = True if unc == "(exact)" else False
        v = float(val)
        u = 0 if exact else float(unc)
        units = line[110:].strip()
        value = ufloat(v, u) if u else v
        if d["-d"]:
            f = FormatNumber(RoundOff(v, digits=d["-d"]), units=units, exact=exact, solidus=True)
        else:
            f = FormatNumber(value, units=units, exact=exact, solidus=True)
        constants.append((name, level, f))
    return constants
def Report(constants):
    n = 79
    print(dedent(f'''
    {'Physical Constants':^{n}s}
    {'2018 CODATA adjustment':^{n}s}
    {'http://physics.nist.gov/constants':^{n}s}
    '''))
    # Get length of longest name
    maxlen = max(len(i[0]) for i in constants)
    for name, level, num in sorted(constants):
        if level <= d["-l"]:
            print(f"{name:{maxlen}s} {num}")
if __name__ == "__main__":
    d = {}      # Options dictionary
    args = ParseCommandLine(d)
    constants = GetData()
    Report(constants)
