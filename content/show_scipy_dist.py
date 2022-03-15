import numpy as np
from scipy import stats
from columnize import Columnize
if 1:
    l = sorted([d for d in dir(stats) if isinstance(getattr(stats,d),
        stats.rv_continuous)])
    print("Continuous distributions:")
    for i in Columnize(l):
        print(i)
    print()
if 1:
    l = sorted([d for d in dir(stats) if isinstance(getattr(stats,d),
               stats.rv_discrete)])
    print("Discrete distributions:")
    for i in Columnize(l):
        print(i)
