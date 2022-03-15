'''

ToDo
    - Print headings and Version data.

'''
if 1:  # Copyright, license
    # These "trigger strings" can be managed with trigger.py
    #∞copyright∞# Copyright (C) 2022 Don Peterson #∞copyright∞#
    #∞contact∞# gmail.com@someonesdad1 #∞contact∞#
    #∞license∞#
    #   Licensed under the Open Software License version 3.0.
    #   See http://opensource.org/licenses/OSL-3.0.
    #∞license∞#
    #∞what∞#
    # Provide math tables using python's math module. 
    #∞what∞#
    #∞test∞# #∞test∞#
    pass
if 1:   # Standard imports
    import sys
    from math import (log, log10, sqrt, pi, sin, cos, tan, factorial, ceil, exp)
    from decimal import Decimal, getcontext
    from io import StringIO
    from pdb import set_trace as xx
if 1:   # Custom imports
    from wrap import dedent
    from columnize import Columnize
    from frange import frange
    from sig import sig
    from primes import Primes
    if 0:
        import debug
        debug.SetDebugger()
if 1:   # Global variables
    nl = "\n"
    title = "*Math*" + nl
    # Set True to use Unicode symbols in output
    uni = True
    d2r = pi/180
    symbols = {
        "theta" : chr(0x03b8),
        "mu" : chr(0x03bc),
        "pi" : chr(0x03c0),
        "sqrt" : chr(0x221a),
        "deg" : chr(0x00b0),
        "degree" : chr(0x00b0),
        "degrees" : chr(0x00b0),
        "e0" : chr(0x2070),
        "e1" : chr(0x00b9),
        "e2" : chr(0x00b2),
        "e3" : chr(0x00b3),
        "e-" : chr(0x207b),
        "^2" : chr(0x00b2),
        "*" : chr(0x00b7),
    }
def rlz(s):
    "Remove leading '0' from string s"
    if s[0] == "0":
        s = s[1:]
    return s
def SectionHeading(title, tag):
    w = 79
    n = w - len(title) - len(tag) - 3
    h = "-"*w + nl
    if n > 0:
        return f"{h}{title}{' '*n}*{tag}*"
    else:
        return f"{h}{title} *{tag}*"
def Mensuration():
    symbols = (
        ("^2", chr(0x00b2)),
        ("pi", chr(0x03c0)),
        ("theta", chr(0x03b8)),
        ("sqrt", chr(0x221a)),
        ("*", chr(0x00b7)),
        ("^3", chr(0x00b3)),
        ("A1", "A" + chr(0x2081)),
        ("A2", "A" + chr(0x2082)),
        #(" ~ ", " " + chr(0x2248) + " "),
        # I commented this out because it looks more like '=' from a
        # distance than '~'.
    )
    def U(s):
        if uni:
            for i in symbols:
                s = s.replace(*i)
        return s
    s = [SectionHeading("Mensuration", "Mensuration"), ""]
    s.append(U(dedent(f'''
    Let
        d = inscribed circle diameter
        D = circumscribed circle diameter
        s = perimeter
        A = area or surface area
        V = volume
        L = arc length
        a, b, c = length of sides
        r = radius of inscribed circle = d/2
        R = radius of circumscribed circle = D/2
        theta = angle
        n = number of sides
        h = height
     
    Regular hexagon
        d = distance across flats
        D = distance across points
        A = sqrt(3)/2*d^2
        a = length of side = D/2 = d/sqrt(3)
        D = 2*a = 2*(length of side) = 2*d/sqrt(3)
        s = 6*a = 6*d/sqrt(3)
     
    Regular polygon
        K = pi/n
        a = length of side = d*tan(K) = D*sin(K)
        r = sqrt(R^2 - a^2/4) = a*cot(K)/2 = R*cos(K)
        R = sqrt(r^2 + a^2/4) = a*csc(K)/2 = r*sec(K)
        A = n*a*r/2 = n*a/2*sqrt((D^2 - a^2)/4)
          = n*a^2*cot(K)/4 = n*r^2*tan(K) = n*R^2*sin(2*K)/2
        s = 2*sqrt(R^2 - r^2) = d*tan(theta/2)
     
      d = inscribed circle diameter, D = circumscribed circle diameter, A = area,
      s = perimeter, a = length of one side, T = angle subtended by side
     
     n  T(deg)   A/d^2   A/D^2   A/a^2    d/a     D/a     a/d     a/D     D/d
     3   120.0   1.299   .3248   .4330   .1443   .2887   6.928   3.464   2.000
     4   90.00   1.000   .5000   1.000   .2500   .3536   4.000   2.828   1.414
     5   72.00   .9082   .5944   1.720   .3441   .4253   2.906   2.351   1.236
     6   60.00   .8660   .6495   2.598   .4330   .5000   2.309   2.000   1.155
     7   51.43   .8428   .6841   3.634   .5191   .5762   1.926   1.736   1.110
     8   45.00   .8284   .7071   4.828   .6036   .6533   1.657   1.531   1.082
     9   40.00   .8189   .7231   6.182   .6869   .7310   1.456   1.368   1.064
    10   36.00   .8123   .7347   7.694   .7694   .8090   1.300   1.236   1.051
    12   30.00   .8038   .7500   11.20   .9330   .9659   1.072   1.035   1.035
    15   24.00   .7971   .7626   17.64   1.176   1.202   .8502   .8316   1.022
    16   22.50   .7956   .7654   20.11   1.257   1.281   .7956   .7804   1.020
    20   18.00   .7919   .7725   31.57   1.578   1.598   .6335   .6257   1.012
    24   15.00   .7899   .7765   45.57   1.899   1.915   .5266   .5221   1.009
    32   11.25   .7879   .7804   81.23   2.538   2.551   .3940   .3921   1.005
    48   7.500   .7865   .7832   183.1   3.814   3.822   .2622   .2616   1.002
    60   6.000   .7861   .7840   286.2   4.770   4.777   .2096   .2093   1.001
    64   5.625   .7860   .7841   325.7   5.089   5.095   .1965   .1963   1.001
     
    Parallelogram
        A = a*b
        s = 2*(a + b)
     
    Trapezoid
        Sides a and b are perpendicular to the height direction
        A = (a+b)*h/2
     
    Circular sector (Pie slice)
        L = pi*theta = 2*A/r
        A = r*L/2 = 0.008727*theta*r^2
     
    Circular segment (circle with an intersecting chord)
        h = height = r - 1/2*sqrt(4*r^2 - c^2) = r*[1 - cos(theta/2)]
        c = width = 2*sqrt(h*(2*r - h))
        r = (c^2 + 4*h^2)/(8*h)
        A = 1/2*[r*l - c*(r - h)]
     
    Ellipse
        a = major diameter
        b = minor diameter
        A = pi*a*b
        s ~ pi*sqrt(2*(a^2 + b^2))                   (approximation)
        s ~ pi*sqrt(2*(a^2 + b^2) - (a - b)^2/2.2)   (Better approximation)
        s = 4*a*E(k), k = sqrt(a^2 - b^2)/a,
            E is the complete elliptic integral of the second kind
     
    Cube
        a = length of side
        A = 6*a^2
        V = a^3
        s = 4*a
     
    Pyramid
        h = height
        V = 1/3*h*(area of base)
     
        If base is a regular polygon of n sides and a = length of side,
        r = radius of inscribed circle, and R = radius of circumscribed
        circle, then
            V = n*a*r*h/6 = n*a*h/6*sqrt(R^2 - a^2/4)
     
    Frustum of pyramid (pyramid with top chopped off)
        A1 = area of top
        A2 = area of base
        h = height
        V = h/3*(A1 + A2 + sqrt(A1*A2))
     
    Cone
        A = area of conical surface
        h = height
        s = slant height
        V = pi*r^2*h/3
        A = pi*r*sqrt(r^2 + h^2)
     
    Frustum of cone (cone with top chopped off)
        A = area of conical surface
        r = radius of top
        R = radius of bottom
        S = slant height = sqrt((R - r)^2 + h^2)
        A = pi*S*(R + r)
        V = 1.0472*h*(R^2 + R*r + r^2)
     
    Sphere
        d = 2*r
        A = 4*pi*r^2 = pi*d^2
        V = 4/3*pi*r^3 = pi*d^3/6
     
    Spherical sector (analogous to circular sector)
        r = radius of sphere
        c = diameter of cone's base = 2*sqrt(h*(2*r - h))
        h = height from cone's base to spherical surface
        A = total area of conical and spherical surface
          = pi*r*(2*h + c/2)
        V = 2/3*pi*r^2*h
     
    Spherical cap (analogous to circular segment)
        r = radius of sphere
        c = diameter of cutting circle = 2*sqrt(h*(2*r - h))
        r = (c^2 + 4*h^2)/(8*h)
        A = 2*pi*r*h = pi*(c^2/4 + h^2)
        V = pi*h^2*(r - h/3) = pi*h*(c^2/8 + h^2/6)
     
    Ellipsoid
        a, b, c are the three diameters
        V = 4/3*pi*a*b*c
     
    Paraboloid
        h = height
        d = diameter at height
        p = d^2/(8*h)
        A = 2/3*pi/p*(sqrt((d^2/4 + p^2)^3) - p^3)
        V = 1/2*pi*r^2*h
     
    Torus
        d = diameter of ring = 2*r
        r = radius of ring = d/2
        R = radius from center to centerline of ring
        D = diameter of centerline of ring
        A = 4*pi^2*R*r = pi^2*D*d
        V = 2*pi^2*R*r^2 = pi^2/4*D*d
     
    Barrel (approximate formulas)
        D = major diameter
        d = diameter of ends
        h = height
     
        If the sides are bent to the arc of a circle:
            V ~ 1/12*pi*h*(2*D^2 + d^2)
     
        If the sides are bent to the arc of a parabola:
            V ~ 0.209*h*(2*D^2 + D*d + 3/4*d^2)
     
    Prismoidal Formula
        This is a general formula by which the volume of any prism, pyramid,
        or frustum of a pyramid may be found.
     
        A1 = area of one end of the body
        A2 = area of the other end of the body
        Am = area of a middle section between the two end surfaces
        h  = height of body
        V = h/6*(A1 + 4*Am + A2)
     
    Area of revolution
        Let a collinear curve AB be rotated around an axis CD; the curve
        does not intersect the axis and AB and CD are coplanar.  The
        surface area of the surface of revolution is the length of AB
        multiplied by the arc length of the path of the center of gravity 
        of AB.
     
    Solid of revolution
        If a collinear set of points make up a surface S that does not 
        intersect the rotation axis A (A and S are coplanar), the volume
        of the generated solid body is the area of S multiplied by the 
        arc length of the path of the center of gravity of S.
     
    From Machinery's Handbook, 19th ed.{nl}
    ''')))
    print(nl.join(s))
