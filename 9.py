#Schrodinger
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import brentq

E0 = 0
E1 = 10
V0 = 20
przedzial = 1
y = np.zeros((600,2))
x = np.linspace(0,3*przedzial, 600)
#y0_sym = y
y0_sym = np.array([1, 0])
#y0_asym = y
#y0_asym[0] = [0, 1]
print(y[1])

def V(x):
    if x < -przedzial or x > przedzial:
        return 0
    else:
        return V0

def SE(y, x):
    a0 = y[1]
    a1 = 2.0 * (V(x)-E) * y[0]
    return np.array([a0, a1])

def psi(energy):
    global y
    global E
    E = energy
    y = odeint(SE, y0_sym, x)
    return y[-1, 0]

energyvalue = brentq(psi, E0, E1)

print(energyvalue)
plt.plot(x, y[:, 0], -x, y[:, 0])
plt.show()