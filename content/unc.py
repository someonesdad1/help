'''
*uncertainties*

|unc_basics|
|unc_unumpy|
|unc_printing|

Web pages:
  https://pythonhosted.org/uncertainties/
  https://pythonhosted.org/uncertainties/user_guide.html
  https://pythonhosted.org/uncertainties/numpy_guide.html
  https://pythonhosted.org/uncertainties/tech_guide.html

Three-letter fields starting with x indicate more details

-----------------------------------------------------------------------------
Basics                                       *unc_basics*

import uncertainties import ufloat, ufloat_fromstr
x = uncertainties.ufloat(nominal_value, uncertainty)

uncertainties.ufloat_fromstr takes various strings:
    x = ufloat_fromstr("0.20+/-0.01")
    x = ufloat_fromstr("(2+/-0.1)e-01") # Factored exponent
    x = ufloat_fromstr("0.20(1)")       # Short-hand notation
    x = ufloat_fromstr("20(1)e-2")      # Exponent notation
    x = ufloat_fromstr(u"0.20±0.01")    # Pretty-print form
    x = ufloat_fromstr("0.20")          # Automatic uncertainty of +/-1 on last

Nominal value and uncertainty
    x.nominal_value
    x.std_dev

    The following work on floats and ufloats:
        uncertainties.nominal_value(x)
        uncertainties.std_dev(x)

Printing  xxa
    Controlling uncertainty digits with u format spec
        print("x = {:.2u}".format(x))
    Pretty printing P format uses Unicode characters
        x = ufloat(2e-1, 0.1e-1)
        print(x)                    --> 0.200+/-0.010
        print("{:.2e}'.format(x))   --> (2.00+/-0.10)e-01
        print("{:.2eP}'.format(x))  --> (2.00±0.10)×10⁻¹
    LaTeX printing
        print("{:.2eL}'.format(x))  
            --> \left(2.00 \pm 0.10\right) \times 10^{-1}
        The following snippet can turn this LaTeX output into a format
        string for Open Office equations:
            x = ufloat(0.2, 0.01)
            s = "{:.2eL}".format(x)
            s = s.replace(r"\left", " left ").replace(r"\right", " right ")
            s = s.replace(r"\pm", " ± ").replace(r"\times", " times ")
            print(s)

Testing for a ufloat
    isinstance(x, uncertainties.UFloat)

uncertainties.umath functions
    acos      atanh     erf       floor     isinf     log1p     sinh
    acosh     ceil      erfc      fmod      isnan     modf      sqrt
    asin      copysign  exp       frexp     ldexp     pow       tan
    asinh     cos       expm1     fsum      lgamma    radians   tanh
    atan      cosh      fabs      gamma     log       sin       trunc
    atan2     degrees   factorial hypot     log10

ufloats in numpy arrays
    arr = numpy.array([ufloat(1, 0.01), ufloat(2, 0.1)])
    print(2*arr)\
        -> [2.0+/-0.02 4.0+/-0.2]

Comparisons

    ufloats are random variables with unspecified distributions; they are
    characterized by much (most) of the probability density being largest
    in the neighborhood of the nominal_value and most of the time a random
    sample will be within a small number of std_dev values of the nominal
    value.  Thus, 
        >>> x = ufloat(3.14, 0.01)
        >>> y = ufloat(3.00, 0.01)
        >>> x > y
        True
    because x is largely contained in 3.14±~0.01 and y is largely contained
    in 3±~0.01, which means random samples will obey the indicated ordering
    most of the time.

    However, comparing
        >>> x = ufloat(3, 0.01)
        >>> y = ufloat(3.0001, 0.01)
    returns a meaningless Boolean value because the approximate linearity
    assumption is violated [(x, y) --> (x > y)] is not continuous.

    However, values with largely overlapping probability distributions can
    sometimes be compared unambiguously:

        >>> x = ufloat(3, 1)
        >>> x
        3.0+/-1.0
        >>> y = x + 0.0002
        >>> y
        3.0002+/-1.0
        >>> y > x
        True

    In fact, correlations guarantee that y is always larger than x: y-x
    correctly satisfies the assumption of linearity, since it is a constant
    “random” function (with value 0.0002, even though y and x are random).
    Thus, it is true that y > x.

Uncertainty components
    Use tags to label components (do not need to be unique for each
    variable):
        >>> u = ufloat(1, 0.1, "u variable")  # Tag
        >>> v = ufloat(10, 0.1, "v variable")
        >>> sum_value = u+2*v
        >>> sum_value
        21.0+/-0.223606797749979
        >>> for (var, error) in sum_value.error_components().items():
        ...     print "{}: {}".format(var.tag, error)
        ...
        u variable: 0.1
        v variable: 0.2

Covariance matrix
    >>> sum_value = u+2*v
    >>> cov_matrix = uncertainties.covariance_matrix([u, v, sum_value])
    -->
    [[0.01, 0.0,  0.01],
     [0.0,  0.01, 0.02],
     [0.01, 0.02, 0.05]]

    You can create a covariance relation
    >>> (u2, v2, sum2) = uncertainties.correlated_values([1, 10, 21],
                            cov_matrix)

Correlation matrix (needs numpy)
    >>> corr_matrix = uncertainties.correlation_matrix([u, v, sum_value])
    >>> corr_matrix
    -->
    array([[ 1.        ,  0.        ,  0.4472136 ],
           [ 0.        ,  1.        ,  0.89442719],
           [ 0.4472136 ,  0.89442719,  1.        ]])

    Use of a correlation matrix:
        >>> (u3, v3, sum3) = uncertainties.correlated_values_norm(
        ...     [(1, 0.1), (10, 0.1), (21, 0.22360679774997899)], corr_matrix)
        >>> print u3
        1.00+/-0.10

Making custom functions accept uncertainty arguments
    wrapped_f = uncertainties.wrap(f)

    Note f must return a single float.

Standard score of a number using a ufloat
    x = ufloat(0.2, 0.01)
    x.std_score(0.17) --> -3 
        (i.e., 0.17 is 3 standard deviations below the mean)

Derivatives
    >>> u = ufloat(1, 0.1)
    >>> v = ufloat(10, 0.1)
    >>> sum_value = u+2*v
    >>> sum_value.derivatives[u]
    1.0
    >>> sum_value.derivatives[v]
    2.0

-----------------------------------------------------------------------------
unumpy                                       *unc_unumpy*

from uncertainties import unumpy

Building arrays
    >>> arr = unumpy.uarray([1, 2], [0.01, 0.002])
    >>> print arr
    [1.0+/-0.01 2.0+/-0.002]

Accessing components
    unumpy.nominal_values(arr)
        --> array([ 1.,  2.])
    unumpy.std_devs(mat)
        --> matrix([[ 0.1  ,  0.002]])

Math functions
    e.g. unumpy.arccos()   Note numpy's function names are used

Pickling and text format
    Has advantage of preserving correlations between variables.

    Text format:
        numpy.savetext(filename, ftm="%r")
        numpy.ufloat_fromstr

unumpy.ulinalg
    >>> unumpy.ulinalg.inv([[ufloat(2, 0.1)]])
    array([[0.5+/-0.025]], dtype=object)
    >>> unumpy.ulinalg.pinv(mat)    # Pseudo-inverse
    matrix([[0.2+/-0.0012419339757],
            [0.4+/-0.00161789987329]], dtype=object)


-----------------------------------------------------------------------------
Printing examples xxa                                    *unc_printing*

'''
from uncertainties import ufloat, ufloat_fromstr, UFloat
import string
import sys
from pdb import set_trace as xx
if len(sys.argv) > 1:
    import debug
    debug.SetDebugger()
