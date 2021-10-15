import numpy as np
from matplotlib import pyplot as plt
import timeit


# def silnia(liczba):
#     out = 1
#     for i in range(1, liczba + 1):
#         out *= i
#     return out
#
# g = lambda x: x+6-4*np.exp(x)
# gprim = lambda x: -4*np.exp(x)+1
# def metoda_newtona(a, precision, function=None, functionprime = None):
#     while abs(function(a)) >= precision:
#         a = a - function(a)/functionprime(a)
#     return print(f'Miejsce zerowe: {a}')
#
#
# metoda_newtona(0, 10**(-10), function=g, functionprime=gprim)



# lista = [f(x) for x in range(-3, 3)]
# lista2 = [_ for _ in range(-3, 3)]
#
# plt.plot(lista2, lista, '-o')
# plt.show()

# f = lambda x: np.exp(x) - x ** 2 + 1


# def metoda_bisekcji_recu(a, b, funkcja, precision=10 ** (-10)):
#     x = (a + b) / 2
#     if abs(a - b) > precision:
#         y = funkcja(x)
#         if y * funkcja(a) < 0:
#             metoda_bisekcji_recu(a, x)
#         elif y * funkcja(b) < 0:
#             metoda_bisekcji_recu(x, b)
#     else:
#         return print(f'Miejsce zerowe: {x}')
#
# def metoda_bisekcji_while(a, b, funkcja, precision=10 ** (-10)):
#
#     while abs(a - b) > precision:
#         x = (a + b) / 2
#         y = funkcja(x)
#         if y * funkcja(a) < 0:
#             b = x
#         elif y * funkcja(b) < 0:
#             a = x
#     return print(f'Miejsce zerowe: {x}')
#
# metoda_bisekcji_while(-10, 10, f)

h = lambda x: np.sqrt(x)
def metoda_punktu_stalego(iterations, function):
    for i in range(iterations+1):
        f = lambda x: function(x)+x
        if f(i) == i:
            return print(f'Miejsce zerowe: {i}')


