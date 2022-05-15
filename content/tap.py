'''
Tap drill sizes calculated as OD - 1/pitch
'''
from color import TRM as t
from wrap import dedent
from f import flt
import sys
from dpdb import set_trace as xx 
from get import GetTextLines
if len(sys.argv) > 1:
    import debug
    debug.SetDebugger()
ii = isinstance
inch = '''
    iCn0-72
    iCn1-64
    iCn2-56
    iCn3-48
    iCn4-40
    iCn5-40
    iCn6-32
    iCn8-32
    iCn10-24
    iCn12-24
    iC1/4-20
    iC5/16-18
    iC3/8-16
    iC7/16-14
    iC1/2-13
    iC9/16-12
    iC5/8-11
    iC3/4-10
    iC7/8-9
    iC1-8

    iFn0-80
    iFn1-72
    iFn2-64
    iFn3-56
    iFn4-48
    iFn5-44
    iFn6-40
    iFn8-36
    iFn10-32
    iFn12-28
    iF1/4-28
    iF5/16-24
    iF3/8-24
    iF7/16-20
    iF1/2-20
    iF9/16-18
    iF5/8-18
    iF3/4-16
    iF7/8-14
    iF1-12
'''
metric = '''
    mC1.6-.35
    mC2-.4
    mC2.5-.45
    mC3-.5
    mC3.5-.4
    mC4-.7
    mC4.5-.75
    mC5-.8
    mC6-1
    mC7-1
    mC8-1.25
    mC10-1.5
    mC12-1.75
    mC14-2
    mC16-2
    mC18-2.5
    mC20-2.5
    mC22-2.5
    mC24-3

    mF1.6-.2
    mF2-.25
    mF2.5-.35
    mF3-.35
    mF3.5-.35
    mF4-.5
    mF4.5-.5
    mF5-.5
    mF6-.75
    mF7-.75
    mF8-1
    mF10-1.25
    mF12-1.25
    mF14-1.5
    mF16-1.5
    mF18-1.5
    mF20-1.5
    mF22-1.5
    mF24-2
'''


def InterpretSize(s):
    'Return (t, dia, tpi_or_pitch, C_or_F) where t is "i" or "M"'
    t = s[0]
    series = s[-1]
    dia, p = s[1:-1].split("-")
    return (t, dia, p, series)
if 0:
    def GetData():
        sizes = '''
            in0-80F in1-64C in1-72F in2-56C in2-64F in3-48C in3-56F in4-40C
            in4-48F in5-40C in5-44F in6-32C in6-40F in8-32C in8-36F in10-24C
            in10-32F in12-24C in12-28F

            i1/4-28F i1/4-20C i5/16-18C i5/16-24F i3/8-16C i3/8-24F i7/16-14C
            i7/16-20F i1/2-13C i1/2-20F i9/16-12C i9/16-18F i5/8-11C i5/8-18F
            i3/4-10C i3/4-16F i7/8-9C i7/8-14F i1-8C i1-12F
    
            M1.6-.35C M1.6-.2F M2-.4C M2-.25F M2.5-.45C M2.5-.35F M3-.5C M3-.35F
            M3.5-.4C M3.5-.35F M4-.7C M4-.5F M4.5-.75C M4.5-.5F M5-.8C M5-.5F M6-1C
            M6-.75F M7-1C M7-.75F M8-1.25C M8-1F M10-1.5C M10-1.25F M12-1.75C
            M12-1.25F M14-2C M14-1.5F M16-2C M16-1.5F M18-2.5C M18-1.5F M20-2.5C
            M20-1.5F M22-2.5C M22-1.5F M24-3C M24-2F
        '''
        i, m = [], []
        for s in sizes.split():
            u = InterpretSize(s)
            _, dia, p, series = u
            if _ == "i":
                if "/" in dia:
                    d = eval(dia)
                else:
                    d = NumSize(dia)
                dia = dia[1:] if dia[0] == "n" else dia
                sz = f"{dia}-{p}"
                tpi = int(p)
                cf = series
                i.append((sz, d, tpi, cf))
            else:
                sz = f"{dia}-{p}"
                d = flt(dia)
                p = flt(p)
                cf = series
                m.append((sz, d, p, cf))
        m.append((0, 0, 0, ""))
        out = []
        for j in zip(i, m):
            out.append(j)
        return out
    def f(x):
        'Inch fmt with no leading 0'
        s = f"{x:.3f}"
        return s[1:] if s[0] == "0" else s
    def Report():
        t.fine = t("wht")
        t.coarse = t("yell")
        t.metric = t("royl")
        t.inch = t("whtl")
        print(f"Tap Drills in inches")
        print(f"Coarse threads")
        for i, m in GetData():
            print(i, m)
            if 0:
                # Inch
                sz, d, tpi, cf = i
                if cf == "F":
                    continue
                td = flt(d - 1/tpi)
                print(f"{sz:8s} {f(td):>5s} {f(d):>5s}", end="   ")
                # Metric
                sz, d, p, cf = m
                if cf == "F":
                    continue
                td = flt(d - 1/p)/25.4
                d = d/25.4
                print(f"{sz:8s} {f(td):>5s} {f(d):>5s}")

    Report()
