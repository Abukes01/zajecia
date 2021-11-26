import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# # CURVEFIT
# f = lambda x, a, b: a*x + b
# x = np.arange(0, 10)
# a = 2.2
# b = 1.7
# y = f(x, a, b)
#
# rng = np.random.default_rng()
# noise = 0.2*rng.normal(size=x.size)
# yn = y+noise
# plt.plot(x, yn, 'o')
#
# Popt, Pcov = curve_fit(f, x, yn)
# print(Popt, Pcov, sep='\n\n')
# plt.plot(x, f(x, *Popt))
# plt.show()

