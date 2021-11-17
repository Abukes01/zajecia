import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import os


class CalkiMetody(object):

    def __init__(self, start, stop, funkcja=lambda x: (np.cos(-x**2/9)+1)-1/200):
        self.a_limit = start
        self.b_limit = stop
        self.x = np.linspace(self.a_limit, self.b_limit, 1000)
        self.f = funkcja
        self.savePlot()


    def savePlot(self):
        if os.path.isfile('savedPlot.png') is False:
            plt.plot(self.x, self.f(self.x))
            plt.xlabel('Ox')
            plt.ylabel('Oy')
            plt.savefig('savedPlot.png')

    def showPlot(self):
        plt.plot(self.x, self.f(self.x))
        plt.xlabel('Ox')
        plt.ylabel('Oy')
        plt.title('f(x)=(x^3)sin(x)')
        plt.show()

    def metodaTrapezow(self):
        run = True
        while run:
            try:
                fragments = int(input('Wprowadź ilość przedziałów\n (Podstawowa: 10000).\n ?>>') or '10000')
                portion = self.b_limit - self.a_limit
                delta_x = portion/fragments
                x_0 = self.a_limit
                x_1 = delta_x
                out = 0
                for i in range(fragments):
                    if x_1 <= self.b_limit:
                        out += ((self.f(x_0) + self.f(x_1)) * (x_1-x_0)) / 2
                        x_0 += delta_x
                        x_1 += delta_x
                run = False
                return print(f"Wartość całkowania funkcji metodą trapezów z {fragments} podziałami wynosi {out}"), self.showPlot()

            except ValueError:
                print('Wprowadzona wartość nie jest poprawną liczbą całkowitą')

    def metodaSimpsona(self):
        run = True
        while run:
            try:
                fragments = int(input('Wprowadź PARZYSTĄ ilość przedziałów\n (Podstawowa: 10000)\n ?>>') or '10000')
                if fragments % 2 == 1:
                    raise ValueError
                portion = self.b_limit-self.a_limit
                delta_x = portion/fragments
                x_0 = self.a_limit
                x_1 = delta_x
                suma_wartosci = self.f(x_0)
                for i in range(fragments):
                    if i % 2 == 0 and (x_1 <= self.b_limit):
                        suma_wartosci += 4 * self.f(x_1)
                        i += 1
                        x_1 += delta_x
                    elif i % 2 == 1 and (x_1 <= self.b_limit):
                        suma_wartosci += 2 * self.f(x_1)
                        i += 1
                        x_1 += delta_x
                    elif i == fragments:
                        suma_wartosci += self.f(x_1)
                out = (delta_x * suma_wartosci)/3
                run = False
                return print(f"Wartość całkowania funkcji metodą Simpsona z {fragments} podziałami wynosi {out}"), self.showPlot()


            except ValueError:
                print('Wprowadzona wartość jest niepoprawna, bądź nie jest liczbą parzystą.')

    def metodaMonteCarlo(self):
        run = True
        while run:
            try:
                total_points = int(input('Wprowadź ilość próbek.\n (Podstawowa: 10000)\n ?>>') or '10000')
                points_above_x = 0
                points_under_x = 0
                h1 = 10
                points_over_x = [(rnd.uniform(self.a_limit, np.pi), rnd.uniform(0, h1)) for i in range(total_points+1)]
                points_below_x = [(rnd.uniform(np.pi, self.b_limit), rnd.uniform(self.f(self.b_limit), 0)) for i in range(total_points+1)]
                for element in points_over_x:
                    if self.f(element[0]) < element[1]:
                        continue
                    else:
                        points_above_x += 1
                for element in points_below_x:
                    if self.f(element[0]) < element[1]:
                        points_under_x += 1
                    else:
                        continue
                integral = (np.pi * h1) * (points_above_x/total_points) + ((self.b_limit - np.pi) * self.f(self.b_limit)) * (points_under_x/total_points)
                run = False
                return print(f"Wartość całkowania funkcji metodą Monte-Carlo z {total_points} punktami wynosi {integral}"), self.showPlot()

            except ValueError:
                print('Wprowadzona wartość nie jest poprawną liczbą całkowitą')




wybor =\
'''
[1] Metoda Trapezów
[2] Metoda Simpsona
[3] Metoda Monte-Carlo
'''

start = int(input('Wprowadź punkt startowy.\n ?>>'))
stop = int(input('Wprowadź punkt końcowy.\n ?>>'))
metody = CalkiMetody(start, stop)
runMain = True
# metody.showPlot()
while runMain:
    print(wybor)
    metoda = input('Wybierz metodę wyliczania całki. (Wprowadź numer w [])\n ?>>')
    if metoda == '1':
        runMain = False
        metody.metodaTrapezow()
    elif metoda == '2':
        runMain = False
        metody.metodaSimpsona()
    elif metoda == '3':
        runMain = False
        metody.metodaMonteCarlo()
    else:
        print('Wybierz poprawną metodę.')
