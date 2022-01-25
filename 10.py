import numpy as np
import matplotlib.pyplot as plt

dl = 1e-6  # very small interval to stop bisection
n = 2000
ul = np.zeros(n, float)
ur = np.zeros(n, float)
k2l = np.zeros(n, float)  # k**2 left wavefunc
k2r = np.zeros(n, float)
# plot every 5 points
imax = 100
xl0 = 1.8
xr0 = 5  # leftmost, rightmost x
# Xl0 and xr0 must be adjusted to the
# aproportiate potential values
x = np.linspace(xl0, xr0, n)
h = (xr0 - xl0) / (n - 1.)
amin = -500
amax = -400  # root limits
e = amin  # Initial E guess
de = 0.01
ul[0] = 0.0
ul[1] = 0.00001
ur[0] = 0.0
ur[1] = 0.00001


def f(x):
    gamma = 500
    rm = 2.5
    y = gamma * (np.power(rm / x, 12) - 2 * np.power(rm / x, 6))
    return y


Vpot = f(x)
im = Vpot.argmin()  # match point
nl = im + 2
nr = n - im + 1  # left, right wv
istep = 0


def setk2(e):  # k2
    global n, h, xl0, xr0
    for i in range(0, n):
        xl = xl0 + i * h
        xr = xr0 - i * h
        k2l[i] = e - f(xl)
        k2r[i] = e - f(xr)
    return k2l, k2r


def numerov(n, h, k2, u):  # Numerov algorithm
    b = (h ** 2) / 12.0
    for i in range(1, n - 1):
        u[i + 1] = (2 * u[i] * (1 - 5 * b * k2[i]) - (1. + b * k2[i - 1]) * u[i - 1]) / (1 + b * k2[i + 1])


[k2l, k2r] = setk2(e)
numerov(nl, h, k2l, ul)  # Left psi
numerov(nr, h, k2r, ur)  # Right psi
fact = ur[nr - 2] / ul[im]  # Scale
for i in range(0, nl):
    ul[i] = fact * ul[i]
f0 = (ur[nr - 1] + ul[nl - 1] - ur[nr - 3] - ul[nl - 3]) / (2 * h * ur[nr - 2])  # Log deriv


def normalize(ul, ur):
    global n, h, xl0, xr0
    asum = 0
    for i in range(0, n):
        if i > im:
            ul[i] = ur[n - i - 1]
            asum = asum + ul[i] * ul[i]
    asum = np.sqrt(h * asum)
    ul = ul / asum


while abs(de) > dl and istep < imax:  # bisection algorithm

    e1 = e
    e = (amin + amax) / 2
    for i in range(0, n):
        k2l[i] = k2l[i] + e - e1
        k2r[i] = k2r[i] + e - e1
    im = 500
    nl = im + 2
    nr = n - im + 1
    numerov(nl, h, k2l, ul)  # New wavefuntions
    numerov(nr, h, k2r, ur)
    fact = ur[nr - 2] / ul[im]
    for i in range(0, nl):
        ul[i] = fact * ul[i]
    f1 = (ur[nr - 1] + ul[nl - 1] - ur[nr - 3] - ul[nl - 3]) / (2 * h * ur[nr - 2])  # Log deriv

    if f0 * f1 < 0:  # Bisection localize root
        amax = e
        de = amax - amin
    else:
        amin = e
        de = amax - amin
        f0 = f1
    normalize(ul, ur)
    istep = istep + 1

asum = 0
for i in range(0, n):
    asum = asum + ul[i] * ul[i]
#         asum = asum+ul[i]*ul[i]
asum = np.sqrt(h * asum)
ul = ul / asum
# plt.subplot(1,1,1)
plt.plot(x, f(x))
plt.plot(x, ul * 450)
plt.show()