def TrigRelations():
    s = [SectionHeading("Trig Relations", "Trig_relations"), ""]
    s.append(dedent(f'''
    Sum/Diff formulas
        sin(a+b) = sin(a)*cos(b) + cos(a)*sin(b)
        sin(a-b) = sin(a)*cos(b) - cos(a)*sin(b)
        cos(a+b) = cos(a)*cos(b) - sin(a)*sin(b)
        cos(a-b) = cos(a)*cos(b) + sin(a)*sin(b)
        tan(a+b) = (tan(a)+tan(b))/(1-tan(a)*tan(b))
        tan(a-b) = (tan(a)-tan(b))/(1+tan(a)*tan(b))
     
    Multiple angle formulas
     
        sin(2*a) = 2*sin(a)*cos(a) = 2*tan(a)/(1+tan(a)^2)
        cos(2*a) = cos(a)^2 - sin(a)^2 = 2*cos(a)^2 - 1 = 1 - 2*sin(a)^2
                 = (1-tan(a)^2)/(1+tan(a)^2)
     
        sin(n*a) = 2*sin((n-1)*a)*cos(a) - sin((n-2)*a)
        cos(n*a) = 2*cos((n-1)*a)*cos(a) - cos((n-2)*a)
        tan(n*a) = (tan((n-1)*a) + tan(a))/(1 - tan((n-1)*a)*tan(a))
     
    Half-angle formulas
        sin(a/2) = +-sqrt((1-cos(a))/2)
        cos(a/2) = +-sqrt((1+cos(a))/2)
        tan(a/2) = +-sqrt((1-cos(a))/(1+cos(a))) = (1-cos(a))/sin(a) 
                 = sin(a)/(1+cos(a))
     
    Hyperbolic relationships
        cos(i*x)  = cosh(x)
        sin(i*x)  = i*sinh(x)
        cosh(i*x) = cos(x)
        sinh(i*x) = i*sin(x)
     
    Let A, B, C be the angles of a triangle and a, b, c the corresponding
    opposite sides, and s = (a+b+c)/2.
     
        Radius of inscribed circle = sqrt((s-a)*(s-b)*(s-c)/2)
        Radius of circumscribed circle = a/(2*sin(A))
                                       = b/(2*sin(B))
                                       = c/(2*sin(C))
     
        Law of tangents:
     
            (b-c)/(b+c) = tan((B-C)/2)/tan((B+C)/2)
            (c-a)/(c+a) = tan((C-A)/2)/tan((C+A)/2)
            (a-b)/(a+b) = tan((A-B)/2)/tan((A+B)/2){nl}
    '''))
    print(nl.join(s))
