'''
Tap drill sizes calculated as OD - 1/pitch
'''
def English():
    sizes = [
        # OD       TPI      Class    OD decimal
        [ "0",     "80",    "UNF",   .060, ],
        [ "1",     "64",    "UNC",   .073, ],
        [ "1",     "72",    "UNF",   .073, ],
        [ "2",     "56",    "UNC",   .086, ],
        [ "2",     "64",    "UNF",   .086, ],
        [ "3",     "48",    "UNC",   .099, ],
        [ "3",     "56",    "UNF",   .099, ],
        [ "4",     "40",    "UNC",   .112, ],
        [ "4",     "48",    "UNF",   .112, ],
        [ "5",     "40",    "UNC",   .125, ],
        [ "5",     "44",    "UNF",   .125, ],
        [ "6",     "32",    "UNC",   .138, ],
        [ "6",     "40",    "UNF",   .138, ],
        [ "8",     "32",    "UNC",   .164, ],
        [ "8",     "36",    "UNF",   .164, ],
        [ "10",    "24",    "UNC",   .190, ],
        [ "10",    "32",    "UNF",   .190, ],
        [ "12",    "24",    "UNC",   .216, ],
        [ "12",    "28",    "UNF",   .216, ],
        [ "1/4",   "28",    "UNF",   1/4,  ],
        [ "1/4",   "20",    "UNC",   1/4,  ],
        [ "5/16",  "18",    "UNC",   5/16, ],
        [ "5/16",  "24",    "UNF",   5/16, ],
        [ "3/8",   "16",    "UNC",   3/8,  ],
        [ "3/8",   "24",    "UNF",   3/8,  ],
        [ "7/16",  "14",    "UNC",   7/16, ],
        [ "7/16",  "20",    "UNF",   7/16, ],
        [ "1/2",   "13",    "UNC",   1/2,  ],
        [ "1/2",   "20",    "UNF",   1/2,  ],
        [ "9/16",  "12",    "UNC",   9/16, ],
        [ "9/16",  "18",    "UNF",   9/16, ],
        [ "5/8",   "11",    "UNC",   5/8,  ],
        [ "5/8",   "18",    "UNF",   5/8,  ],
        [ "3/4",   "10",    "UNC",   3/4,  ],
        [ "3/4",   "16",    "UNF",   3/4,  ],
        [ "7/8",   "9",     "UNC",   7/8,  ],
        [ "7/8",   "14",    "UNF",   7/8,  ],
        [ "1",     "8",     "UNC",   1,    ],
        [ "1",     "12",    "UNF",   1,    ],
    ]
    print("Thread    Class  Tap drill")
    print("------    -----  ---------")
    for size in sizes:
        OD, TPI, Class, od = size
        pitch = 1/float(TPI)
        tap_drill = od - pitch
        name = OD + "-" + TPI
        print("%(name)-8s   %(Class)-4s    %(tap_drill).3f" % locals())
def Metric():
    sizes = [
        [ "1.6",   ".35",   "Coarse"],
        [ "1.6",   ".2",    "Fine"  ],
        [ "2",     ".4",    "Coarse"],
        [ "2",     ".25",   "Fine"  ],
        [ "2.5",   ".45",   "Coarse"],
        [ "2.5",   ".35",   "Fine"  ],
        [ "3",     ".5",    "Coarse"],
        [ "3",     ".35",   "Fine"  ],
        [ "3.5",   ".4",    "Coarse"],
        [ "3.5",   ".35",   "Fine"  ],
        [ "4",     ".7",    "Coarse"],
        [ "4",     ".5",    "Fine"  ],
        [ "4.5",   ".75",   "Coarse"],
        [ "4.5",   ".5",    "Fine"  ],
        [ "5",     ".8",    "Coarse"],
        [ "5",     ".5",    "Fine"  ],
        [ "6",     "1",     "Coarse"],
        [ "6",     ".75",   "Fine"  ],
        [ "7",     "1"  ,   "Coarse"],
        [ "7",     ".75",   "Fine"  ],
        [ "8",     "1.25",  "Coarse"],
        [ "8",     "1",     "Fine"  ],
        [ "10",    "1.5",   "Coarse"],
        [ "10",    "1.25",  "Fine"  ],
        [ "12",    "1.75",  "Coarse"],
        [ "12",    "1.25",  "Fine"  ],
        [ "14",    "2",     "Coarse"],
        [ "14",    "1.5",   "Fine"  ],
        [ "16",    "2",     "Coarse"],
        [ "16",    "1.5",   "Fine"  ],
        [ "18",    "2.5",   "Coarse"],
        [ "18",    "1.5",   "Fine"  ],
        [ "20",    "2.5",   "Coarse"],
        [ "20",    "1.5",   "Fine"  ],
        [ "22",    "2.5",   "Coarse"],
        [ "22",    "1.5",   "Fine"  ],
        [ "24",    "3",     "Coarse"],
        [ "24",    "2",     "Fine"  ],
    ]
    print("Thread     Class    Tap drill    Inches")
    print("------     ------   ---------    ------")
    for size in sizes:
        OD, PITCH, Class = size
        pitch = float(PITCH)
        od    = float(OD)
        tap_drill = od - pitch
        name = "M" + OD + "-" + PITCH
        inches = tap_drill/25.4
        print("%(name)-8s   %(Class)-6s      %(tap_drill)4.1f %(inches)10.3f" % locals())
English()
print()
Metric()