from wrap import dedent
x = ufloat(12345.67, 0.1234)
i = " "*4
if 1:
    # Pretty printing:  S = shorthand, P = pretty (Unicode symbols),
    # L = LaTeX
    s = "x = ufloat(12345.67, 0.1234)"
    print(f"Pretty printing of uncertainties")
    print(f"{i}Definition of x is", repr(s))
    exec(s)
    print(f"{i}x = {x} (default format spec)")
    print(f"{i}x = {x:P} (P format spec)")
    for n in range(1, 4):
        print(f"{i}{n} {'digits:' if n > 1 else 'digit:'}")
        print(f"{i*2}fP   {x:.{n}fP}")
        print(f"{i*2}fS   {x:.{n}fS}")
        print(f"{i*2}fL   {x:.{n}fL}")
        print(f"{i*2}eP   {x:.{n}eP}")
        print(f"{i*2}eS   {x:.{n}eS}")
        print(f"{i*2}eL   {x:.{n}eL}")
        print(f"{i*2}gS   {x:.{n}gS}")
    # Demonstrate these strings can be used for reinitialization
    s = "0.00+/-0.17"
    for t in "{:fP} {:fS} {:eP} {:eS}".split():
        y = ufloat_fromstr(t.format(x))
        assert(str(y - x) == "0.00+/-0.17")
if 1:
    print(dedent(f'''
 
    Example of subclassing the formatter so that ufloats print as desired
    and allow other numerical types to also print as desired:'''))
    s = '''
    class Fmt(string.Formatter):
        def format_field(self, value, format_spec):
            if isinstance(value, UFloat):
                return value.format(format_spec+'S')  # Shorthand option added
            else:  # float, int, etc.
                return super(Fmt, self).format_field(value, format_spec)
    '''.rstrip()[1:]
    print(s)
    exec(dedent(s))
    n, s = 12345.67, 0.1234
    x = ufloat(n, s)
    frmtr = Fmt()
    print()
    print(frmtr.format(i + "Result = {0:.1u}", x))  # 1-digit uncertainty
    print(frmtr.format(i + "Result = {0:.1f}", n))  # float
    print(frmtr.format(i + "Result = {0:d}", int(n)))  # int