def MathConstants():
    if 0:
        # Replace with Unicode symbols (need to get working; must change
        # the table below so the first column uses the same amount of space
        # for the Unicode symbols).
        def S(s):
            for i in ("pi", "sqrt", "degrees", "^2"):
                if i in s and uni:
                    s = s.replace(i, symbols[i])
            return s
        fmt = "{0:<20s} {1:>16.10f} {2:>16.10f}"
        print(fmt.format(S("pi"), pi, log10(pi)))
        print(fmt.format(S("2*pi"), 2*pi, log10(2*pi)))
        print(fmt.format(S("3*pi"), 3*pi, log10(3*pi)))
        print(fmt.format(S("4*pi"), 4*pi, log10(4*pi)))
        print(fmt.format(S("pi^2"), pi**2, log10(pi**2)))
        print(fmt.format(S("sqrt(pi)"), pi**0.5, log10(pi*0.5)))
        print(fmt.format(S("x"*20), pi**0.5, log10(pi*0.5)))
        print("1234567890"*5)
        f = "{0:>20s}"
        print(len(f.format(S("ssrt(si)"))))
        print(len(f.format(S("sqrt(pi)"))))
        exit()
    s = [SectionHeading("Math Constants", "Constants"), ""]
    s.append(dedent(f'''
    Constant              Number        log10(Number)
    --------------    --------------   --------------
    pi                  3.1415926536     0.4971498727
    2*pi                6.2831853072     0.7981798684
    3*pi                9.4247779608     0.9742711274
    4*pi               12.5663706144     1.0992098640
    pi^2                9.8696044011     1.0992098640
    sqrt(pi)            1.7724538509     0.2485749363
    e                   2.7182818285     0.4342944819
    log10(e)            0.4342944819    -0.3622156887
    log10(pi)           0.4971498727    -0.3035126675
    ln(pi)              1.1447298858     0.0587030212
    ln(2)               0.6931471806    -0.1591745390
    ln(10)              2.3025850930     0.3622156887
    sqrt(2)             1.4142135624     0.1505149978
    sqrt(3)             1.7320508076     0.2385606274
    sqrt(10)            3.1622776602     0.5000000000
    e^pi               23.1406926328     0.4971498727
    Euler constant      0.5772156649    -0.2386618912
    Golden ratio        1.6180339887     0.2089876402     (1 + sqrt(5))/2
     
    Square degrees on a sphere    = 129600/pi  = 41252.96125
    Square degrees in a steradian = 32400/pi^2 = 3282.80635{nl}
    '''))
    print(nl.join(s))
def Base10Logs():
    s = [SectionHeading("4 Place base 10 logarithms", "Base_10_logs"), ""]
    print(nl.join(s))
    indent, places, spc = " "*3, 4, " "*4
    def Header():
        print(" "*64, "PP")
        print(indent, " "*0, sep="", end="")
        fmt = "{{0:^{0}d}} ".format(places)
        for i in range(10):
            s = fmt.format(i)
            if i == 9:
                s = s.rstrip()
            print(s, end="")
        print(" "*2, end="")
        for i in range(1, 10):
            print("{0:3d}".format(i), end="")
        print()
    fmt = "{{0:0{0}d}} ".format(places)
    Header()
    for i in range(10, 100):
        print("{0:2d} ".format(i), end="")
        row, pp = [], []
        for j in range(10):
            x = int(10**places*log10(i/10 + j/100) + 0.5)
            row.append(fmt.format(x))
        for j in range(1, 10):
            diff = int(row[j]) - int(row[j - 1])
            pp.append("{0:3d}".format(diff))
        row[-1] = row[-1].rstrip()
        row.extend(pp)
        print(''.join(row))
        if i in set((29, 49, 69, 89)):
            print()
            Header()
def Base10Antilogs():
    s = [SectionHeading("4 Place base 10 antilogarithms", "Base_10_antilogs"), ""]
    print(nl.join(s))
    indent, places, spc = " "*3, 4, " "*4
    def Header():
        print(indent, " "*1, sep="", end="")
        fmt = "{{0:^{0}d}}  ".format(places)
        for i in range(10):
            print(fmt.format(i), end="")
            if i == 4:
                print(spc, end="")
        print()
    fmt = "{{0:0{0}d}}  ".format(places)
    Header()
    for i in range(100):
        print("{0:2d}  ".format(i), end="")
        for j in range(10):
            x = i/100 + j/1000
            y = int(10**(places + x - 1) + 0.5)
            print(fmt.format(y), end="")
            if j == 4:
                print(spc, end="")
        print()
        if i > 1 and not ((i + 1) % 20) and i != 99:
            print()
            Header()
def TrigFunctions():
    def f(x, width=0):  # Format to 4 places, no leading 0
        s = "{0:.4f}".format(x)
        if s[0] == "0":
            s = s[1:]
        while len(s) < width:
            s = " " + s
        return s
    s = [SectionHeading("Trigonometric Functions", "TrigFunctions"), ""]
    print(nl.join(s))
    print(dedent('''
    Rad     Deg     Sine      Cosine    Tangent   Cotangent
    -----   ---    ------     ------    -------   ---------  ---   ------
    '''))
    for deg in range(46):
        x = deg*pi/180
        print(f(x, 0), end="   ")
        print("{0:3d}".format(deg), end="     ")
        print(f(sin(x)), end="     ")
        print(f(cos(x), 6), end="     ")
        print(f(tan(x), 6), end="     ")
        if deg == 0:
            print("  inf", end="    ")
        else:
            print(f(1/tan(x), 7), end="  ")
        print("{0:3d}".format(90 - deg), end="   ")
        print(f(pi/2 - x, 6), end="     ")
        print()
    print(dedent(f'''
    ------  ---    ------     ------    -------   ---------  ---   ------
                   Cosine      Sine    Cotangent   Tangent   Deg     Rad{nl}
    '''))
