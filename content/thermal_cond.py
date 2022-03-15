'''
Print out an ASCII table of thermal conductivities in W/m*K.
'''
import sys
from sig import sig
# Thermal conductivities of common materials at 75 degF in
# Btu*in/ft^2*hr*degF.  Multiply by 0.1442 to get in W/m*K.
k = (
    ("Insulation",),
    ("Sawdust",                             0.36),
    ("Wood shavings",                       0.41),
    ("Standard fiberglass batt",                0.313),
    ("High performance fiberglass batt",    0.263),
    ("Loose-fill fiberglass",               0.400),
    ("Loose-fill rock wool",                0.357),
    ("Loose-fill cellulose",                0.270),
    ("Expanded polystyrene",                0.263),
    ("Extruded polystyrene",                0.208),
 
    ("Gases",),
    ("Air",                                 0.181),
    ("Carbon dioxide",                      0.115),
    ("Helium",                              1.04 ),
    ("Methane",                             0.237),
 
    ("Liquids",),
    ("Ethylene glycol",                     1.80 ),
    ("Gasoline",                            0.94 ),
    ("Water",                               4.19 ),
 
    ("Metals",),
    ("Aluminum",                            1890 ),
    ("Copper",                              2760 ),
    ("Iron",                                555  ),
    ("Lead",                                240  ),
 
    ("Miscellaneous",),
    ("Acoustical tile",                     0.40 ),
    ("Asphalt",                             5.2  ),
    ("Concrete (2.25 sp gr)",              12.0 ),
    ("Cotton (0.1 sp gr)",                  0.30 ),
    ("Fir",                                 0.76 ),
    ("Oak",                                 1.18 ),
    ("Plywood",                             0.83 ),
    ("Soil, low",                           4 ),
    ("Soil, high",                          20 ),
    ("Window glass",                        6.10 ),
    ("Yellow Pine",                         1.04 ),
)
def out(*v, **kw):
    '''Utility output to a stream.  Keywords:
    sep     Separator between *v elements
    nl      Include newline when finished with *v
    stream  Where to output
    rep     How to convert objects to a string 
    '''
    sep = kw.setdefault("sep", " ")
    nl  = kw.setdefault("nl", True)
    stream = kw.setdefault("stream", sys.stdout)
    rep  = kw.setdefault("repr", str)
    if v:
        stream.write(sep.join([rep(i) for i in v]))
    if nl:
        stream.write("\n")
out('''Thermal conductivities
  Values in W/(m*K).  To convert to Btu*in/ft^2*hr*degF, multiply by
  6.93.
''')
f = "    %-35s   %s"
conv = 0.1442   # Converts Btu*in/ft^2*hr*degF to W/m*K.
for i in k:
    if len(i) == 1:
        out(" ", i[0])
    else:
        s, k = i
        out(f % (s, sig(k*conv)))