def IF(x):
    'Inch format with no leading 0'
    return rlz(f"{x:.3f}")
def rlz(s):
    'Remove the leading zero of a string or flt'
    t = s if ii(s, str) else f"{s!s}"
    return t[1:] if t[0] == "0" else t
def Metric():
    def Conv(s):
        '''s is e.g. 'mC1.6-.35'.  Remove the first two letters and convert
        the diameter and pitch to flts.
        '''
        d, p = s[2:].split("-")
        return flt(d), flt(p)
    # Put into coarse and fine containers
    c, f = [], []
    for line in GetTextLines(metric):
        if "C" in line:
            c.append(line)
        else:
            f.append(line)
    d = zip(c, f)
    print(dedent(f'''
        {t("royl")}Metric Threads:  tap drill diameters in inches{t.n}
                      Coarse                  Fine
          Nom Dia  Pitch  TapDrill        Pitch  TapDrill
        '''))
    s = lambda n: " "*n
    for c, f in d:
        # Coarse
        dc, pc = Conv(c)
        # Fine
        df, pf = Conv(f)
        assert dc == df
        tdc = IF((dc - pc)/25.4)
        tdf = IF((df - pf)/25.4)
        print(
                # Nominal dia in mm
                f"{s(4)}{dc!s:^3s}"
                # Coarse pitch
                f"{s(5)}{rlz(pc)!s:^4s}"
                # Coarse tap drill
                f"{s(4)}{tdc:5s}"
                # Fine pitch
                f"{s(10)}{rlz(pf)!s:^4s}"
                # Fine tap drill
                f"{s(4)}{tdf:5s}"
              )
        #print(dc, pc, df, pf)
def NumSize(n):
    '''n is a string.  If it starts with 'n', then it's a number size, so
    convert it to a diameter in inches.  Otherwise, just convert the string
    to a flt.
    '''
    if n.startswith("n"):
        return flt((60 + 13*int(n[1:]))/1000)
    else:
        if "/" in n:
            return flt(eval(n))
        return flt(n)
def Inch():
    def Conv(s):
        '''s is e.g. 'iCn0-72'.  Remove the first two letters and convert
        the diameter and tpi to flts.
        '''
        d, p = s[2:].split("-")
        # Note p is tpi, not pitch
        return NumSize(d), flt(p)
    # Put into coarse and fine containers
    c, f = [], []
    for line in GetTextLines(inch):
        if "C" in line:
            c.append(line)
        else:
            f.append(line)
    d = zip(c, f)
    print(dedent(f'''
        {t("yel")}Inch Threads:  tap drill diameters in inches{t.n}
                      Coarse                  Fine
          Nom Dia   tpi   TapDrill         tpi   TapDrill
        '''))
    s = lambda n: " "*n
    for c, f in d:
        # Coarse
        dc, tpic = Conv(c)
        # Fine
        df, tpif = Conv(f)
        if "n" in c:
            sz = c[3:].split("-")[0]
        else:
            sz = c[2:].split("-")[0]
        assert dc == df
        tdc = dc - 1/tpic
        tdf = df - 1/tpif
        print(
                # Nominal size 
                f"{s(3)}{sz!s:^4s}"
                # Coarse tpi
                f"{s(5)}{rlz(tpic)!s:^4s}"
                # Coarse tap drill
                f"{s(4)}{tdc:5.3f}"
                # Fine pitch
                f"{s(10)}{rlz(tpif)!s:^4s}"
                # Fine tap drill
                f"{s(4)}{tdf:5.3f}"
              )
        #print(dc, pc, df, pf)
x = flt(0)
x.rtz = x.rtdp = True
Metric()
Inch()
