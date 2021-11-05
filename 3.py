from scipy import interpolate
import numpy as np
from matplotlib import pyplot as plt


# # Z1
# x = np.linspace(0, 10, num=11)
# y = (np.cos(-x**2/9)+1)-1/200
# x2 = np.linspace(0, 10, num=200)
# y2 = (np.cos(-x2**2/9)+1)-1/200
#
# plt.plot(x2,y2, '-g', x, y, 'ro')
# plt.show()


# # Z2
# x = np.linspace(0, 10, num=11)
# y = (np.cos(-x**2/9)+1)-1/200
# f = interpolate.interp1d(x, y, kind='cubic')
# xnew = np.linspace(0, 10, num=200)
# ynew = f(xnew)   # use interpolation function returned by `interp1d`
# plt.plot(x, y, 'o', xnew, ynew, '-')
# plt.show()


# # Z3
# x = np.linspace(0, 10, num=11)
# y = (np.cos(-x**2/9)+1)-1/200
# f = interpolate.interp1d(x, y, kind='cubic')
# xnew = np.linspace(0, 10, num=200)
# ynew = f(xnew)
# data = np.zeros((len(xnew),2))
# data[:,0] = xnew
# data[:,1] = ynew
# print(data)


# # Z4
# x1 = np.linspace(0, 10, num=11)
# y1 = (np.cos(-x1**2/9)+1)-1/200
# f1 = interpolate.interp1d(x1, y1, kind='cubic')
# xnew = np.arange(0.1, 10, 0.1)
# ynew = f1(xnew)
# prime = lambda x, h, func: (1/2*h)*(func(x+h)-func(x-h))
# speed=[]
# for x in xnew:
#     speed.append(prime(x, 0.1, f1))
# print(speed)
# plt.subplot(121)
# plt.title('Położenie w czsie')
# plt.xlabel('Czas')
# plt.ylabel('Położenie')
# plt.plot(xnew, ynew)
# plt.subplot(122)
# plt.title('Prędkość')
# plt.xlabel('Czas')
# plt.ylabel('Prędkość')
# plt.plot(xnew, speed)
# plt.show()



