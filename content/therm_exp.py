'''
This script sorts the thermal expansion data in the file 'physics' to show
it ordered by value.  Note that last two entries need to be inserted
manually, as they are ranges.
'''
data = '''
Aluminum,                               23.1       ,69
Brass,                                  19         ,57
Steel (carbon),                         10.8       ,32.4
Concrete,                               12         ,36                
Copper,                                 17         ,51
Diamond,                                1          ,3
Ethanol,                                250        ,750
Gasoline,                               317        ,950
Glass,                                  8.5        ,25.5
Glass (Pyrex),                          3.2        ,
Glass (borosilicate),                   3.3        ,9.9
Gold,                                   14         ,42
Ice,                                    51         , 
Iron,                                   11.8       ,35.4
Lead,                                   29         ,87
Macor,                                  9.3        , 
Magnesium,                              26         ,78
Mercury,                                61         ,182
Molybdenum,                             4.8        ,14.4
Nickel,                                 13         ,39
Oak,                                    54  ,(Perp. to the grain)
Douglas fir,                            27         ,75  (radial)
Douglas fir,                            45         ,75  (tangential)
Douglas fir,                            3.5        ,75  (parallel to grain)
Platinum,                               9          ,27
Polypropylene,                          150        ,450
PVC,                                    52         ,156
Quartz (fused (pure glass)),            0.59       ,1.77
Silicon carbide,                        2.77       ,8.31
Silicon,                                2.56       ,9
Silver,                                 18         ,54
Titanium,                               8.6        ,26
Tungsten,                               4.5        ,13.5
Turpentine,                             90         ,
Water,                                  69         ,207
'''
d = []
for i in data.strip().split("\n"):
    name, l, v = i.split(",")
    d.append([float(l), name, v.strip()])
d = sorted(d)
fmt = "{:39s} {:11s} {}"
for l, name, v in d:
    print(fmt.format(name, str(l), v))
# Add in the two ranges
print('''
Stainless steel                         10-17       30-52
Steel (depends on composition)          11-13       33-39
'''[1:-1])
