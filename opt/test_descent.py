from descent import minimize
import numpy as np
import sys

"""
Results should look like:

x0 = 0.10; min = cosf(x=0.297)=-3.172
x0 = 0.80; min = cosf(x=0.989)=-1.006
x0 = 0.30; min = cosf(x=0.297)=-3.172
x0 = 1.20; min = cosf(x=0.989)=-1.006
x0 = 0.05; min = cosf(x=0.297)=-3.172
x0 = 2.00; min = x2(x=2.000)=1.000
x0 = -1.00; min = x2(x=2.000)=1.000
x0 = -9.30; min = x2(x=2.000)=1.000
x0 = 2.00; min = x3(x=0.333)=-0.593
x0 = 0.50; min = x3(x=0.333)=-0.593
x0 = 0.33; min = x3(x=0.333)=-0.593
x0 = 1.00; min = x3(x=0.333)=-0.593
"""


def assertequals(which, result, expecting):
    if abs(result - expecting) > 0.0001:
        sys.stderr.write(
            "Failure: %s expecting %1.4f found %1.4f (not within %1.2f)\n" % (
            which, expecting, result, PRECISION))
        return False
    return True


LEARNING_RATE = 2.0
h = 0.00001
PRECISION = 0.00000001  # can't be too small as f(x)-f(xprev) prec is low


def cosf(x): return np.cos(3 * np.pi * x) / x


def x2(x): return (x - 2) ** 2 + 1


def x3(x): return 5 * x ** 3 + 2 * x ** 2 - 3 * x


tests = [(cosf, 0.1, 0.29691298),
         (cosf, 0.8, 0.98865134),
         (cosf, 0.3, 0.29691298),
         (cosf, 1.2, 0.98865134),
         (cosf, 0.05, 0.29691298),

         (x2, 2.0, 2.0),
         (x2, -1.0, 2.0),
         (x2, -9.3, 2.0),

         (x3, 2.0, 1 / 3.0),
         (x3, 0.5, 1 / 3.0),
         (x3, 1 / 3.0, 1 / 3.0),
         (x3, 1.0, 1 / 3.0),
]

print """def cosf(x): return np.cos(3 * np.pi * x) / x
def x2(x): return (x-2)**2 + 1
def x3(x): return 5*x**3 + 2*x**2 - 3*x
"""

for t in tests:
    f = t[0]
    x0 = t[1]
    minx = t[2]
    tracex = minimize(f, x0, LEARNING_RATE, h, PRECISION)

    start = tracex[0]
    stop = tracex[-1]

    # print "Start f(x=%2.8f)=%2.8f" % (start, f(start))
    print "x0 = %1.2f; min = %s(x=%2.3f)=%2.3f" % (x0, f.__name__, stop, f(stop))
