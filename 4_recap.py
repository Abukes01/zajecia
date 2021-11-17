import numpy as np
from scipy import interpolate
from matplotlib import pyplot as plt

xnew = np.linspace(0,10, num=11)
print(xnew)
ynew = np.linspace(10, 20, num=11)
print(ynew)
znew = np.linspace(20, 30, num=11)
print(znew)

with open('test.txt', 'wt') as file:
    zipped = zip(xnew, ynew, znew)
    for x, y, z in zipped:
        file.write(f'{x} {y} {z}\n')

with open('test.txt', 'rt') as file:
    lines = file.readlines()
    transformed = [item.strip('\n').split(' ') for item in lines]
    x, y = [float(unpack[0]) for unpack in transformed], [float(unpack[1]) for unpack in transformed]
    print(x)
    print(y)