def NaturalLogarithms():
    def f(x):
        fmt, end = "{0:10.6f}", " "*4
        if x < 0:
            i = abs(int(x)) + 1
            end = " - {0}".format(i)
            while len(end) < 5:
                end += " "
            x += i
        return fmt.format(x) + end
    def Mult(a, b, indent=""):
        r = []
        for i in range(a, b):
            r.append("{0: 3d} {1:12s}".format(i, f(log(10**i))))
        for i in Columnize(r):
            print(indent, i, sep="")
        print()
    def Header():
        print(" "*5, end="")
        for i in range(10):
            s = "{0:.2f}".format(i/100)[1:]
            if not i:
                s = " "*1 + s
            print("{0:^7s}".format(s), end="")
        print()
    def PrintRow(row):
        digit = int(row[0])
        fmt1 = "{0:7.5f}"
        fmt2 = "{0}{1:5s} "
        print(fmt1.format(row[0]), end="")
        for item in row[1:]:
            s = fmt1.format(item)
            first = int(item)
            t = s[2:]
            c = " " if first == digit else "*"
            print(fmt2.format(c, t), end="")
        print()
    s = [SectionHeading("Natural Logarithms", "NaturalLogs"), ""]
    s.append(f'''
                            Multiples of ln(10){nl}''')
    print(nl.join(s))
    Mult(-50, 0, indent=" "*3)
    Mult(1, 51, indent=" "*2)
    print(" "*22, "Natural logs of 1.00 - 9.99", nl)
    Header()
    for i in range(10, 100):
        print("{0:3.1f}  ".format(i/10), end="")
        row = []
        for j in range(10):
            x = i/10 + j/100
            row.append(log(x))
        PrintRow(row)
        if i > 10 and not ((i + 1) % 10) and i != 99:
            print()
        if i > 10 and not ((i + 1)//10 % 2) and not ((i + 1) % 10) and i != 99:
            Header()
    print(dedent(f'''
    Example:  calculate the natural logarithm of Avogadro's constant, 6.022e23.
     
        The natural log of 1e23 is 52.959457.  Reading down the table to the row
        6.0, we get 
            ln(6.02) = 1.79509
            ln(6.03) = 1.79675
        The difference between the last three digits is 166; we multiply by 0.2 to
        get 33.2.  Thus, to linearly interpolate to the answer, calculate
            1.79509 + 0.000332 = 1.795422
        Add this to 52.959457 to get 54.754879.  Results:
            Calculated = 54.754879
            Actual     = 54.754877
        so we're within about 2 parts out of 5e7.{nl}
    '''))
def StirlingsFormula():
    s = [SectionHeading("Stirling's formula", "StirlingsFormula"), ""]
    s.append(f'''
                        n!
      lim       ------------------- = sqrt(2*pi)
    n -> inf    n^n*exp(-n)*sqrt(n){nl}''')
    print(nl.join(s))
def Factorials():
    s = [SectionHeading("Factorials", "Factorials"), ""]
    s.append(dedent('''
     n  log10(n!)                   n!
    --- ---------  ----------------------------------------'''))
    print(nl.join(s))
    for n in range(2, 51):
        f = factorial(n)
        print("{0:3d}  {1:8.5f}  {2:d}".format(n, log10(f), f))
    print()
def SumOfIntegerPowers():
    s = [SectionHeading("Sum of Integer Powers", "Sum_of_Integer_Powers"), ""]
    s.append(dedent(r'''
                                    n
                                  ------
                                  \
                                   \        m
                                   /       k
                                  /
                                  ------
                                   k = 1
     
      m -->     1       2         3           4             5               6                 7                   8                     9                      10
     n
      1         1       1         1           1             1               1                 1                   1                     1                       1
      2         3       5         9          17            33              65               129                 257                   513                    1025
      3         6      14        36          98           276             794              2316                6818                 20196                   60074
      4        10      30       100         354          1300            4890             18700               72354                282340                 1108650
      5        15      55       225         979          4425           20515             96825              462979               2235465                10874275
      6        21      91       441        2275         12201           67171            376761             2142595              12313161                71340451
      7        28     140       784        4676         29008          184820           1200304             7907396              52666768               353815700
      8        36     204      1296        8772         61776          446964           3297456            24684612             186884496              1427557524
      9        45     285      2025       15333        120825          978405           8080425            67731333             574304985              4914341925
     10        55     385      3025       25333        220825         1978405          18080425           167731333            1574304985             14914341925
     11        66     506      4356       39974        381876         3749966          37567596           382090214            3932252676             40851766526
     12        78     650      6084       60710        630708         6735950          73399404           812071910            9092033028            102769130750
     13        91     819      8281       89271       1002001        11562759         136147921          1627802631           19696532401            240627622599
     14       105    1015     11025      127687       1539825        19092295         241561425          3103591687           40357579185            529882277575
     15       120    1240     14400      178312       2299200        30482920         412420800          5666482312           78800938560           1106532668200
     16       136    1496     18496      243848       3347776        47260136         680856256          9961449608          147520415296           2206044295976
     17       153    1785     23409      327369       4767633        71397705        1091194929         16937207049          266108291793           4222038196425
     18       171    2109     29241      432345       6657201       105409929        1703414961         27957167625          464467582161           7792505423049
     19       190    2470     36100      562666       9133300       152455810        2597286700         44940730666          787155279940          13923571680850
     
      m -->     1       2         3           4             5               6                 7                   8                     9                      10
     n
     20       210    2870     44100      722666      12333300       216455810        3877286700         70540730666         1299155279940          24163571680850
     21       231    3311     53361      917147      16417401       302221931        5678375241        108363590027         2093435326521          40843452659051
     22       253    3795     64009     1151403      21571033       415601835        8172733129        163239463563         3300704544313          67403375450475
     23       276    4324     76176     1431244      28007376       563637724       11577558576        241550448844         5101857205776         108829886664124
     24       300    4900     90000     1763020      35970000       754740700       16164030000        351625763020         7743664746000         172233267629500
     25       325    5525    105625     2153645      45735625       998881325       22267545625        504213653645        11558362011625         267600699270125
     26       351    6201    123201     2610621      57617001      1307797101       30299355801        713040718221        16987865690601         408767794923501
     27       378    6930    142884     3142062      71965908      1695217590       40759709004        995470254702        24613463175588         614658927018150
     28       406    7714    164836     3756718      89176276      2177107894       54252637516       1373272253038        35191919128996         910855693713574
     29       435    8555    189225     4463999     109687425      2771931215       71502513825       1873518665999        49699065104865        1331562927013775
     30       465    9455    216225     5273999     133987425      3500931215       93372513825       2529618665999        69382065104865        1922052927013775
     31       496   10416    246016     6197520     162616576      4388434896      120885127936       3382509703440        95821687265536        2741681213994576
     32       528   11440    278784     7246096     196171008      5462176720      155244866304       4482021331216       131006059354368        3867581120837200
     33       561   12529    314721     8432017     235306401      6753644689      197863309281       5888429949457       177417543756321        5399160106101649
     34       595   13685    354025     9768353     280741825      8298449105      250386659425       7674223854353       238134536522785        7463537860161425
     35       630   14910    396900    11268978     333263700     10136714730      314725956300       9926099244978       316950175194660       10222085213677050
     36       666   16206    443556    12948594     393729876     12313497066      393090120396      12747209152434       418510131863076       13878243653740026
     37       703   17575    494209    14822755     463073833     14879223475      488021997529      16259688606355       548471871658153       18686828026157875
     38       741   19019    549081    16907891     542309001     17890159859      602437580121      20607480744851       713687972921001       24965039874146099
     39       780   20540    608400    19221332     632533200     21408903620      739668586800      25959490005332       922416334079760       33105445959337700
     
      m -->     1       2         3           4             5               6                 7                   8                     9                      10
     n
     40       820   22140    672400    21781332     734933200     25504903620      903508586800      32513090005332      1184560334079760       43591205959337700
     41       861   23821    741321    24607093     850789401     30255007861     1098262860681      40498015234453      1511942268473721       57013865269490101
     42       903   25585    815409    27718789     981480633     35744039605     1328802193929      50180667230869      1918613652323193       74094063391167925
     43       946   27434    894916    31137590    1128489076     42065402654     1600620805036      61868867508470      2421206264260036       95705545704452174
     44       990   29370    980100    34885686    1293405300     49321716510     1919898614700      75917091133686      3039328103769540      122902906642870350
     45      1035   31395   1071225    38986311    1477933425     57625482135     2293568067825      92732216524311      3796008746347665      156953535558885975
     46      1081   33511   1168561    43463767    1683896401     67099779031     2729385725041     112779828756247      4718198909016721      199374283041662551
     47      1128   35720   1272384    48343448    1913241408     77878994360     3236008845504     136591115418008      5837329382119488      251973415277492600
     48      1176   38024   1382976    53651864    2168045376     90109584824     3823077187776     164770395847064      7189934842714176      316898477386037624
     49      1225   40425   1500625    59416665    2450520625    103950872025     4501300260625     198003326416665      8818348440624625      396690743683649625
     50      1275   42925   1625625    65666665    2763020625    119575872025     5282550260625     237065826416665     10771473440624625      494346993683649625
     51      1326   45526   1758276    72431866    3108045876    137172159826     6179960938476     282833770987066     13105638613715076      613389417511262626
     52      1378   48230   1898884    79743482    3488249908    156942769490     7208032641004     336293499518522     15885544497350788      757944523460319650
     53      1431   51039   2047761    87633963    3906445401    179107130619     8382743780841     398553189929883     19185308089152921      932831993825832699
     54      1485   53955   2205225    96137019    4365610425    203902041915     9721668990825     470855151269019     23089614001466265     1143664513090753275
     55      1540   56980   2371600   105287644    4868894800    231582682540    11244104225200     554589089159644     27694980585450640     1396959675209893900
     56      1596   60116   2547216   115122140    5419626576    262423661996    12971199074736     651306400733660     33111150033595536     1700265164306008076
     57      1653   63365   2732409   125678141    6021318633    296720109245    14926096567929     762735557845661     39462611988979593     2062298495762899325
     58      1711   66729   2927521   136994637    6677675401    334788801789    17134080735481     890798639563677     46890270728624521     2493102702662305149
     59      1770   70210   3132900   149111998    7392599700    376969335430    19622732220300    1037629077167998     55553266547279460     3004219455962946550
     
      m -->     1       2         3           4             5               6                 7                   8                     9                      10
     n
     60      1830   73810   3348900   162071998    8170199700    423625335430    22422092220300    1205590677167998     65630962547279460     3608881215962946550
     61      1891   77531   3575881   175917839    9014796001    475145709791    25564835056321    1397297990165279     77325108640113601     4322224127625829151
     62      1953   81375   3814209   190694175    9930928833    531945945375    29086449662529    1615638095750175     90862195186377153     5161523493494169375
     63      2016   85344   4064256   206447136   10923365376    594469447584    33025430301696    1863793876017696    106496009343230976     6146453785375960224
     64      2080   89440   4326400   223224352   11997107200    663188924320    37423476812800    2145268852728352    124510407852712960     7299375289982807200
     65      2145   93665   4601025   241074977   13157397825    738607814945    42325704703425    2463913665618977    145222320690603585     8645649624445697825
     66      2211   98021   4888521   260049713   14409730401    821261764961    47780865404481    2823954271888673    168985000704403521    10213986505356493601
     67      2278  102510   5189284   280200834   15759855508    911720147130    53841577009804    3230021949445314    196191535100698468    12036824309908255050
     68      2346  107134   5503716   301582210   17213789076   1010587629754    60564565828236    3687185189098690    227278635397128036    14150747130065465674
     69      2415  111895   5832225   324249331   18777820425   1118505792835    68010919080825    4200983563527331    262730723232704265    16596941190720225475
     70      2485  116795   6175225   348259331   20458520425   1236154792835    76246349080825    4777463663527331    303084330232704265    19421693680720225475
     71      2556  121836   6533136   373671012   22262749776   1364255076756    85341469239216    5423217194773092    348932830951153296    22676937231730106676
     72      2628  127020   6906384   400544868   24197667408   1503569146260    95372082243504    6145421331081828    400931528765382288    26420843474354594100
     73      2701  132349   7295401   428943109   26270739001   1654903372549   106419480762601    6951881422975909    459803115473650201    30718469304058151749
     74      2775  137825   7700625   458929685   28489745625   1819109862725   118570761035625    7851076163179685    526343526248729625    35642459701414029125
     75      2850  143450   8122500   490570310   30862792500   1997088378350   131919149707500    8852205313570310    601428212528026500    41273811172361294750
     76      2926  149226   8561476   523932486   33398317876   2189788306926   146564344279276    9965240101025286    686018856374604676    47702700104701236126
     77      3003  155155   9018009   559085527   36105102033   2398210687015   162612867546129   11200976392572967    781170550823776113    55029380577287436775
     78      3081  161239   9492561   596100583   38992276401   2623410287719   180178436401041   12571090763256103    888039471737060721    63365156408523636199
     79      3160  167480   9985600   635050664   42069332800   2866497743240   199382345387200   14088199573162664   1007891067719679040    72833432491150483400
     
      m -->     1       2         3           4             5               6                 7                   8                     9                      10
     n
     80      3240  173880  10497600   676010664   45346132800   3128641743240   220353865387200   15765921173162664   1142108795719679040    83570850731150483400
     81      3321  180441  11029041   719057385   48832917201   3411071279721   243230657842161   17618941362014505   1292203431016678161    95728516190207412201
     82      3403  187165  11580409   764269561   52540315633   3715077951145   268159204898929   19663082220669481   1459822981426386193   109473319323803470825
     83      3486  194054  12152196   811727882   56479356276   4042018324514   295295255888556   21915374452808522   1646763236693926596   124989360511009324274
     84      3570  201110  12744900   861515018   60661475700   4393316356130   324804290544300   24394133363891018   1854978985224856260   142479483387607416050
     85      3655  208335  13359025   913715643   65098528825   4770465871755   356861999372425   27119038614281643   2086595931508059385   162166923821679681675
     86      3741  215731  13995081   968416459   69802799001   5175033106891   391654781594121   30111217885347499   2343923348819723001   184297081710482752651
     87      3828  223300  14653584  1025706220   74787008208   5608659307900   429380261081904   33393334600784620   2629467503062752528   209139423129626321500
     88      3916  231044  15335056  1085675756   80064327376   6073063394684   470247820718896   36989679848839916   2945945884891618576   236989520730566533724
     89      4005  238965  16040025  1148417997   85648386825   6570044685645   514479155614425   40926268654541997   3296302288599103785   268171240660532717325
     90      4095  247065  16769025  1214027997   91553286825   7101485685645   562308845614425   45230940754541997   3683722777599103785   303039084670532717325
     91      4186  255346  17522596  1282602958   97793608276   7669354937686   613984947550156   49933466030693518   4111652577728892196   341980696482343462726
     92      4278  263810  18301284  1354242254  104384423508   8275709939030   669769607673804   55065654762069134   4583813941015448868   385419541904706676550
     93      4371  272459  19105641  1429047455  111341307201   8922700122479   729939694734561   60661472858719535   5104225024003936161   433817772622635994799
     94      4465  281295  19936225  1507122351  118680347425   9612569903535   794787454153825   66757162244130351   5677219826232552865   487679284032125964975
     95      4560  290320  20793600  1588572976  126418156800  10347661794160   864621183763200   73391366557020976   6307469235957162240   547552977955963855600
     96      4656  299536  21678336  1673507632  134571883776  11130419583856   939765931574016   80605262346859312   7000003231781642496   614036241555113960176
     97      4753  308945  22591009  1762036913  143159224033  11963391588785  1020564216052129   88442695941236273   7760234290436207713   687778654244606786225
     98      4851  318549  23532201  1854273729  152198432001  12849233969649  1107376769376801   96950326167054129   8593982052566357601   769485934933361475249
     99      4950  328350  24502500  1950333330  161708332500  13790714119050  1200583304167500  106177773111333330   9507499300049998500   859924142434241924250
    100      5050  338350  25502500  2050333330  171708332500  14790714119050  1300583304167500  116177773111333330  10507499300049998500   959924142434241924250
    '''))
    print(nl.join(s))
    print()
def PowersOfTwo():
    s = [SectionHeading("Positive and Negative Powers of 2", "Powers_of_2"), ""]
    s.append(dedent('''
    n      2**n                                       Power of 10'''))
    print(nl.join(s))
    R = range(1, 101)
    for n in R:
        x = 2**n
        s = str(int(log10(x)))
        print("{0:3d}     {1:<38d}          {2:s}".format(n, x, s))
    print(dedent('''
    Example:  2**35 is 34359738368 or 3.4e10.
    '''))
    d = Decimal("2")
    getcontext().prec = 100
    getcontext().capitals = 0
    print(" n     2**(-n)")
    for n in R:
        x = d**(-n)
        s = str(int(log10(x)))
        print("{0:3d}    {1:s}".format(n, str(x)))
def Derivatives():
    s = [SectionHeading("Derivatives", "Derivatives"), ""]
    s.append(dedent('''
    Let D = d/dx, u = u(x), v = v(x).
    Note 1/a*b = (1/a)*b
     
    Function            Derivative
    --------            ----------
     
    log_a u             log_a(e)*u*Du
    ln u                (1/u)*Du
    a^u                 a^u*(ln a)*Du
    u^v                 v*u^(v-1)*Du + ln(u)*u^v*Dv
     
    sin(u)              cos(u)*Du
    cos(u)              -sin(u)*Du
    tan(u)              sec^2(u)*Du
    cot(u)              -csc^2(u)*Du
    sec(u)              sec(u)*tan(u)*Du
    csc(u)              -csc(u)*cot(u)*Du
    vers(u)             sin(u)*Du
     
    asin(u)             Du/sqrt(1 - u^2), abs(asin(u)) <= pi/2
    acos(u)             -Du/sqrt(1 - u^2), 0 <= acos(u) <= pi
    atan(u)             Du/(1 + u^2), abs(atan(u)) <= pi/2
    acot(u)             -Du/(1 + u^2), 0 <= acot(u) <= pi
     
    sinh(u)             cosh(u)*Du
    cosh(u)             sinh(u)*Du
    tanh(u)             sech^2(u)*Du
    coth(u)             csch^2(u)*Du
    sech(u)             sech(u)*tanh(u)*Du
    csch(u)             csch(u)*coth(u)*Du
     
    asinh(u)            Du/sqrt(u^2 + 1)
    acosh(u)            Du/sqrt(u^2 - 1), u > 1, acosh(u) > 0
    atanh(u)            Du/(1 - u^2), u^2 < 1
    acoth(u)            Du/(1 - u^2), u^2 > 1
    asech(u)            -Dx/(u*sqrt(1 - u*u)), 0 < u < 1, asech(u) > 0
    acsch(u)            -Dx/(abs(u)*sqrt(1 + u*u))
    '''))
    print(nl.join(s))
def Integrals():
    s = [SectionHeading("Integrals", "Integrals"), ""]
    s.append(dedent(f'''
    Note 1/a*b = (1/a)*b
     
    Function            Integral
    --------            --------
     
    b^(a*x)             b^(a*x)/(a*ln(b)), b > 0
    ln(x)               x*ln(x) - x
    a^x*log(a)          a^x, a > 0
    1/(a^2 + x^2)       1/a*atan(x/a)
    1/(a^2 - x^2)       1/a*atanh(x/a) = 1/(2*a)*ln((a + x)/(a - x)), a^2 > x^2
    1/(x^2 - a^2)       -1/a*acoth(x/a) = 1/(2*a)*ln((x - a)/(x + a)), x^2 > a^2
    1/sqrt(a^2 - x^2)   asin(x/abs(a)) = -acos(x/abs(a)), a^2 > x^2
    1/sqrt(x^2 + a^2)   ln(x + sqrt(x^2 + a^2))
    1/sqrt(x^2 - a^2)   ln(x + sqrt(x^2 - a^2))
    sqrt(a^2 - x^2)     1/2*(x*sqrt(a^2 - x^2) + a^2*asin(x/abs(a)))
    sqrt(a^2 + x^2)     1/2*(x*A + a^2*ln(x + A)), A = sqrt(a^2 + x^2)
     
    sin(a*x)            -1/a*cos(a*x)
    cos(a*x)            1/a*sin(a*x)
    tan(a*x)            -1/a*ln(cos(a*x)) = 1/a*ln(sec(a*x))
    cot(a*x)            1/a*ln(sin(a*x)) = -1/a*ln(csc(a*x))
    sec(a*x)            1/a*ln(sec(a*x) + tan(a*x)) = 1/a*ln(tan(pi/4 + a*x/2))
    csc(a*x)            1/a*ln(csc(a*x) - cot(a*x)) = 1/a*ln(tan(a*x/2))
     
    sin^2(a*x)          -1/(2*a)*sin(a*x)*cos(a*x) + x/2
    cos^2(a*x)          1/(2*a)*sin(a*x)*cos(a*x) + x/2
    1/sin^2(a*x)        -1/a*cot(a*x)
    1/cos^2(a*x)        1/a*tan(a*x)
     
    sin(m*x)*sin(n*x)   sin((m-n)*x)/(2*(m-n)) - sin((m+n)*x)/(2*(m+n)), m^2 != n^2
    cos(m*x)*cos(n*x)   sin((m-n)*x)/(2*(m-n)) + sin((m+n)*x)/(2*(m+n)), m^2 != n^2
    sin(m*x)*cos(n*x)   cos((m-n)*x)/(2*(m-n)) - cos((m+n)*x)/(2*(m+n)), m^2 != n^2
     
    sin(a*x)*cos(a*x)   1/(2*a)*sin^2(a*x)
    1/sin(a*x)*cos(a*x) 1/a*ln(tan(a*x))
     
    sin(a + b*x)        -1/b*cos(a + b*x)
    cos(a + b*x)        1/b*sin(a + b*x){nl}
    '''))
    print(nl.join(s))
def SquaresSquareRoots():
    def Header(first_line=False):
        s = "                    S = square root, C = cube root"
        t = s if first_line else ""
        print(t)
        if uni:
            # √ ∛ ² ³
            print(dedent('''
               n       n²    √(n)     √(10*n)            n³    ∛(n)     ∛(10*n)   ∛(100*n)
            '''))
        else:
            print(dedent('''
               n     n**2    S(n)     S(10*n)          n**3    C(n)     C(10*n)   C(100*n)
            '''))
    def f(x, width=10, dp=6):
        fmt = "{{0:{0}.{1}f}} ".format(width, dp)
        return fmt.format(x)
    s = [SectionHeading("Squares, SquareRoots, Etc.", "SquaresSquareRoots"), ""]
    print(nl.join(s))
    count, max_integer = 1, 1100
    R = range(1, max_integer + 1)
    Header()
    for i in R:
        if i == 10000:
            print("1e4 ", end="")                       # n
            print("      1e8 ", end="")                 # n**2
            print("      100 ", end="")                 # sqrt(n)
        else:
            print("{0:4d} ".format(i), end="")          # n
            print("{0:8d} ".format(i**2), end="")       # n**2
            print(f(i**(1/2), width=9), end="")         # sqrt(n)
        print(f((10*i)**(1/2), width=10), end="")       # sqrt(10*n)
        if i == 10000:
            print("        1e12 ".format(i**3), end="") # n**3
        else:
            print("{0:12d} ".format(i**3), end="")      # n**3
        print(f(i**(1/3), width=9), end="")             # cbrt(n)
        print(f((10*i)**(1/3)), end="")                 # cbrt(10*n)
        print(f((100*i)**(1/3)))                        # cbrt(100*n)
        if not (count % 25) and count != max_integer:
            Header()
        count += 1
def DegreesAndRadians():
    deg = "°" if uni else " deg"
    s = [SectionHeading("Degrees and Radians", "Degrees_and_radians"), ""]
    s.append(dedent('''
    1 radian = 57.296780{0}, 1{0} = 0.017453292 radians{1}'''.format(deg, nl)))
    print(nl.join(s))
    # Degrees to radians
    print("Degrees to radians:")
    res = []
    for i in range(361):
        res.append("{0:3d}  {1:8.6f}".format(i, i*pi/180))
    for i in Columnize(res):
        print(i)
    print()
    # Radians to degrees
    print("Radians to degrees")
    res = []
    for i in frange(0, 2*pi, 0.02):
        res.append("{0:4.2f}  {1:8.6f}".format(i, i*180/pi))
    for i in Columnize(res):
        print(i)
    print()
    # Minutes and seconds to milliradians
    print("Minutes of arc to milliradians")
    res = []
    for minutes in range(1, 60):
        r = minutes/60*d2r*1000
        res.append("{0:2d}  {1:8.5f}   ".format(minutes, r))
    for i in Columnize(res):
        print(i)
    print()
    print("Seconds of arc to microradians")
    res = []
    for minutes in range(1, 60):
        r = minutes/3600*d2r*10**6
        res.append("{0:2d}  {1:8.5f}   ".format(minutes, r))
    for i in Columnize(res):
        print(i)
    print()
def NumericalConstants():
    s = [SectionHeading("Numerical Constants", "Numerical_Constants"), ""]
    s.append(dedent('''
    a = 1000
    A = sqrt(10*n)
    B = a/sqrt(n)
                                                                            Circle
      n   n^2  a/n    a/n^2  sqrt(n)    A       B    n^(1/3)  pi*n  a*pi/n   Area
    '''))
    print(nl.join(s))
    fmt = "{0:^7s} "
    fmt1 = "{0:^6s} "
    #for n in range(1, 10) + range(95, 101):
    for n in range(1, 101):
        print("{0:3d} ".format(n), end="")                  # n
        print("{0:5d} ".format(n**2), end="")               # n**2
        print(fmt.format(rlz(sig(10**3/n, 5))), end="")     # 1000/n
        print(fmt.format(sig(10**3/n**2, 5)), end="")       # 1000/n**2
        print(fmt.format(sig(n**0.5, 5)), end="")           # sqrt(n)
        print(fmt.format(sig((10*n)**0.5, 5)), end="")      # sqrt(10*n)
        print(fmt.format(sig(1000/(n**0.5), 5)), end="")    # 1000/sqrt(n)
        print(fmt.format(sig(n**(1/3), 5)), end="")         # cube root
        print(fmt1.format(sig(pi*n, 4)), end="")            # pi*n
        print(fmt1.format(sig(1000*pi/n, 4)), end="")       # 1000*pi/n
        print(fmt.format(sig(pi*n**2/4, 5)), end="")        # Circle area
        print()
def ProportionalParts():
    s = [SectionHeading("Proportional Parts", "Proportional_Parts"), ""]
    print(nl.join(s))
    # Header
    for j in range(2):
        if j:
            print(" ", end="")
        print(" N  ", end=" ")
        for i in range(1, 10):
            s = rlz("{0:.1f}".format(i/10))
            print("{0:3s}".format(s), end="")
        print(" ", end="")
    print()
    # Table
    for i in range(50):
        if i and i % 10 == 0:
            print()
        for k in range(2):
            if k:
                print("   ", end="")
            print("{0:3d} ".format(i + 50*k), end="")
            for j in range(1, 10):
                n = int(j/10*(i + 50*k) + 0.5)
                print("{0:3d}".format(n), end="")
        print()
def Fit(x, width):
    '''Using sig(), keep increasing digits until width of sig(x) is equal to
    the desired width.
    '''
    digits = 1
    while len(sig(x, digits)) < width:
        digits += 1
        if digits >= 15:
            break
    fmt = "{{0:^{0}s}}".format(width)
    return fmt.format(sig(x, digits))
def Exponential():
    s = [SectionHeading("Exponential Function (E = exp)", "Exponential"), ""]
    print(nl.join(s))
    def Header():
        print(dedent('''
          x      E(x)       E(10*x)    E(100*x)     E(-x)       E(-10*x)     E(-100*x)
        '''))
    e, width = " "*2, 10
    #for i in range(1, 10) + range(90, 101):
    for x in range(1, 101):
        if x in (1, 20, 40, 60, 80):
            Header()
        print("{0:4.2f}  ".format(x/100), end="")
        print(Fit(exp(x/100), width), end=e)
        print(Fit(exp(x/10), width), end=e)
        print(Fit(exp(x), width + 1), end=e)
        print(Fit(exp(-x/100), width), end=e)
        print(Fit(exp(-x/10), width + 1), end=e)
        print(Fit(exp(-x), width + 1))
def SquareRoots():
    s = [SectionHeading("Square Roots", "SquareRoots"), ""]
    print(nl.join(s))
    def Header(width=7):
        print()
        print(" "*4, end="")
        for i in range(10):
            fmt = "{{0:^{0}s}}".format(width)
            print(fmt.format(str(i)), end="")
        print()
    e, width = " "*1, 10
    #for i in range(0, 10) + range(90, 111):
    for i in range(0, 111):
        if not (i % 20):
            Header()
        print("{0:3d}".format(i), end=e)
        for j in range(10):
            print(Fit(sqrt(10*i + j), 6), end=e)
        print()
def Reciprocals():
    s = [SectionHeading("Reciprocals", "Reciprocals"), ""]
    print(nl.join(s))
    def Header(title, width=7):
        print(nl, title, sep="")
        print(" n    1000/n    "*5)
    def Table(a, b):
        fmt = "{0:3d}"
        Header("{0} to {1}".format(a, b))
        res = []
        for n in range(a, b):
            res.append(fmt.format(n) + " " + Fit(1000/n, 10))
        for i in Columnize(res, columns=5, sep="  "):
            print(i)
    Table(1, 201)
    Table(201, 401)
    Table(401, 601)
    Table(601, 801)
    Table(801, 999)
def ListOfPrimes():
    n = 10000
    s = [SectionHeading("Primes", "Primes"), "",
        "Primes from 1 to {0}".format(n), ""]
    print(nl.join(s))
    for i in Columnize(Primes(n)):
        print(i)
def ShortTables(digits=3):
    R0, R1, R9 = range(10), range(1, 10), range(9)
    s = [SectionHeading("Short Math Tables", "ShortMathTables"), ""]
    print(nl.join(s))
    def Table(title, rows, trailer=None, inc=0):
        print(title)
        print(" "*3, end="")
        fmt = "{{0:^{0}d}}".format(digits)
        for i in R0:
            print(fmt.format(i), end=" ")
        print()
        for i, row in enumerate(rows):
            print("{0:1d} {1:s}".format(i + inc, ''.join(row)))
        if trailer is not None:
            print(trailer)
        print()
    def S(x):
        '''Return the integer x with the indicated number of digits and a
        leading space character.
        '''
        assert digits > 1
        s = str(x)
        assert(len(s) <= digits + 1)
        while len(s) < digits:
            s = "0" + s
        while len(s) < digits + 1:
            s = " " + s
        return s
    def Signif(x):
        '''Convert the number x to a string and return the leading digits
        prepended by a space.
        '''
        s = "{0:.15e}".format(x).partition("e")[0].replace(".", "")
        return " " + s[:digits]
    # Log
    lines = []
    for i in R1:
        row =[]
        for j in R0:
            x = int(10**digits*log10(i + float(j)/10) + 0.5)
            row.append(S(x))
        lines.append(row)
    fmt = "{{:.{:d}g}}".format(min(4, digits))
    s = [
        "ln(10) = " + fmt.format(log(10)),
        "log(pi) = " + fmt.format(log10(pi)),
        "log(e) = " + fmt.format(log10(exp(1)))
    ]
    trailer = ', '.join(s)
    Table("Log 1(.1)10", lines, trailer, inc=1)
    # Antilog
    lines = []
    for i in R0:
        row =[]
        for j in R0:
            t = 10**(digits - 1)*(10**(i/10 + j/float(100)))
            x = int(round(t, 0))
            row.append(S(x))
        lines.append(row)
    Table("Antilog 0(.01)1", lines)
    # Sine
    lines = []
    for i in R9:
        row =[]
        for j in R0:
            theta = 10*i + j
            x = int(round(10**digits*sin(theta*d2r), 0))
            s = S(x)
            if s == str(10**digits):
                s = " "*len(str(10**digits))
            row.append(s)
        lines.append(row)
    Table("Sine 0(1)90 deg", lines)
    # Cosine
    lines = []
    for i in R9:
        row =[]
        for j in R0:
            theta = 10*i + j
            x = int(round(10**digits*cos(theta*d2r), 0))
            s = S(x)
            if s[0] == "1":
                s = " "*(digits + 1)
            row.append(s)
        lines.append(row)
    Table("Cosine 0(1)90 deg", lines)
    # Tangent (radians)
    lines = []
    for i in R1:
        row =[]
        for j in R0:
            theta = i/10 + j/100
            x = int(round(10**digits*tan(theta), 0))
            s = S(x)
            if s[0] == "1":
                s = " " + s[1:]
            row.append(s)
        lines.append(row)
    t = "Add {} for arguments 0.79 and greater".format(10**digits)
    Table("Tangent .1(.01)1 radians", lines, trailer=t, inc=1)
    # Reciprocal
    lines = []
    for i in R1:
        row =[]
        for j in R0:
            x = int(round(10**digits*(1/(i + j/10)), 0))
            s = Signif(x)
            row.append(s)
        lines.append(row)
    Table("Reciprocal (significand)", lines, inc=1)
    # Square
    lines = []
    for i in R1:
        row =[]
        for j in R0:
            x = int(round(10**digits*((i + j/10)**2), 0))
            s = Signif(x)
            row.append(s)
        lines.append(row)
    Table("Square (significand)", lines, inc=1)
    # Square root 1
    lines = []
    for i in R1:
        row =[]
        for j in R0:
            x = int(round(10**digits*((i + j/10)**0.5), 0))
            s = Signif(x)
            row.append(s)
        lines.append(row)
    Table("Square root 1(.1)10", lines, inc=1)
    # Square root 2
    lines = []
    for i in R1:
        row =[]
        for j in R0:
            x = int(round(10**digits*((10*i + j)**0.5), 0))
            s = Signif(x)
            row.append(s)
        lines.append(row)
    Table("Square root 10(1)100", lines, inc=1)
    # Circumference of circle
    lines = []
    for i in R1:
        row =[]
        for j in R0:
            x = int(round(10**digits*(i + j/10)*pi, 0))
            s = Signif(x)
            row.append(s)
        lines.append(row)
    Table("Circumference of circle diam. (significand)", lines, inc=1)
    # Area of circle
    lines = []
    for i in R1:
        row =[]
        for j in R0:
            r = (i + j/10)/2
            A = pi*r**2
            x = int(round(10**digits*A, 0))
            s = Signif(x)
            row.append(s)
        lines.append(row)
    Table("Area of circle diam. (significand)", lines, inc=1)
    # Volume of sphere
    lines = []
    for i in R1:
        row =[]
        for j in R0:
            r = (i + j/10)/2
            V = 4/3*pi*r**3
            x = int(round(10**digits*V, 0))
            s = Signif(x)
            row.append(s)
        lines.append(row)
    Table("Volume of sphere diam. (significand)", lines, inc=1)
    # Degrees to radians
    lines = []
    for i in R9:
        row =[]
        for j in R0:
            deg = 10*i + j
            x = int(round(10**digits*deg*d2r, 0))
            s = S(x if deg <= 57 else (x - 10**digits))
            row.append(s)
        lines.append(row)
    trailer = "Add {} for angles over 57 degrees".format(10**digits)
    Table("Degrees to radians 0(1)90", lines, trailer=trailer)
    # Radians to degrees
    lines = []
    for i in R0:
        row =[]
        for j in R0:
            rad = i/10 + j/100
            x = int(round(10**digits*rad*180/pi, 0))
            s = Signif(x)
            row.append(s)
        lines.append(row)
    Table("Radians to degrees 0(.01)1 (significand)", lines)
    # x/pi
    lines = []
    for i in R1:
        row =[]
        for j in R0:
            x = int(round(10**digits*(i + j/10)/pi, 0))
            s = Signif(x)
            row.append(s)
        lines.append(row)
    Table("x/pi (significand)", lines, inc=1)
    # Cube root 1
    lines = []
    for i in R1:
        row =[]
        for j in R0:
            x = int(round(10**digits*(i + j/10)**(1/3), 0))
            s = Signif(x)
            row.append(s)
        lines.append(row)
    Table("Cube root 1(.1)10", lines, inc=1)
    # Cube root 2
    lines = []
    for i in R1:
        row =[]
        for j in R0:
            x = int(round(10**digits*(10*i + j)**(1/3), 0))
            s = Signif(x)
            row.append(s)
        lines.append(row)
    Table("Cube root 10(1)100", lines, inc=1)
    # Cube root 3
    lines = []
    for i in R1:
        row =[]
        for j in R0:
            x = int(round(10**digits*(100*i + 10*j)**(1/3), 0))
            s = Signif(x)
            row.append(s)
        lines.append(row)
    Table("Cube root 100(1)1000", lines, inc=1)
    # Cube 
    lines = []
    for i in R1:
        row =[]
        for j in R0:
            x = int(round(10**digits*(i + j/10)**3, 0))
            s = Signif(x)
            row.append(s)
        lines.append(row)
    Table("Cube (significand)", lines, inc=1)
if __name__ == "__main__":
    trap = 0
    if trap:
        old = sys.stdout
        stream = StringIO()
        sys.stdout = stream
    Mensuration()
    TrigRelations()
    Derivatives()
    Integrals()
    MathConstants()
    NumericalConstants()
    StirlingsFormula()
    Base10Logs()
    Base10Antilogs()
    TrigFunctions()
    Exponential()
    NaturalLogarithms()
    StirlingsFormula()
    Factorials()
    SumOfIntegerPowers()
    PowersOfTwo()
    SquaresSquareRoots()
    DegreesAndRadians()
    ProportionalParts()
    ListOfPrimes()
    ShortTables(4)
    if trap:
        tables = stream.getvalue()
        # Now combine with headings
        stream = StringIO()
        sys.stdout = stream
        print(title)
        for i in headings:
            print(i)
        print(tables, end="")
        sys.stdout = old
        # Remove spaces at end of lines
        lines = [i.rstrip() for i in stream.getvalue().split(nl)]
        s = nl.join(lines)
        open("math", "w").write(s)
        if len(sys.argv) > 1:
            print(stream.getvalue(), end="")
# vi: wm=1
