import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import pandas as pd
from math import ceil, floor

# # Z6
# rozklad = stats.norm(20.5, 5.5)
# a = rozklad.cdf(25)
# b = 1-rozklad.cdf(30)
# print(a,b)

# #Z7
# rozklad = stats.norm(164, 6)
# a = rozklad.cdf(160)
# b = rozklad.sf(178)
# c = rozklad.cdf(178)-a
# d = rozklad.sf(183)*100
# print(a,b,c,d, sep='\n')

# #Z8
# rozklad = stats.norm(13.5, 2.5)
# q1 = rozklad.ppf(0.25)
# q2 = rozklad.isf(0.25)
# p = rozklad.ppf(0.9)
# print(q1,q2,p, sep='\n')

# #Z9
# rozklad = stats.norm(0,1)
# a = rozklad.isf(0.25)
# b = rozklad.isf(0.8)
# print(a, b, sep='\n')

# #Z10
# rozklad = stats.norm(100, 14.2)
# a = rozklad.ppf(0.99)
# print(a)

# #Z11
# rozklad = stats.norm(78, 13)
# a = rozklad.sf(79)
# rozklad2 = stats.norm(78, 13/20**0.5)
# b = rozklad2.sf(79)
# print(a, b, sep='\n')

# #Z14
# rozklad = stats.chi2(26)
# a = rozklad.cdf(30)
# print(a)

# Zestaw4

# # Z8
# waga = pd.read_excel('Waga.xlsx', 'Arkusz1', index_col=None, na_values=['NA'])
# q1 = waga.quantile([0.25]).iloc[0, 0]
# q2 = waga.quantile([0.5]).iloc[0, 0]
# q3 = waga.quantile([0.75]).iloc[0, 0]
# odchylenie = waga.iloc[:, 0].std()
# srednia = waga.iloc[:, 0].mean()
# moda = waga.iloc[:, 0].mode()
# rozstep = waga.iloc[:, 0].max() - waga.iloc[:, 0].min()
# rozrzut_srednia = (odchylenie / srednia) * 100
# rmk = q3 - q1
# dist = stats.norm(srednia, odchylenie)
# plt.subplot(1,3,1)
# plt.hist(waga['Waga'], bins=list(range(50,85,5)), rwidth=0.85, density=1)
# plt.plot(np.linspace(50,80), dist.pdf(np.linspace(50,80)))
# plt.subplot(1,3,2)
# plt.hist(waga['Waga'], bins=list(range(50,85,5)), rwidth=0.85)
# plt.subplot(1,3,3)
# plt.hist(waga['Waga'], bins=list(range(50,85,5)), rwidth=0.85, cumulative=1)
# plt.show()


# # Z10
# anty = pd.read_excel('Antybiotyki2.xls', 'Dane 2', index_col=None, na_values=['NA'])
# daneIlosciowe = anty[['Dni hospitalizacji', 'Wiek', 'Temperatura', 'WBC']]
# print(daneIlosciowe)
# # anty.loc[anty.Antybiotyk=='T']
# q2 = daneIlosciowe.quantile([0.5])
# odchylenie = daneIlosciowe.std()
# srednia = daneIlosciowe.mean()
# rozstep = daneIlosciowe.max()-daneIlosciowe.min()
#
# q2_T = daneIlosciowe.loc[anty.Antybiotyk=='T'].quantile([0.5])
# odchylenie_T = daneIlosciowe.loc[anty.Antybiotyk=='T'].std()
# srednia_T = daneIlosciowe.loc[anty.Antybiotyk=='T'].mean()
# rozstep_T = daneIlosciowe.loc[anty.Antybiotyk=='T'].max()-daneIlosciowe.loc[anty.Antybiotyk=='T'].min()
#
# q2_N = daneIlosciowe.loc[anty.Antybiotyk=='N'].quantile([0.5])
# odchylenie_N = daneIlosciowe.loc[anty.Antybiotyk=='N'].std()
# srednia_N = daneIlosciowe.loc[anty.Antybiotyk=='N'].mean()
# rozstep_N = daneIlosciowe.loc[anty.Antybiotyk=='N'].max()-daneIlosciowe.loc[anty.Antybiotyk=='T'].min()
#
# plt.subplot(1,2,1)
# plt.scatter(daneIlosciowe['Temperatura'], daneIlosciowe['WBC'])
# plt.subplot(1,2,2)
# plt.hist(anty['Wiek'], bins=list(range(0,85,10)), rwidth=0.85)
# plt.show()

# ZESTAW 5

# # Z1
# rozklad = stats.norm(0,1)
# a = rozklad.isf(0.1/2)
# b = rozklad.isf(0.05/2)
# c = rozklad.isf(0.01/2)
# print(a,b,c,sep='\n')

# # Z2
# rozklad = stats.norm()
# a = rozklad.isf(0.1/2)
# b = rozklad.isf(0.05/2)
# c = rozklad.isf(0.01/2)
# sr = 125
# odch = 15
# n = 130
# print(f'90% : {sr-a*(odch/np.sqrt(n))} < miu < {sr+a*(odch/np.sqrt(n))}')
# print(f'95% : {sr-b*(odch/np.sqrt(n))} < miu < {sr+b*(odch/np.sqrt(n))}')
# print(f'99% : {sr-c*(odch/np.sqrt(n))} < miu < {sr+c*(odch/np.sqrt(n))}')

# # Z3
# rozklad = stats.t(14)
# z = rozklad.isf(0.01/2)
# print([119-z*(2.1/np.sqrt(15)),119+z*(2.1/np.sqrt(15))])

# # Z4
# # 75 PROCENT pacjentów
# rozklad = stats.norm()
# a = rozklad.isf(0.05/2)
# delta = a*np.sqrt(0.75*0.25/136)
# print([0.75-delta,0.75+delta])

# # Z5
# rozklad = stats.norm()
# a = rozklad.isf(0.05/2)
# odch = 15
# d = 2
# n = (a*odch/d)**2
# print(ceil(n))

