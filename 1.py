from matplotlib import pyplot as plt
import numpy as np
import random as rnd


# #Z1
# print(f'{[_ for _ in range(10)]}\nKoniec')


# #Z2
#
# lista = [_ for _ in range(10)]
# lista2 = [_ for _ in range(10)]
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Wykres')
# plt.plot(lista, lista2, 'bo')
# plt.show()


# # Z3
# print('1->10001\n')
# x = 0
# for i in range(1, 10002):
#     x += 1 / i ** 3
# print(f'Standard: {x:.64f}')
# x = np.float32(0)
# for i in range(1, 10002):
#     x += 1 / i ** 3
# print(f'32bit:    {x:.64f}\n')
#
# print('10001->1\n')
# y = 0
# for i in range(10002,0, -1):
#     y += 1 / i ** 3
# print(f'Standard: {y:.64f}')
# y = np.float32(0)
# for i in range(10002,0, -1):
#     y += 1 / i ** 3
# print(f'32bit:    {y:.64f}')


# # Z4
# def silnia(liczba):
#     out = 1
#     for i in range(1, liczba + 1):
#         out *= i
#     return out
#
#
# def fibonacci(docyfry):
#     ciag = [1, 1]
#     while len(ciag) < docyfry:
#         ciag.append((ciag[-1] + ciag[-2]))
#     return print(ciag)
#
#
# fibonacci(10)

# # Z5
#
# def ileNukleotydow(nic: str, nukleotyd: str):
#     A, T, G, C = 0, 0, 0, 0
#     for nuk in nic:
#         if nuk == 'A':
#             A += 1
#         elif nuk == 'T':
#             T += 1
#         elif nuk == 'G':
#             G += 1
#         elif nuk == 'C':
#             C += 1
#     if nukleotyd == 'A':
#         return print(A)
#     elif nukleotyd == 'T':
#         return print(T)
#     elif nukleotyd == 'G':
#         return print(G)
#     elif nukleotyd == 'C':
#         return print(C)
# ileNukleotydow('AATGCCATCGAA', 'A')
