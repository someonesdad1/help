'''
Generate statistical tables
    Each table should give a reference to a printed table where values can
    be checked and outline the calculation method.
 
    Todo
        - To chi-squared PP, add 255 d.f. for assessing the counts in files
          in random bytes.  Also include 0.001 column.  Also include the
          approximation given on pg 41 of Knuth:vol2.  Include an example
          of a chi-squared goodness-of-fit test for a file of random bytes.
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
    # Generate statistical tables for 'statistical' help file
    #∞what∞#
    #∞test∞# #∞test∞#
    pass
if 1:   # Standard imports
    import sys
    from io import StringIO
    import time
    import scipy
    import random
    from scipy.stats import norm, chi2, binom, poisson, t as T, f as F
    from scipy.stats import hypergeom, beta
    from scipy.special import gamma
    from numpy import matrix
    from math import log, log10, sqrt, pi, ceil
    from pdb import set_trace as xx
if 1:   # Custom imports
    from wrap import dedent
    from sig import sig
    from columnize import Columnize
    if 0:
        import debug
        debug.SetDebugger()
if 1:   # Global variables
    nrv = norm()
    sep = "-"*78
    headings = []   # Used for the |xxxxx| headings at start of file
    nl = "\n"
    title = "*Statistics*" + nl
    ds = sys.stdout
    # Convert a range to a list
    RL = lambda k, l, m:  list(range(k, l, m))
    # The following dictionary translates exponents to Unicode characters
    EXP = {
        "0" : "⁰",
        "1" : "¹",
        "2" : "²",
        "3" : "³",
        "4" : "⁴",
        "5" : "⁵",
        "6" : "⁶",
        "7" : "⁷",
        "8" : "⁸",
        "9" : "⁹",
    }
def SectionHeading(name, tag):
    global headings
    headings.append("|{0}|".format(tag))
    return nl + sep + nl + "{0:50s} *{1}*".format(name, tag)
def Versions():
    t = time.strftime("%d %b %Y")
    if t[0] == "0":
        t = t[1:]
    versions = (
        ("Python:", '.'.join([str(i) for i in sys.version_info[:3]])),
        ("scipy:", scipy.__version__),
        ("numpy:", scipy.__numpy_version__),
        ("Date produced:", t),
    )
    fmt = "    %%%ds  %%s" % max([len(i[0]) for i in versions])
    print(dedent('''
 
    The information in this file was computed using a python script
    stats.py.  The versions used were:'''))
    for i in versions:
        print(fmt % i)
    print(dedent('''

    The normal distribution is so frequently used that the following symbols
    are intended unless otherwise stated:
    
        z       Standardized normal PDF argument
        P       Normal distribution PDF
        Q       Normal distribution 1 - P
    '''))
def References():
    s = [SectionHeading("Statistics References", "Statistics_references")]
    s.append(dedent('''

    [as]        M. Abramowitz and I. Stegun, "Handbook of Mathematical Functions",
                Dover, 1965.
    [bl]        A. Bowker and G. Lieberman, "Engineering Statistics", 2nd ed.,
                Prentice-Hall, 1972, ISBN 0132794551.
    [crow]      E. Crow, F. Davis, and M. Maxfield, "Statistics Manual", Dover,
                1960.
    [cunnane]   C. Cunnane, "Unbiased plotting positions -- a review", Journal
                of Hydrology, 37, 205-222, Elsevier.
    [duncan]    A. Duncan, "Quality Control and Industrial Statistics", 4th ed.,
                Irwin, 1974, ISBN 0256015589.
    [gwh]       I. Guttman, S. Wilks, and J. Hunter, "Introductory Engineering
                Statistics", 2nd ed., Wiley, 1971, ISBN 0471337706.
    [gumbel]    E. Gumbel, "Statistical theory of extreme values", NBS, AMS
                33, 1954.
    [ik]        K. Ishikawa, "Guide to Quality Control", Asian Productivity
                Organization, 1976 (2nd revised printing, 1982), ISBN 9283310365.
    [jk1]       N. Johnson and S. Kotz, "Discrete Distributions", Wiley, 1969, ISBN
                0471443603.
    [johnson]   L. Johnson, "The statistical treatment of fatigue data", Elsevier,
                1964.
    [king]      J. King, "Probability charts for decision making", TEAM, revised
                edition, 1981.
    [nelson]    W. Nelson, "Applied life data analysis", Wiley, 1982.
    [ph]        Pearson & Hartley, "Biometrika tables for statisticians", vol. 1,
                Biometrika Trust, 3rd ed. with corrections, 1976, ISBN 0904653102.
    [we]        Western Electric, "Statistical Quality Control Handbook", 2nd ed.,
                1958.
    '''))
    print(nl.join(s))
def Normal():
    NormalCDF()
    NormalQ()
    NormalPP()
    NormalCDFExtreme()
    NormalInverse()
    NormalInverseSmall()
def NormalCDF():
    s = [SectionHeading("Normal CDF for N(0, 1)", "Normal_CDF")]
    s.append("\nDivide table entries by 1e5 to get cumulative probability\n")
    print(nl.join(s))
    def Header():
        s = ["{0:.2f}".format(i/100)[1:] for i in range(10)]
        print("  z   ", '   '.join(s))
    def PositiveCDF():
        Header()
        for z in range(41):
            if z == 21:
                Header()
            print(" {0:.1f}  ".format(z/10), end="")
            for col in range(10):
                f = nrv.cdf(z/10 + col/100)
                s = "{0:6.5f}".format(f)
                print(s[2:], end=" ")
            print()
    def NegativeCDF():
        def Header():
            s = ["{0:.2f}".format(i/100)[1:] for i in range(10)]
            print("  z   ", '   '.join(s))
        Header()
        for z in range(-40, 0):
            if z == -21:
                Header()
            print("-{0:.1f}  ".format(-z/10), end="")
            for col in range(10):
                f = nrv.cdf(z/10 - col/100)
                s = "{0:6.5f}".format(f)
                print(s[2:], end=" ")
            print()
    NegativeCDF()
    print()
    PositiveCDF()
def NormalQ():
    s = [SectionHeading("Normal Q = 1 - cdf for N(0, 1)", "Normal_Q")]
    s.append("\nDivide table entries by 1e5 to get cumulative probability\n")
    print(nl.join(s))
    def Header():
        s = ["{0:.2f}".format(i/100)[1:] for i in range(10)]
        print("  z   ", '   '.join(s))
    def PositiveCDF():
        Header()
        for z in range(41):
            if z == 21:
                Header()
            print(" {0:.1f}  ".format(z/10), end="")
            for col in range(10):
                f = nrv.cdf(z/10 + col/100)
                s = "{0:6.5f}".format(1 - f)
                print(s[2:], end=" ")
            print()
    def ExtremePositiveCDF():
        print(dedent('''
        More detailed data for extreme values: 1350³ means 1.350e-3 and
        258⁴⁶ means 2.58e-46.\n
        '''))
        Header()
        done = False
        for z in range(30, 221):
            if z in range(50, 221, 20):
                Header()
            print(" {0:.1f}  ".format(z/10), end="")
            for col in range(10):
                f = nrv.sf(z/10 + col/100)
                s = "{0:6.3e}".format(f)
                m, e = s.split("e")
                m = int(m.replace(".", ""))
                e = -int(e)
                if e > 99:
                    done = True
                    break
                E = ''.join([EXP[i] for i in str(e)])
                if e > 9:
                    print(''.join((str(m)[:-1], E)), end=" ")
                else:
                    print(''.join((str(m), E)), end=" ")
            print()
            if done:
                break
        print("\nCalculated with scipy.stats.norm().sf() (survivor function)")
    def NegativeCDF():
        def Header():
            s = ["{0:.2f}".format(i/100)[1:] for i in range(10)]
            print("  z   ", '   '.join(s))
        Header()
        for z in range(-40, 0):
            if z == -21:
                Header()
            print("-{0:.1f}  ".format(-z/10), end="")
            for col in range(10):
                f = nrv.cdf(z/10 - col/100)
                s = "{0:6.5f}".format(1 - f)
                print(s[2:], end=" ")
            print()
    if 0:
        NegativeCDF()
        print()
    if 1:
        PositiveCDF()
        print()
        ExtremePositiveCDF()
def NormalPP():
    '''-log10(Q(z)) where Q = 1 - CDF(z).
    '''
    # Uses scipy's percentage point method rv.ppf().
    s = [SectionHeading("Normal CDF Percentage Points", 
        "Normal_PercentagePoints")]
    s.extend(["", "Normal distribution N(0, 1):  P(z) = CDF(z)", ""])
    print(nl.join(s))
    print('       '.join(["P, %       z "]*4))
    results, pp = [], []
    pp.extend((
        ".001", ".002", ".005",
        ".01", ".02", ".05",
        ".1", ".2", ".3", ".4", ".5", ".6", ".7", ".8", ".9"
    ))
    pp.extend(["1", "2", "2.5"])
    pp.extend([str(i) for i in range(3, 98)])
    pp.extend(( "97.5", "98", "99", "99.1", "99.2", "99.3", "99.4", "99.5",
        "99.6", "99.7", "99.8", "99.9", "99.95",
        "99.99", "99.995", "99.999"))
    for P in pp:
        z = nrv.ppf(float(P)/100)
        results.append("{0:6s} {1:8.5f}".format(P, z))
    for i in Columnize(results):
        print(i)
    print(nl, "Extreme percentage points:", nl, sep="")
    print('       '.join(["P, %       z "]*4))
    pp, results = [], []
    for i in ["e{0}".format(i) for i in range(-20, -3)]:
        pp.extend(("1" + i, "2" + i, "5" + i))
    for P in pp:
        z = nrv.ppf(float(P)/100)
        results.append("{0:6s} {1:8.5f}".format(P, z))
    for i in Columnize(results):
        print(i)
    print("\nCalculated using the scipy.stat.norm().ppf() function.")
def NormalAsymptotic(x):
    '''Asymptotic expansion for Q = 1 - CDF for normal distribution.
    Section 26.2.12 on page 932 of Abramowitz & Stegun.  Return the
    base 10 logarithm.  Since x > 36, a quick experiment shows four 
    terms is more than adequate.
    '''
    assert x >= 36
    series = 1 - 1/x**2 + 1*3/x**4 - 1*3*5/x**6
    f = -x*x/2 - log(x) - log(sqrt(2*pi)) + log(series)
    return f/log(10)
def NormalCDFExtreme():
    '''-log10(Q(z)) where Q = 1 - CDF(z).
    '''
    # Uses scipy's survivor method rv.sf(), as this will be more accurate in
    # the extremes than the CDF.
    s = [SectionHeading("Normal CDF Extreme Values", "Normal_CDF_Extreme")]
    s.append("")
    s.extend(["Normal distribution N(0, 1), large z:  Q(z) = 1 - CDF(z)", ""])
    print(nl.join(s))
    print("Base 10 logarithms:", nl)
    print('    '.join([" z    -log10(Q) "]*4))
    results = []
    for z in RL(5, 51, 1) + RL(60, 101, 10) + RL(150, 501, 50):
        if z < 38:
            q = -log10(nrv.sf(z))
        else:
            q = -NormalAsymptotic(z)
        results.append("{0:3d} {1:11.5f}".format(z, q))
    for i in Columnize(results):
        print(i)
    # Same table, but print the natural logarithms
    print()
    print("Natural logarithms:", nl)
    print('    '.join([" z    -ln(Q)    "]*4))
    results = []
    for z in RL(5, 51, 1) + RL(60, 101, 10) + RL(150, 501, 50):
        if z < 38:
            q = -log(nrv.sf(z))
        else:
            q = -NormalAsymptotic(z)*log(10)
        results.append("{0:3d} {1:11.5f}".format(z, q))
    for i in Columnize(results):
        print(i)
    print(dedent('''

    Ref. table 2, p. 117, [ph].  For z < 38, calculated with scipy.stats.norm.sf().
    For z >= 38, calculated with asymptotic expansion 26.2.12 on page 932 of
    Abramowitz & Stegun.'''))
def NormalInverse():
    s = [SectionHeading("Inverse normal CDF:  z(Q)", "Normal_Inverse_CDF")]
    s.extend(["", "Inverse normal z(Q) for N(0, 1):  "
              "Q(z) = 1 - CDF(z)", ""])
    print(nl.join(s))
    s = ["{0:.3f} ".format(i/1e3)[1:] for i in range(10)]
    Q = "  Q    " + '  '.join(s)
    print(Q)
    for q in range(50):
        if q == 25:
            print(nl, Q, sep="")
        x = q/100
        print("{0:.2f}  ".format(x), end="")
        for col in range(10):
            f = nrv.ppf(1 - (x + col/1e3))
            s = "{0:6.4f}".format(f)
            if "inf" in s:
                print(" inf   ", end="")
            else:
                print(s, end=" ")
        print()
    print("Ref. table 4 p. 118 [biometrika].  Calculated with scipy.stats.norm().ppf().")
def NormalInverseSmall():
    s = [SectionHeading("Inverse normal CDF for Small Q", 
        "Normal_Inverse_CDF_small")]
    s.append("")
    s.extend(["Inverse normal z(Q), Q = 1 - CDF(z) for N(0, 1)", ""])
    print(nl.join(s))
    s = ["{0:.4f}".format(i/1e4)[1:] for i in range(10)]
    print("  Q    ", '  '.join(s))
    Q = lambda x: nrv.ppf(1 - x)
    for q in range(20):
        x = q/1e3
        print("{0:.3f}  ".format(x), end="")
        for col in range(10):
            f = Q(x + col/1e4)
            s = "{0:6.4f}".format(f)
            if "inf" in s:
                print(" inf   ", end="")
            else:
                print(s, end=" ")
        print()
    print(dedent('''

    Ref. table 3 p. 117 [biometrika].  Calculated with scipy's percentage point
    function.'''))
def StdDevConfidenceLimits():
    '''Return a table of factors to get a confidence interval for a
    population standard deviation from a sample standard deviation.
    '''
    def B1(alpha, df):
        return sqrt((df)/chi2.ppf(1 - alpha/2, df))
    def B2(alpha, df):
        return sqrt((df)/chi2.ppf(alpha/2, df))
    s = [SectionHeading("Standard Deviation Confidence Interval",
        "StdDevConfidenceLimits")]
    s.append("")
    s.append(dedent('''
    Factors for confidence intervals for a normal distribution's population
    standard deviation when given a sample standard deviation s and sample 
    size n.
    
        df = n - 1 for a single sample size n
        df = n1 + n2 + ... + nk - k for k sample sizes of n1, n2, ...
    '''))
    print(nl.join(s))
    print(" "*11, (' '*18).join([str(i) + "%" for i in (90, 95, 99)]))
    print(" df    ", (' '*10).join(["b1       b2"]*3))
    for df in RL(1, 31, 1) + RL(40, 101, 10):
        print("{0:3d}".format(df), end=" ")
        for value, alpha in (("90%", 0.1), ("95%", 0.05), ("99%", 0.01)):
            b1, b2 = B1(alpha, df), B2(alpha, df)
            s = "{0:8.3f} {1:8.3f}".format(b1, b2)
            print(s, end=" "*4)
        print()
    print(dedent('''
    >100  1/(1 +- 1.645/a)     1/(1 +- 1.960/a)     1/(1 +- 2.576/a)
        where a = 1/sqrt(2*df)
    
            b1 = sqrt((n - 1)/ChiSqPPF(alpha/2, n - 1))
            b2 = sqrt((n - 1)/ChiSqPPF(1 - alpha/2, n - 1))
    
    Ref. table 8 p. 242 [crow].  Calculated with scipy's PPF (percentage point
    function) for the chi-square distribution scipy.stats.chi2.
    
    Example:  a set of 12 measurements has a sample standard deviation of 12.43.
    Calculate a 95% confidence interval for the population standard deviation.
        Entering table with df = 11 under 95% column, we get b1 = 0.748 and 
        b2 = 1.551.  The confidence interval is
            [b1*s, b2*s] = [0.748*s, 1.551*s] = [9.298, 19.279]
    '''))
def ProbabilityPlotting():
    s = [SectionHeading("Probability Plotting",
        "Probability_Plotting")]
    s.append("")
    s.extend([dedent('''
    Probability plotting involves plotting a distribution's CDF against the values
    of a sample of data points.  The CDF is estimated by simple order statistics
    and, on suitable graph paper, the data come from a particular distribution when
    the points fall nearly on a straight line.  Mean and standard deviations are
    easily picked off from the graph.  These graphs are often made by hand for
    small (e.g., 20 or less) samples and tend to be fast and robust.  In
    particular, Weibull distribution fits are often determined this way in e.g.
    reliability engineering.
     
    [king] is the best practical reference, although it's out of print.  The book
    comments that [cunnane] studied different forms of the CDF estimator:
     
      i/(n + 1)               Weibull formula (recommended by [gumbel])
      (i - 0.5)/n             Hazen formula (recommended by [johnson])
      (i + a)/(n + 1 + 2*a)   Cunnane
          where a = 3/8 for normal distribution
                  = 0.44 for type 1 extreme value
                  = 1/2 for type 2 extreme value and Weibull
                  = 0.4 for other non-normal distributions
     
          King's Monte Carlo studies showed that there are no practical
          differences in estimation of the means, but the Weibull formula
          consistently overestimates the standard deviation while the Hazen
          formula underestimates it.  Cunnane's formula gives standard deviation
          estimates that average 1-2% high.
     
        Recommendation:  use Cunnane for computer programs & linear regression
        fits; use the Weibull formula i/(n + 1) for hand plotting because of ease
        of calculation.
    ''')])
    print(nl.join(s))
    print("Comparison of the three different formulas (normal "
          "distribution for Cunnane):")
    print()
    print("         Weibull   Hazen    Cunnane")
    for n in (5, 10, 15):
        print("n =", n)
        for i in range(1, n):
            w = i/(n+1)
            h = (i - 1/2)/n
            c = (i + 3/8)/(n + 1.75)
            print(" "*3, ("{:10.2f}"*3).format(w, h, c))
def BinomialCDF():
    R = range(2, 21)
    Rt1 = [1] + RL(5, 51, 5)
    Rt2 = RL(55, 100, 5) + [99]
    def Header(Rt):
        print(" "*31, "p")
        print(" n  k ", end="")
        for p in Rt:
            print("{0:^6s}".format(str(p) + "%"), end="")
        print()
    def Table(Rt):
        Header(Rt)
        for m in range(n):
            print("{0:2d} {1:2d} ".format(n, m), end="")
            for p in Rt:
                rf = binom(n, p/100)
                s = "{0:05.0f}".format(1e4*rf.cdf(m))
                if s == "10000":
                    s = "     "
                if s[0] == "0":
                    s = " " + s[1:]
                if p == 100:
                    s = "  --"
                print("{0:4s} ".format(s), end="")
            print()
        print()
    s = [SectionHeading("Binomial CDF", "Binomial_CDF")]
    s.append("")
    s.extend([dedent('''
    Binomial cumulative distribution function n = [2, {0}]
        n = sample size
        k = number of items with characteristic, 0 <= k <= n
        p = probability of item having characteristic, 0 <= p <= 1
     
      Table values are the probability P(X <= k; n, p).
    ''').format(max(R))])
    print(nl.join(s))
    for n in R:
        Table(Rt1)
        Table(Rt2)
    print(dedent('''
    Ref. [nelson] pg 588 (tables) and 91 (discussion), [jk1:50].  Values computed
    with scipy.stats.binom().cdf().
     
    Assumptions:
        * Each of the n items in the sample has the same chance of being selected.
        * Each sampling event is statistically independent of the other sampling
          events.
        * If the binomial distribution's assumptions may not be satisfied, it can
          still be used as a reference distribution as a contrast.
     
    The binomial distribution is used to model dichotomous situations where a
    collection of objects has a particular characteristic in a large population of
    N items.  It is appropriate for small samples, where "small" means perhaps n <
    N/10.  The binomial distribution is also used in the situation of sampling with
    replacement.
     
    For sampling without replacement or where n > N/10, use the hypergeometric
    probability distribution.
     
    The probability of getting k units with the characteristic in a sample of n
    units is
        P(k; n, p) = (n!)/((k!)*(n - k)!)*(p**k)*((1 - p)**(n - k))
    The table values above are the sum from 0 to k of P(k; n, p).
     
    The standard deviation of a binomial random variable y = X/n is
        sqrt(y*(1 - y)/n)
     
    The skewness is positive (right tail longer than left) if p < 1/2 and negative
    if p > 1/2; the distribution is symmetric iff p is 1/2.
     
    If x is a binomial random variable with n and p, then
        (x - n*p)/sqrt(n*p*(1 - p))
    tends to the normal distribution as n tends to infinity (Laplace's theorem).
    '''))
def PoissonCDF():
    def Hdr(mus, mup, fmu, musp):
        print(mup)
        print(" m", " "*musp, end="")
        s = [fmu.format(i) for i in mus]
        print(' '.join(s))
    def Put(mus, numlines, rnd, fmt, mup, fmu="{0:^11s}", musp=1):
        Hdr(mus, mup, fmu, musp)
        for m in range(numlines):
            print("{0:2d}  ".format(m), end="")
            for mu in mus:
                rv = poisson(float(mu))
                s = str(round(rv.cdf(m), rnd))
                while len(s) < rnd + 2:  # round bug:  trailing '0' truncated
                    s += "0"
                if s[0] == "1":
                    s = ""
                elif s[0] == "0":
                    s = s[2:]
                print(fmt.format(s), end="")
            print()
        print()
    s = [SectionHeading("Poisson CDF", "Poisson_CDF")]
    s.extend(["", "Poisson cumulative distribution function",
        "  (Higher m values not shown will round to 1 at table precision)",
        ""])
    print(nl.join(s))
    mup = " "*38 + "mu"
    fmt = "{0:^10s}  "
    fmtmu = "{0:^11s}"
    mus = (".001", ".005", ".01", ".015", ".02", ".025")
    Put(mus, 4, 8, fmt, mup, musp=0)
    mus = (".03", ".035", ".04", ".045", ".05", ".055")
    Put(mus, 4, 6, fmt, mup, musp=0)
    mus = (".06", ".065", ".07", ".075", ".08", ".085")
    Put(mus, 4, 6, fmt, mup, musp=0)
    mus = (".09", ".095", ".1", ".2", ".3", ".4")
    Put(mus, 6, 6, fmt, mup, musp=0)
    mus = (".5", ".6", ".7", ".8", ".9", "1")
    Put(mus, 9, 6, fmt, mup, musp=0)
    fmt = "{0:^8s} "
    mus = ("1.2", "1.4", "1.6", "1.8", "2", "2.5", "3", "3.5")
    Put(mus, 13, 4, fmt, mup, fmu="{0:^8s}")
    mus = ("4", "4.5", "5", "6", "7", "8", "9", "10")
    Put(mus, 23, 4, fmt, mup, fmu="{0:^8s}")
    print(dedent('''
    Ref. [nelson:586] and [jk:87].  Values computed with scipy.stats.binom().cdf().
     
    A random variable X is from a Poisson distribution if
     
        P(X == k; mu) = exp(-mu)*mu**k/k!, k = 0, 1, 2, ..., mu > 0
     
    This distribution is the limit of a binomial distribution where n -> infinity,
    p -> 0, but n*p = mu.
     
    Poisson model assumptions:
        * The events occur at a known and average rate (constant over time, space,
          volume, etc.).
        * The modeled events occur independently of each other.
        * The potential number of occurrences of events is essentially unlimited.
     
    Some uses of the Poisson model to model number of:
        * Soldiers in a regiment kicked to death yearly by horses (famous example
          by Bortkiewicz 1898).
        * Defects in a sheet of material.
        * Flaws in a length of wire or computer tape.
        * Failures in a repairable product over a given period.
        * Particles emitted by a radioactive source in a given period of
          time.
        * Telephone calls arriving in a telephone exchange.
        * Mutations in a stretch of DNA after a radiation treatment.
        * Photons arriving at a telescope.
        * Electron fluctuations in conductors (shot noise).
     
    Bortkiewicz noted that events with low frequency in a large population follow
    the Poission distribution even when the probabilities of the events varies.
     
    Given a sample of n measured integer values ki (i = 1, 2, ..., n) from a
    Poisson process, the Poisson parameter mu's maximum likelihood estimate is
     
        mu = sum(ki)/n
     
    Standard devation = sqrt(mu).
     
    Confidence interval for mu:  given an observation k from a Poisson distribution
    with mean mu, the 1 - alpha confidence interval for mu is
     
        1/2*ChiSq(alpha/2; 2*k) <= mu <= 1/2*ChiSq(1 - alpha/2; 2*k + 2)
     
    Poisson process (https://en.wikipedia.org/wiki/Poisson_process):  a continuous
    time counting process {N(t), t >= 0} where
     
        * N(0) = 0
        * The number of occurrences in disjoint intervals are independent of each
          other.
        * The probability distribution of the number of occurrences counted in any
          time interval only depends on the length of the interval.
        * The distribution of N(t) is a Poisson distribution.
        * No counted occurrences are simultaneous.
     
    implies
        * The waiting time distribution until the next occurrence is exponential.
        * Occurrences are distributed uniformly on any interval of time.
        * Time between consecutive events are independent random variables.
        * Number of events in any time interval is independent of the number of
          events in any other disjoint interval.
     
    An inhomogeneous Poisson process is where the mean mu changes in time.  A good
    example is radioactive decay because the total number of source atoms decreases
    over time.
     
    Example:  suppose a critical business process averages 10 events per unit time.
    Further suppose the business requires that 99.9% of the time that its
    infrastructure for dealing with these events must be adequate.  What should be
    the design goal for the throughput of the infrastructure?
     
        From the table, look under the column mu = 10.  The 99.9% cumulative
        probability occurs for between counts of 20 and 21 occurrences.  You'd
        design for 21 occurrences.
    '''))
def ChiSquarePP():
    s = [SectionHeading("Chi-squared Percentage Points", "ChiSquare_PP")]
    t = " "*32 + "alpha"
    R = RL(1, 31, 1) + RL(40, 101, 10) + [200, 255]
    R = RL(1, 31, 1) + [200, 255]
    digits = 4
    s.extend(["", "Table values are x values for which upper tail "
              "areas are equal to alpha.", "df = degrees of freedom.", t])
    print(nl.join(s))
    pp = (".995", ".99", ".975", ".95", ".9", ".75", ".5")
    fmt = "{0:^10s}"
    print(" df ", end="")
    for alpha in pp:
        print(fmt.format(alpha), end="")
    print()
    for df in R:
        print("{0:3d} ".format(df), end="")
        rv = chi2(df)
        for alpha in pp:
            x = rv.ppf(1 - float(alpha))
            print(fmt.format(sig(x, digits)), end="")
        print()
    print()
    print(" "*25, "Lower tail areas")
    print(t)
    pp = (".25", ".1", ".05", ".025", ".01", ".005")
    print(" df ", end="")
    for alpha in pp:
        print(fmt.format(alpha), end="")
    print()
    for df in R:
        print("{0:3d} ".format(df), end="")
        rv = chi2(df)
        for alpha in pp:
            x = rv.ppf(1 - float(alpha))
            print(fmt.format(sig(x, digits)), end="")
        print()
    print()
    print(dedent('''

    Ref. [crow] pg 232.  Values computed with scipy.stats.chi2().ppf().
     
    Example:  [bl:298]  A 100(1 - alpha)% upper one-sided confidence interval
    for a sample standard deviation s from a normal distribution 
    ((n - 1)*(s/alpha)**2 has a chi-square distribution with n - 1 degrees of
    freedom) is
     
        s*sqrt((n - 1)/ChiSq(1 - alpha; n - 1))
     
    Suppose an experiment gave a standard deviation s = 0.196 with n = 25.  For
    99% confidence, the upper bound for the population standard deviation is

        0.196*sqrt(24/ChiSq(0.99, 24)) = 0.196*sqrt(24/10.86) = 0.291

    The two key assumptions needed are that the parent distribution is normal
    and 0he sample was a random sample (each value had an equal chance of being
    drawn).
     
    [as] give an asymptotic expansion for Q (upper tail area) for large df in
    26.4.13:
        
        Q(chi2|df) approx = Q1(x) where x = sqrt(2*chi2) - sqrt(2*df - 1) for
        df > 100 and where Q1 is the normal distribution's upper tail area.
     
        Example:  Suppose we want Q(99.3|100), so chi2 = 99.3 and df = 100.
        Then x = sqrt(2*99.3) - sqrt(199) = -0.014 and Q1(-0.014) is about
        0.5 by inspection; this is confirmed by the above chi-squared table.
     
    Random byte streams
    -------------------
     
      The 255 d.f. line is useful for testing the hypothesis that a sequence of
      bytes came from a true random process.   The chi-squared goodness-of-fit
      statistic is calculated for each byte's frequency by summing the
      following term for each byte: (observed - expected)**2/expected.
      observed is the byte's frequency divided by the total counts and expected
      is 1/256.  This is a sensitive statistic for large files (megabytes).
      Look up the statistic in the table and get the corresponding probability
      P.  My rule of thumb is that if 0.1 <= P <= 0.9, then the sequence is
      likely random.  If P < 0.05 or P > 0.95, it's suspect, so perform a
      repeat test.  If P < 0.01 or P > 0.99, it's very likely not a random
      sequence (for example, English text and program source code files can 
      have chi-squared statistics in the millions).
     
      I've tested the -t and -u output of /pylib/pgm/mkfile pretty well and
      find that they produce good pseudorandom sequences (they must be labeled
      pseudorandom because they are generated by the OS in software).  John
      Walker's ent.exe program is a useful adjunct for testing
      (http://www.fourmilab.ch/random/) because it prints the entropy,
      chi-squared statistic, mean, and the serial correlation coefficient, all
      which help with assessing randomness.  Here's a shell script that shows
      the distribution of the chi-squared statistic produced by
      /pylib/pgm/cnt.py:
     
        echo > results
        for i in $(seq 100); do
            mkfile -t 10M aa
            python cnt.py -r aa |grep 'chi' >>results
        done
     
      which resulted in the sorted data of the chi-squared statistic:
     
        193.51 195.11 211.22 212.04 212.97 214.22 214.55 218.11 219.18 220.92
        221.23 222.93 224.59 225.82 225.92 226.28 227.02 227.04 227.59 227.6
        227.97 228.62 229.24 229.38 229.55 230.07 230.27 230.47 230.58 230.66
        230.84 230.95 231.17 231.98 232.43 232.51 232.94 233.85 233.86 234.42
        235.29 235.7 236.25 236.87 237.3 237.63 237.7 237.93 238.78 239.38
        239.91 240.36 241.06 241.78 242.07 242.41 242.75 242.84 242.93 243.88
        244.08 244.11 244.68 245.07 245.07 245.29 245.49 245.51 245.54 245.72
        245.83 245.94 246.32 246.58 246.68 247.16 247.26 247.89 248.03 248.14
        248.51 248.78 248.88 249.54 249.91 250.34 250.39 250.59 251.19 251.24
        251.25 251.41 252.0 252.31 252.79 252.98 253.31 253.4 253.42 253.58
        253.84 253.91 254.42 254.96 254.99 255.18 255.37 255.98 256.26 256.4
        256.44 256.71 256.79 257.0 257.26 257.76 257.85 258.09 258.62 258.78
        259.58 259.8 259.85 259.88 260.0 260.1 260.22 260.59 260.91 261.1
        261.56 261.67 262.16 262.29 263.02 263.29 263.36 263.65 263.84 264.07
        264.11 264.17 264.18 264.45 264.59 264.83 265.43 265.48 265.7 265.83
        265.9 267.43 268.05 268.69 268.75 269.07 269.1 269.51 269.88 270.27
        270.38 270.54 270.69 271.25 271.78 272.63 273.24 273.38 273.38 273.41
        273.97 274.05 274.3 275.15 275.91 276.39 276.99 277.22 277.49 278.36
        279.17 279.69 280.84 280.94 281.4 281.47 282.11 286.4 287.57 287.79
        288.84 289.72 289.82 291.48 292.46 292.9 293.61 296.94 301.39 331.79
     
      which plots linearly on a normal probability plot except for a few
      outliers.  The statistics on these data are:
    
        Mean         253.5    
        Std dev      20.61    
        Sd/mean      0.08132  
        Count        200      
        Minimum      193.5    
        Maximum      331.8    
        Range        138.3    
        Median       253.7    
        Geom. mean   252.7    
        Skewness     0.09668  
        Kurtosis     0.5776   
    
        Estimated Percentiles (%, value):
            0        193.5    
            5        221.2    
            10       227.9    
            15       230.8    
            20       235.1    
            25       239.8    
            30       244.     
            35       245.8    
            40       248.4    
            45       251.2    
            50       253.7    
            55       256.4    
            60       259.1    
            65       261.3    
            70       264.1    
            75       265.8    
            80       270.3    
            85       273.5    
            90       278.4    
            95       287.8    
            100      331.8    
    
        Outliers (extreme outliers marked by *):
                    193.5    
                    195.1    
                    331.8    
    
      These data are a pretty reasonable reflection of a set of random bytes
      and you get a feel for the variability of the statistics.
    
      Note that the chi-squared statistic doesn't change if the sequence is
      sorted, so other tests like entropy, serial correlation, etc. are needed
      to make a suitable estimate of randomness.  However, always remember that
      a sorted sequence of bytes is equally probable with any other ordering of
      the sequence if the sequence is truly random.  Also realize that the
      number of permutations of a 1 GB sequence of bytes is truly beyond
      astronomical: it's 1e9! which has over 8 billion digits; this is a number
      far beyond human comprehension and experience.
    '''))
def StudentT_PP():
    s = [SectionHeading("t Distribution Percentage Points", "StudentT_PP")]
    t = " "*32 + "P(t)"
    R = RL(1, 31, 1) + [40, 60, 120, "inf"]
    digits = 4
    s.extend(["", "Table values are t values for which upper tail "
              "areas are equal to P(t).", "df = degrees of freedom.", t])
    print(nl.join(s))
    pp = (".4", ".3", ".25", ".2", ".15", ".1", ".05", ".025", ".01", ".005")
    fmt = "{0:^7s}"
    print(" df   ", end="")
    for alpha in pp:
        print(fmt.format(alpha), end="")
    print()
    for df in R:
        if df == "inf":
            print("inf   ", end="")
            df = 10**5
        else:
            print("{0:3d}   ".format(df), end="")
        rv = T(df)
        for P in pp:
            x = rv.ppf(1 - float(P))
            s = sig(x, digits)
            if s[0] == "0":
                s = s[1:]
            print(fmt.format(s), end="")
        print()
    print()
    print(dedent('''

    Ref. [crow] pg 231.  Values computed with scipy.stats.t().ppf().
     
    Confidence interval for mean:  xbar +/- t(alpha/2, n-1)*s/sqrt(n)
     
    t test:  Compute t = (xbar - a)/(s/sqrt(n)).  If |t| > t(alpha/2, n - 1),
    reject the hypothesis that mu = a.
     
    Assumptions:  approximately normal distribution, random sample.
    '''))
def FDistributionPP():
    Rt1 = range(1, 11)
    Rt2 = (12, 15, 20, 25, 30, 35, 40, 50, 60, 120)
    R = RL(1, 31, 1) + [40, 60, 120]
    def Hdr(alpha, numerator_df):
        print(" "*28 + "P(F) = alpha = {0}".format(alpha))
        print(" "*31 + "Numerator df")
        print("dfd    ", end="")
        for i in numerator_df:
            print("{0:^7s}".format(str(i)), end="")
        print()
    def Table(P, Rt, R):
        Hdr(P, Rt)
        for dfd in R:
            print("{0:3d}   ".format(dfd), end="")
            for dfn in Rt:
                rv = F(dfn, dfd)
                x = rv.ppf(1 - float(P))
                s = "{0:.2f}".format(x)
                if dfd == 1:
                    if P in (".01", ".025"):
                        s = "{0:.1f}".format(x)
                if s[0] == "0":
                    s = s[1:]
                print(fmt.format(s), end="")
            print()
        print()
    s = [SectionHeading("F Distribution Percentage Points", "FDistributionPP")]
    s.extend(["",
    "Table values are F values for which upper tail areas are equal to P(F).",
    "df = degrees of freedom, dfd = denominator df column"])
    print(nl.join(s))
    pp = ("0.1", "0.05", "0.025", "0.01")
    fmt = "{0:>7s}"
    print()
    for P in pp:
        Table(P, Rt1, R)
        Table(P, Rt2, R)
    print(dedent('''

    Ref. [crow] pg 234.  Values computed with scipy.stats.f().ppf().
     
    F test for sigma1/sigma2 assumptions [crow:74]:
        * Populations have normal distributions
        * The samples are random samples drawn independently from the two
          populations.
     
    Null hypothesis:  (sigma1/sigma2)**2 is 1 at significance alpha on the basis of
    a sample size of n1 for population 1 and n2 for population 2.
     
    Statistic:  F = (s1/s2)**2 with the larger s in the numerator so the ratio is 1
    or larger.
     
    Equal tails test:  if F > F(df1, df2; alpha/2), reject null hypothesis.  (Yes,
    it's alpha/2 because we forced the upper area by making F >= 1.)
     
    One-sided test:  reject sigma1 <= sigma2 at confidence alpha if 
    F > F(df1, df2; alpha).  Do not reorder the numerator and denominator to make
    the F statistic >= 1.  Rejection means population 1's sigma is greater than
    population 2's.
    '''))
def UniformRandomDeviates():
    def Header(ncols, width):
        print("Row ", end="")
        fmt = "{{0:^{0}}}".format(width)
        print(''.join([fmt.format(i) for i in range(ncols)]))
    nrows, ncols, digits, width = 100, 10, 5, 7
    n = nrows*digits*ncols
    s = [SectionHeading("{0} Uniform Random Deviates".format(n),
         "Uniform_deviates")]
    s.append(dedent('''

    Generated with python's random.random() function, first 5 digits from the
    number are used and the decimal point is stripped off.  Sequence started with
    random.seed(0).  Note these are pseudorandom variates.  Here are the first five
    generated numbers:\n
    '''))
    print(nl.join(s))
    print("      xxxxx")
    random.seed(0)
    for i in range(5):
        print("    {0}".format(repr(random.random())))
    print()
    Header(ncols, width)
    random.seed(0)
    for row in range(nrows):
        print("{0:3d}  ".format(row), end="")
        for col in range(ncols):
            s = "{0:.15f}".format(random.random())[2:digits + 2]
            print("{0:7s}".format(s), end="")
        print()
def NormalRandomDeviates():
    def Header(ncols, width):
        print("Row   ", end="")
        fmt = "{{0:^{0}}}".format(width)
        print(''.join([fmt.format(i) for i in range(ncols)]))
    nrows, ncols, digits, width = 100, 10, 5, 7
    n = nrows*digits*ncols
    s = [SectionHeading("{0} Uniform Random Deviates".format(n),
         "Uniform_deviates")]
    s.append(dedent('''

    Generated with python's random.normalvariate() function.  Sequence started with
    random.seed(0).  Note these are pseudorandom variates.\n
    '''))
    print(nl.join(s))
    Header(ncols, width)
    random.seed(0)
    for row in range(nrows):
        print("{0:3d}  ".format(row), end="")
        for col in range(ncols):
            x = random.normalvariate(0, 1)
            s = "{0:.3f}".format(x)
            print("{0:>7s}".format(s), end="")
        print()
def StatisticsFormulas():
    s = [SectionHeading("Statistics formulas", "Statistics_formulas")]
    s.append(dedent('''

    Probabilities
        P(A and B) = P(A)*P(B|A) = P(B)*P(A|B)
        P(A or B)  = P(A) + P(B) - P(A and B)
     
    Error classification
        alpha:  type 1:  reject a true hypothesis
        beta:   type 2:  accept a false hypothesis
        "Type 3 error":  get the right answer to the wrong problem
        "Type 4 error":  get the wrong answer to the wrong problem
     
    Python forms for statistics calculations:
        Let the n data items be
            d = [x1, x2, ..., xn]
        n = len(d)
        sx = sum(d)
        sxx = sum([i*i for i in d])
        mean = sx/n
        stdev = ((sxx - n*mean**2)/(n - 1))**0.5
        range = [min(d), max(d)]
        Median (must have n > 1):
            A = (n - 1)//2
            median = d[A] if n % 2 else (d[A] + d[A + 1])/2
     
                   sqrt(n)*sum([(x[i] - mean)**3 for i in x])
        Skewness = -------------------------------------------
                   (sum([(x[i] - mean)**2 for i in x]))**(3/2)
     
                    n*sum([(x[i] - mean)**4 for i in x])
        Skewness = ---------------------------------------  -  3
                   (sum([(x[i] - mean)**2 for i in x]))**2
     
    Sample autocorrelation for lag k
                Sum(i=1 to T - k, (y_i - ybar)*(y_{i+k} - ybar))
        rho_k = ------------------------------------------------
                    Sum(i=1 to T, (y_i - ybar)**2)
     
    Linear regression
        Model:  y = m*x + b
        Sx = Sum(x_i), Sxx = Sum(x_i*x_i), etc.
        m = (n*Sxy - Sx*Sy)/(n*Sxx - Sx**2)
        b = (Sy - m*Sx)/n = ybar - m*xbar
        R**2 = m*(sx/sy)**2    (s is std dev)
             = (n*Sxy - Sx*Sy)**2/((n*Sxx - Sx**2)*(n*Syy - Sy**2))
     
    Weibull distribution
        a = characteristic life (location parameter)
        b = shape parameter
            1 = exponential distribution
            2 = Rayleigh
            3-4 = approximately normal
        PDF(x) = b/a*(x/a)**(b - 1)*exp(-(x/a)**b)
        CDF(x) = 1 - exp(-(x/a)**b)
        CDF(a) = 1 - 1/e = 0.632
        var(x) = Gamma(2 + 1/b) - Gamma(1 + 1/b)**2
    '''))
    print(nl.join(s))
def MonteCarloProportionUncertainties():
    def Header(pp, width):
        print("   n    ", end="")
        fmt = "{{0:^{0}}}".format(width)
        print(''.join([fmt.format(i) for i in pp]))
    def Table(N, pp, width):
        Header(pp, width)
        for n in N:
            print("{0:>7s} ".format(n), end="")
            for P in pp:
                p = float(P)/100
                x = 196*sqrt(p*(1 - p)/float(n))
                s = "{0:.3f}".format(x)
                s = sig(x, 2)
                fmt = "{{0:^{0}s}}".format(width)
                print(fmt.format(s), end="")
            print()
    s = [SectionHeading("Monte Carlo Proportion Uncertainties",
         "Monte_Carlo_uncertainties")]
    t = " "*39 + "p, %"
    s.append(dedent('''
 
    For a Monte Carlo experiment that results in a calculated proportion, the
    "uncertainty" u in % in the proportion at 95% confidence is
     
        u = 100*1.96*sqrt(p*(1 - p)/n)
     
    where p is the observed proportion and n is the number of items in the Monte
    Carlo sample.  This is because the proportion is approximately normally
    distributed with standard deviation sqrt(p*(1 - p)/n) and the normal
    distribution CDF(-1.96) = 0.025.'''))
    print(nl.join(s))
    print(t)
    if 0:
        N = []
        for exponent in range(2, 6):
            for significand in range(1, 10):
                N.append("{0}e{1}".format(significand, exponent))
    else:
        N = (RL(100, 1000, 100) +
             RL(1000, 10000, 1000) +
             RL(10000, 100000, 10000) +
             RL(100000, 1000000, 100000) +
             [1000000])
        N = [str(i) for i in N]
    width = 8
    pp = (".01", ".02", ".05", ".1", ".2", ".5", "1", "2", "5")
    Table(N, pp, width)
    pp = [str(i) for i in range(10, 100, 10)]
    print()
    print(t)
    Table(N, pp, width)
    print(dedent('''
 
    Example:  an experiment with a sample size of n = 1e5 resulted in a proportion
    of 1%.  The "uncertainty" is u = 0.20%.  You'd state the proportion as
    1% +/- 0.20% and explain that this gives a 95% confidenced bound on the
    estimate.  Note this a slightly different uncertainty from the standard
    uncertainty estimate made for a physical measurement using the GUM.
     
    Note the uncertainty is highest for p = 50%.  You can use the p = 50% column to
    select a (conservative) sample size for a particular experiment and a given
    desired "uncertainty" level you'd like to achieve.
     
        Example:  a Monte Carlo experiment will result in a proportion.  If I want
        that proportion to be estimated to within about 1%, how big of a sample
        size should I use?  Look down the p = 50% column to find 1%; read over to
        the left column to get the sample size.  We see n = 9000.
    '''))
def Hypergeometric():
    s = [SectionHeading("Hypergeometric Distribution", "Hypergeometric_dist")]
    s.append(dedent('''

    [jk:143] The hypergeometric distribution is relevant when taking samples
    without replacement from smaller populations.  Given an urn with N balls of
    which Y are white and N - Y are black.  Suppose a sample of n balls is drawn
    randomly from the urn without replacing any of the balls.  Then the probability
    of drawing k white balls in the sample of n balls is
     
        P(k; N, Y, n) = C(Y, k)*C(N - Y, n - k)/C(N, n)
     
    where C(a, b) is a choose b, the binomial coefficient
     
        C(a, b) = a!/(b!*(a - b)!)
     
    For a random variable x with a hypergeometric distribution
     
        E(x) = n*Y/N
        var(x) = [(N - n)/(N - 1)]*n*(Y/N)*(1 - Y/N)
     
    Recurrence
        P(k + 1; N, Y, n) = A*P(k; N, Y, n)
        A = (Y - k)*(n - k)/[(k + 1)*(N - Y - n + k + 1)]
    [jk] also gives recurrences on N, Y, and n.
     
    P(k; N, Y, n) increases with k and reaches a maximum at the greatest integer
    that does not exceed I = (n + 1)*(Y + 1)/(N + 2).  If I is an integer, then
    there are two equal maximum values at I - 1 and I.  If N and Y are large, the
    maximum is near E(x) = n*Y/N.
     
    scipy.stats.hypergeom(N, Y, n) is a discrete random variable with the usual
    scipy functions like cdf, ppf, etc. with argument k.  You can also call
    prob = hypergeom(k, N, Y, n) to get the CDF probability directly.
     
    Example:  Suppose a vet has 35 animals on his premises, 22 which are dogs.  If
    three animals are drawn randomly without replacement, what's the probability
    for the sample having 0, 1, 2, and 3 dogs?
     
        N, Y, n = 35, 22, 3
        rv = hypergeom(N, Y, n)
        for k in range(4):
            print("k = {0:1d}  P = {1:.3f}  CDF = {2:.3f}".format(k, rv.pmf(k),
                rv.cdf(k)))
    results in
        k = 0  P = 0.044  CDF = 0.044
        k = 1  P = 0.262  CDF = 0.306
        k = 2  P = 0.459  CDF = 0.765
        k = 3  P = 0.235  CDF = 1.000
    The most probable number of dogs in the sample is 2.
    '''))
    print(nl.join(s))
def ProportionCI():
    '''You can choose two methods of calculation of the confidence
    interval.  The Clopper-Pearson is conservative and typically exceeds
    the predictions in tables such as [crow:257].  Some web research
    indicated that the Wilson score method seems to be preferred for most
    practical work, so it's the default.  Choose either the "wilson" score
    or the "wilson_continuity".
 
    See https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval.
    Accessed 11 Dec 2014.
    '''
    methods = {
        0 : "Wilson score",
        1 : "Wilson score with continuity correction",
        2 : "Clopper-Pearson",
        3 : "Agresti-Coull",
    }
    method = 1
    percent = True
    def Header(pp, width, indent):
        print(indent, "x  ", end="")
        fmt = "{{0:^{0}}}".format(width)
        print(''.join([fmt.format(i) for i in pp]))
    def Table(n, pp, width, indent=" "*8):
        print("n = {0}".format(n))
        Header(pp, width, indent)
        for x in range(n):
            print("{0}{1:2d}  ".format(indent, x), end="")
            for prob in pp:
                p = x/n
                # prob is e.g. "90%"
                alpha = (1 - float(prob[:-1])/100)/2
                if method == 0:  # Wilson score
                    rv = norm(0, 1)
                    z = abs(rv.ppf(alpha))
                    c = z*sqrt(p*(1 - p)/n + z*z/(4*n**2))
                    a = z*z/n
                    ll = max(0, (p + a/2 - c)/(1 + a))
                    ul = min(1, (p + a/2 + c)/(1 + a))
                elif method == 1:  # Wilson score with continuity correction
                    rv = norm(0, 1)
                    z = abs(rv.ppf(alpha))
                    try:
                        c = z*sqrt(z*z - 1/n + 4*n*p*(1 - p) + (4*p - 2)) + 1
                    except Exception as e:
                        c = 0
                    d = 2*(n + z*z)
                    ll = max(0, (2*n*p + z*z - c)/d)
                    c = z*sqrt(z*z - 1/n + 4*n*p*(1 - p) - (4*p - 2)) + 1
                    ul = min(1, (2*n*p + z*z + c)/d)
                elif method == 2:  # Clopper-Pearson
                    rv = scipy.stats.beta(x, n - x + 1)
                    ll = rv.ppf(alpha)
                    ll = 0 if str(ll) == "nan" else ll
                    rv = scipy.stats.beta(x + 1, n - x)
                    ul = rv.ppf(1 - alpha)
                elif method == 3:  # Agresti-Coull
                    rv = norm(0, 1)
                    z = abs(rv.ppf(alpha))
                    n_tilde = n + z*z
                    p_tilde = (x + z*z/2)/n_tilde
                    c = z*sqrt(p_tilde*(1 - p_tilde)/n_tilde)
                    ll = max(0, p_tilde - c)
                    ul = min(0.999, p_tilde + c)
                else:
                    raise ValueError("Unrecognized method")
                if percent:
                    # Print percentages
                    f = "{0:4.1f}"
                    s = "[{0}, {1}]".format(f.format(ll*100), f.format(ul*100))
                    fmt = "{{0:^{0}s}}".format(width)
                else:
                    # Print fractions
                    f = "{0:.3f}"
                    s = "[{0}, {1}]".format(f.format(ll), f.format(ul))
                    fmt = "{{0:^{0}s}}".format(width)
                print(fmt.format(s), end="")
            print()
    s = [SectionHeading("Confidence Limits for a Proportion ",
         "Proportion_CI"),
         "  (Calculation method = {})".format(methods[method])]
    pct = " in percent" if percent else ""
    s.append(dedent('''

    Suppose a random sample of n items is take from a population and x items are
    found to have a characteristic, leading to a point estimate of the population
    proportion of p = x/n with this characteristic.  The table gives confidence
    intervals for the proportion{}.
    '''.format(pct)))
    print(nl.join(s))
    width = 20
    pp = ("90%", "95%", "99%")
    for n in range(1, 31):
        Table(n, pp, width)
    print(dedent('''

    Ref. https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval.
    Let alpha be the confidence level.  Note the script that produces this document
    lets you choose which method of calculating the table:  Agresti-Coul,
    Clopper-Pearson, Wilson, and Wilson with continuity correction.
     
    For sample sizes larger than 30, use the Clopper-Pearson chart given in
    references such as [ph], [crow], etc.
     
    Example [bl:467]:  suppose x = 4 defects are observed in a sample of n = 25.
    Using the n = 25 table, the line under x = 4 gives the 95% confidence interval
    as
     
    Method
        [bl:467]             [ 4.5, 36.1]
        [crow:260]           [ 5.7, 33.6]
        Agresti-Coul         [ 5.8, 35.3]
        Clopper-Pearson      [ 4.5, 36.1]
        Wilson               [ 6.4, 34.7]
        Wilson corr.         [ 5.3, 36.9]
     
    The 95% column gives the required confidence interval as [0.045, 0.361] for the
    Clopper-Pearson case ([bl]'s method is equivalent).  The table on page 260 of
    [crow] gives the interval [0.057, 0.336].  Because real-world data are noisy, I
    typically round such information to the nearest percent and don't worry about a
    percent or two difference.'''))
    if method == 2:
        print(dedent('''

        Note on the Clopper-Pearson method
            A 100(1 - alpha)% confidence interval for the proportion p is
         
                B(alpha/2; x, n - x + 1) < p < B(1 - alpha/2; x + 1, n - x)
         
            where B(a, b) is the beta distribution percentage point function.  In scipy,
            this is
                rv = scipy.stats.beta(x, n - x + 1)
                lower_limit = rv.ppf(alpha/2)
                rv = scipy.stats.beta(x + 1, n - x)
                upper_limit = rv.ppf(1 - alpha/2)
         
            The Clopper-Pearson formula typically gives wider intervals than other
            estimates.  The Clopper-Pearson formulas are "exact" because they involve
            integration of binomial PDFs, but binomial proportions are discontinuous,
            so the calculated confidence bounds may not match a proportion calculated
            from two integers.  Thus, a 95% confidence bound may be a larger than 95%
            (in some cases up to 99%), and thus may require larger sample sizes than
            needed in experimentation.
        '''))
def StdDevEstimateFromRange():
    # This is not used because it's obsolete; it's subsumed by the information
    # in RangeEstimates().
    s = [SectionHeading("Estimate standard deviation from range",
         "Estimate_stddev_from_range")]
    s.append(dedent('''

    Assuming you have a random sample of n items from a normal distribution, you
    can estimate the standard deviation of the population by multiplying the range
    by the factor k:
     
        n        k
        2      0.886
        3      0.591
        4      0.486
        5      0.430
        6      0.395
        7      0.370
        8      0.351
        9      0.337
        10     0.325
        50     0.222
        100    0.199
        1000   0.154
     
    Ref. [crow:248].
    '''))
    print(nl.join(s))
def StringToMatrix(string):
    '''string is of the form e.g.
        1 2 3 4 5 6
        2 3 4 5 6 7
        ...
    Convert it to a sequence of sequences of numbers.  The numbers will be
    integers if possible; otherwise, they'll be floats.
    '''
    a = []
    for line in string.split(nl):
        line = line.strip()
        if not line or line[0] == "#":
            continue
        b = []
        for s in line.split():
            if "." in s:
                b.append(float(s))
            else:
                b.append(int(s))
        a.append(b)
    assert a
    # Check rows for equal lengths
    assert len(set([len(i) for i in a])) == 1
    return a
def StringToVector(string):
    '''string is of the form e.g. "1 2 3<nl>4 5 6"; convert it to a
    sequence of numbers.  The numbers will be integers if possible;
    otherwise, they'll be floats.
    '''
    a = []
    for line in string.split(nl):
        for s in line.split():
            if "." in s:
                a.append(float(s))
            else:
                a.append(int(s))
    return a
def ControlChartFactors():
    def c4(n):
        return sqrt(2/(n - 1))*gamma(n/2)/gamma((n - 1)/2)
    def K(n):
        return 3*sqrt(1 - c4(n)**2)
    s = [SectionHeading("Factors for Constructing Control Charts",
         "Control_charts")]
    s.append("Discussion follows the tables.  Tables ref. [duncan:968].")
    print(nl.join(s))
    # d2 and d3 values (index is sample size) [duncan:Table M p 968] (these
    # numbers were validated by using the above Monte Carlo calculation).  See
    # [ph:176] for two more decimal places.
    d2 = '''0 0 1128 1693 2059 2326 2534 2704 2847 2970 3078 3173 3258 3336
        3407 3472 3532 3588 3640 3689 3735 3778 3819 3858 3895 3931'''
    d3 = '''0 0 853 888 880 864 848 833 820 808 797 787 778 770 762 755 749
        743 738 733 729 724 720 716 712 709'''
    d2 = [i/1000 for i in StringToVector(d2)]
    d3 = [i/1000 for i in StringToVector(d3)]
    N = range(2, 26)
    indent = " "*3
    #
    print(dedent('''

    Chart for averages:  (assumes a normally-distributed universe)

        n       Sample size
        Xbb     Historical average
        Xb''    Known or chosen population mean
        sigma'' Known or chosen population standard deviation
        sbar    Average of standard deviation
        Rbar    Average of range

      Central line        Control limits
           Xbb              Xbb  +/- A3*sbar
                            Xbb  +/- A2*Rbar
           Xb''             Xb'' +/- A*sigma''\n
    '''))
    width = 10
    h = ("A", "A2", "A3")
    hfmt = "{{0:^{0}s}}".format(width)
    print(indent, " n  ", ' '.join([hfmt.format(i) for i in h]))
    fmt = "{{0:>{0}.3f}}".format(width)
    f = fmt.format
    for n in N:
        sn = sqrt(n)
        A = 3/sn
        A2 = 3/(d2[n]*sn)
        A3 = 3/(c4(n)*sn)
        print(indent, "{0:2d}".format(n), f(A), f(A2), f(A3))
    #
    print(dedent('''

    Chart for ranges:  (assumes a normally-distributed universe)

        n       Sample size
        Rbar    Average of range
        sigma'  Historical population standard deviation
        sigma'' Known or chosen population standard deviation
        d2      Mean of w = R/sigma'
        d3      Standard deviation of w = R/sigma'

      Central line        Control limits
           Rbar             D3*Rbar and D4*Rbar
           d2*sigma''       D1*sigma'' and D2*sigma''\n
    '''))
    width = 8
    h = ("d2", "1/d2", "d3", "D1", "D2", "D3", "D4")
    hfmt = "{{0:^{0}s}}".format(width)
    print(indent, " n ", ' '.join([hfmt.format(i) for i in h]))
    fmt = "{{0:>{0}.3f}}".format(width)
    fmt2 = "{{0:>{0}.4f}}".format(width)
    fmt3 = "{{0:^{0}s}}".format(width)
    f = fmt.format
    for n in N:
        sn = sqrt(n)
        D1 = fmt3.format(" 0") if n < 7 else f(d2[n] - 3*d3[n])
        D2 = d2[n] + 3*d3[n]
        D3 = fmt3.format(" 0") if n < 7 else f(1 - 3*d3[n]/d2[n])
        D4 = 1 + 3*d3[n]/d2[n]
        print(indent, "{0:2d}".format(n), f(d2[n]), fmt2.format(1/d2[n]),
            f(d3[n]), D1, f(D2), D3, f(D4))
    #
    print(dedent('''

    Chart for standard deviations:  (assumes a normally-distributed universe)

        n       Sample size
        sbar    Average of standard deviations
        sigma'' Known or chosen population standard deviation
        c4      Constant for standard deviation central line

      Central line        Control limits
           sbar             B3*sbar and B4*sbar
           d2*sigma''       B5*sigma'' and B6*sigma''\n
    '''))
    width = 8
    h = ("c4", "B3", "B4", "B5", "B6")
    hfmt = "{{0:^{0}s}}".format(width)
    print(indent, " n ", ' '.join([hfmt.format(i) for i in h]))
    fmt = "{{0:>{0}.3f}}".format(width)
    fmt2 = "{{0:>{0}.4f}}".format(width)
    fmt3 = "{{0:^{0}s}}".format(width)
    f = fmt.format
    for n in N:
        B3 = fmt3.format(" 0") if n < 6 else f(1 - K(n)/c4(n))
        B4 = 1 + K(n)/c4(n)
        B5 = fmt3.format(" 0") if n < 6 else f(c4(n) - K(n))
        B6 = c4(n) + K(n)
        print(indent, "{0:2d}".format(n), fmt2.format(c4(n)),
            B3, f(B4), B5, f(B6))
    print(dedent('''

    Ref. Table M from [duncan:968], [bl:477], [crow:254].  The somewhat strange
    notation probably was standardized by the "ASTM Manual on Quality Control of
    Materials", 1951 (as referenced in [crow]).  Note that [crow] and [bl] are
    about the same tables, but give different column names and values than
    [duncan]; where they overlap, they are equal.  (I used Duncan's stuff for
    controlling the ILS stuff in the late 1980's and it worked fine.)
     
    Formulas for the table constants:
        Xbarbar = grand average
        Xbar = sample average
        Rbar = sample average range
        sbar = sample average standard deviation
        sigma' = population standard deviation
        sigma'' = known or chosen population standard deviation for ctrl charts
        A = 3/sqrt(n)
        A2 = 3/(d2*sqrt(n))
        A3 = 3/(c4*sqrt(n))
        B3 = 1 - K/c4
        B4 = 1 + K/c4
        B5 = c4 - K
        B6 = c4 + K
        D1 = d2 - 3*d3
        D2 = d2 + 3*d3
        D3 = 1 - 3*d3/d2
        D4 = 1 + 3*d3/d2
        K = 3*sqrt(1 - c4**2)
        c4 = sqrt(2/(n - 1))*(G(n/2)/(G((n-1)/2)))
        G = gamma function
        w = R/sigma'' = relative range for a normal distribution
        d2 = mean of w = E(Rbar)/sigma' (tabulated in [duncan:948])
        d3 = standard deviation of w (tabulated in [duncan:948])
            Note:  see the python script below that can perform a Monte Carlo
            calculation of d2 and d3 (used to check the d2 and d3 arrays above).
     
    Estimating sigma' from R [bl:476]
        Let there be k subgroups of data and Rbar be the average of the ranges of
        these subgroups.  An unbiased estimator of sigma' is Rbar/d2.
     
        [duncan:139] For controlling variability with small samples, the range is a
        reasonable substitute for the standard deviation and only slightly less
        efficient.  Its advantage is that it's easy to calculate and is thus
        preferred where control charts are maintained by hand.
     
        https://en.wikipedia.org/wiki/Range_%28statistics%29 gives the general
        formula for the CDF of the range of a random variable.
     
    Monte Carlo calculation of d2 and d3
        Instead of setting up a numerical integration for these values, here's a
        script that performs a Monte Carlo calculation that reproduces the data
        in [duncan:948]:
     
        from __future__ import print_function, division
        from numpy import array, average, cov, sqrt
        from numpy.random import normal
     
        M = 10**5
        print("""
        Monte Carlo simulation of the range of a normal distribution with mean
        0 and standard deviation 1.  d2 is the estimated population mean of
        the range random variable and d3 is the estimated standard deviation
        (these are standard notations used in control chart practice).  This
        calculation will essentially reproduce the first three columns of
        table D1 on page 948 in Duncan, "Quality Control and Industrial
        Statistics", 4th ed., Irwin, 1974.
     
        Number of samples to generate = {0}
                d2        d3
         n     Mean     StdDev
        --    ------    ------"""[1:].format(M))
        for n in range(2, 13):
            r = []
            for i in range(M):  # Generate M samples of size n of N(0, 1)
                sample = normal(0, 1, n)
                r.append(max(sample) - min(sample))
            # Calculate mean and standard deviation of range random variable
            r = array(r)
            m, s = average(r), sqrt(cov(r))
            print("{0:2d}{1:9.2f}{2:10.2f}".format( n, m, s))
    '''))
def RangeEstimates():
    s = [SectionHeading("Range estimates", "RangeEstimates")]
    s.append(dedent('''

    The following table ([ph:177]) can be used to:
     
        1) Estimate a population standard deviation from a sample range.
        2) Put confidence bounds on a range.
     
    Assumes a random sample from a normal distribution.  Each entry's unit is the
    population standard deviation.
    '''))
    pp = "{0:25s}{{0}} percentage points".format("")
    print(nl.join(s))
    # From Table 22 [ph:177].  Columns 2-13 are multiplied by 1000; column 1 is
    # multiplied by 1e4.
    table = dedent('''

    #       Column indices:
    #        0  1    2   3   4   5   6   7       8   9   10  11  12  13
    #                     Lower pp                     Upper pp
    #        n  k   .1  .5  1   2.5 5   10      10  5   2.5 1   .5  .1
             2 8862 000 001 002 004 009 018     233 277 317 364 397 465
             3 5908 006 013 019 030 043 062     290 331 368 412 442 506
             4 4857 020 034 043 059 076 098     324 363 398 440 469 531
             5 4299 037 055 067 085 103 126     348 386 420 460 489 548
             6 3946 053 075 087 107 125 149     366 403 436 476 503 562
             7 3698 069 092 105 125 144 168     381 417 449 488 515 573
             8 3512 083 108 120 141 160 184     393 429 460 499 525 582
             9 3367 097 121 134 155 174 197     404 439 470 508 534 590
            10 3249 108 133 147 167 186 209     413 447 478 516 542 597
            11 3152 119 145 158 178 197 220     421 455 486 523 549 604
            12 3069 129 155 168 188 207 230     428 462 492 529 555 609
            13 2998 139 164 177 198 216 239     435 468 499 535 560 614
            14 2935 147 172 186 206 224 247     441 474 504 540 565 619
            15 2880 155 180 193 214 232 254     447 480 509 545 570 623
            16 2831 162 188 201 221 239 261     452 485 514 549 574 627
            17 2787 169 194 207 227 245 267     457 489 518 554 578 631
            18 2747 176 201 214 234 252 273     461 493 522 557 582 635
            19 2711 182 207 220 239 257 279     465 497 526 561 586 638
            20 2677 188 212 225 245 263 284     469 501 530 565 589 641
        ''')
    t = matrix(StringToMatrix(table))
    nrows = len(t[:,0])
    #
    print(pp.format("Lower"))
    print(" n      k      ", end="")
    for i in ".1 .5 1 2.5 5 10".split():
        print("{0:^9s} ".format(i + "%"), end="")
    print()
    nrows = len(t[:,0])
    for i in range(nrows):
        r = t[i, :].tolist()[0]
        print("{0:2d} ".format(r[0]), end="")   # n
        print("{0:8.4f} ".format(r[1]/1e4), end="")   # k
        for x in r[2:8]:
            print("{0:9.2f} ".format(x/100), end="")
        print()
    #
    print()
    print(pp.format("Upper"))
    print(" n      k      ", end="")
    for i in "90 95 97.5 99 99.5 99.9".split():
        print("{0:^9s} ".format(i + "%"), end="")
    print()
    nrows = len(t[:,0])
    for i in range(nrows):
        r = t[i, :].tolist()[0]
        print("{0:2d} ".format(r[0]), end="")   # n
        print("{0:8.4f} ".format(r[1]/1e4), end="")   # k
        for x in r[8:]:
            print("{0:9.2f} ".format(x/100), end="")
        print()
    print(dedent('''

    Suppose a random sample of n measurements is taken from a normal distribution.
    The range of the measurements is R.
     
    Point estimate of the population standard deviation:
        Multiply R by the factor k for the given sample size.
     
    Confidence interval for the range:
        Select the significance level and get the lower and upper percentage point
        factors.  Multiply them by the population standard deviation to get the 
        confidence interval for the range.
     
    Example:  7 measurements (sorted) were [40, 54, 59, 59, 67, 68, 72].  The range
    is R = 72 - 40 = 32.  A point estimate for the population standard deviation is
    sigma = k*R where k = 0.3698; the estimate is sigma = 11.8 (the true population
    value was 10; the sample standard deviation was 10.80).
     
    A 95% confidence interval for the range is [1.25*sigma, 4.49*sigma] or [15,
    53].  A large number of samples of size 7 from this normal distribution would
    have the range fall within this interval 95% of the time.
     
        Note:  the example's sample was generated with the following python code
        (requires numpy):
            from numpy.random import normal, seed
            seed(0)
            mean, sdev, n = 50, 10, 7
            print(normal(mean, sdev, n).astype(int))
     
    The following code generates a histogram for the range and a visual estimate of
    the approximate 95% confidence interval would be about [12, 50], quite
    consistent with the calculated [15, 53] above.
     
        from numpy.random import normal
        from pylab import *
        rng = []
        for i in range(10**5):
            r = normal(50, 10, 7)
            rng.append(max(r) - min(r))
        hist(rng, bins=50)
        show()
    '''))
def StdDevSampleSize():
    s = [SectionHeading("Sample size to estimate standard deviation",
         "Sdev_Est_SampleSize")]
    s.append(dedent('''

    Given a desired confidence level, determine the sample size to determine the
    standard deviation within p% of its true value.  Assumes random sampling from a
    normal distribution.
    '''))
    print(nl.join(s))
    m, indent = -2.0167, " "*4
    pp = ("90%", "95%", "99%")
    A = (13610, 19770, 32670)
    print(" "*19, "Confidence")
    print(indent, "p, %     ", end="")
    for p in pp:
        print("{0:^8s}".format(p), end="")
    print()
    print(indent, "-"*4, end="    ")
    for i in range(3):
        print("{0:^8s}".format("-"*4), end="")
    print()
    for p in range(5, 51):
        print(indent, " {0:2d}   ".format(p), end="")
        for a in A:
            df = int(ceil(a*p**m))
            print("{0:8d}".format(df), end="")
        print()
    print(dedent('''

    Example:  a manufacturing engineer wants to measure the variation in product
    quality by measuring the standard deviation of a random sample of parts.  If he
    wants to know the value within 25% of the true value at 95% confidence, how
    large a sample should he measure?  Ans. 30.
     
        However, production management has decided that only 20 units can be made
        available for experimentation.  At 95% confidence, what will the standard
        deviation be known within?  Ans. 31%.
     
    The table is constructed from empirical equations fitted to curves given in
    chart 9 in [crow:277]:
        90%:  df = 13610*p**m
        95%:  df = 19770*p**m
        99%:  df = 32670*p**m
    where m = -2.0167, p = confidence in %, and df = degrees of freedom.
    '''))
def Regression():
    s = [SectionHeading("Linear_Regression", "Regression")]
    s.append(dedent('''

    Simple linear regression
        y = mx + b
        m = (nΣxy - ΣxΣy)/(nΣx² - (Σx)²)
        b = (Σy - mΣx)/n = ybar = m*xbar
        R² = (m*s_x/s_y)²
           = (nΣxy - ΣxΣy)²/[(nΣx² - (Σx)²)(nΣy² - (Σy)²)]

    HP-42s registers
        ΣREG = 11
        R11 = Σx
        R12 = Σx²
        R13 = Σy
        R14 = Σy²
        R15 = Σxy
        R16 = n
    '''))
    print(nl.join(s))
if __name__ == "__main__":
    dbg = 0     # True to work on a specific section
    if 1:
        # We'll capture all output to stdout so that all whitespace at the end
        # of the lines can be removed.
        original_stdout = sys.stdout
        stream = StringIO()
        sys.stdout = stream
        Versions()
        if not dbg:
            Normal()
            StudentT_PP()
            ChiSquarePP()
            FDistributionPP()
            StdDevConfidenceLimits()
            StdDevSampleSize()
            ProbabilityPlotting()
            BinomialCDF()
            PoissonCDF()
            ProportionCI()
            Hypergeometric()
            UniformRandomDeviates()
            NormalRandomDeviates()
            StatisticsFormulas()
            MonteCarloProportionUncertainties()
            RangeEstimates()
            ControlChartFactors()
            Regression()
            References()
        tables = stream.getvalue()
        # Now combine with headings
        stream = StringIO()
        sys.stdout = stream
        print(title, end=nl)
        for i in headings:
            print(i)
        print(tables)
        sys.stdout = original_stdout
        # Remove spaces at end of lines
        lines = [i.rstrip() for i in stream.getvalue().split(nl)]
        s = nl.join(lines)
        if len(sys.argv) > 1:
            print(stream.getvalue())
        else:
            open("statistics", "wb").write(s.encode("UTF-8"))
            exit(0)
            #try:
            if 1:
                open("statistics", "w").write(s)
            if 1:
            #except UnicodeEncodeError as e:
                print("Unicode error:  wrote to statistics as binary")
                print("Error =", e)
                open("statistics", "wb").write(s.encode("UTF-8"))
    else:
        Normal()
