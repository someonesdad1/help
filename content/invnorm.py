'''
Create a table of the inverse normal function.
'''
from scipy.stats import norm
import numpy as N
def tlz(s, n=0, ddp=False, total=None, nospace=False, noneg=False):
    '''Trim leading zero
    s is string
    n is number of spaces to prepend
    ddp is delete decimal point
    '''
    def pad(s):
        if total:
            while len(s) < total:
                s = " " + s
        return s
    s = s.strip()
    if noneg:
        if s[0] == "-":
            s = s[1:]
    if s == "-1.#IO":
        return pad(" "*(n-1) + "-inf")
    elif s == "1.#IO":
        return pad(" "*n + "inf")
    if s[0] == "0":
        if nospace:
            s = s[1:]
        else:
            s = " " + s[1:]
    if ddp:
        s = s.replace(".", "")
    if total:
        while len(s) < total:
            s += " "
    return pad(" "*n + s)
def NormCDF():
    print "Normal CDF:"
    print " "*3,
    for i in N.arange(0, 0.1, 0.01):
        print tlz("%.2f" % i, 2),
    print
    for i in N.arange(0, 3.3, 0.1):
        print "%.2f" % i,
        for j in N.arange(0, 0.1, 0.01):
            x = i + j
            print tlz("%.5f" % norm.cdf(x), ddp=True),
        print
    print
def InvNorm():
    eps = 1e-6
    print "Inverse Normal:"
    print " Q",
    for i in N.arange(0, 0.01 + eps, 0.001):
        print tlz("%.3f" % i, 1),
    print
    for i in N.arange(0, 0.5, 0.01):
        print tlz("%.2f" % i, nospace=True),
        for j in N.arange(0, 0.01 + eps, 0.001):
            x = i + j
            print tlz("%.4f" % -norm.ppf(x), total=6, noneg=True),
        print tlz("%.2f" % (0.99 - i), nospace=True)
    print " "*2,
    for i in N.arange(0.01, 0 - eps, -0.001):
        print tlz("%.3f" % i, 1),
    print "  P"
    print
def MiddleNorm():
    # 2*(F(x) - F(0))
    eps = 1e-6
    print "Middle Normal:\n   ",
    for i in N.arange(0, 0.1, 0.01):
        print tlz("%.2f" % i, 2),
    print
    for i in N.arange(0, 3.5 + eps, 0.1):
        print tlz("%.2f" % i),
        for j in N.arange(0, 0.1, 0.01):
            x = i + j
            z = 2*(norm.cdf(x) - 0.5)
            print tlz("%.5f" % z, total=6, noneg=True, ddp=True),
        print
    print
NormCDF()
InvNorm()
MiddleNorm()
