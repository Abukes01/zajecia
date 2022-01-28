#Praca domowa 2

import matplotlib.pyplot  as plt
from numpy import array,zeros,arange

global b, a, k, u, Npodatne, L, d, E

def z1():

    # ustawiamy dowolną wartość E
    E = 0.2

    # ustawiamy dowolnie (ale bez szaleństw) reszte parametrów
    d = 0.5  # szybkosc apoptozy kom. podatnych
    L = 5  # L szybkosc odtwa. kom. podatnych
    b = 0.25  # szybkosc infekowania kom. podatnych
    a = 1  # szybkosc niszczenia kom. zak.

    def HIV(state, t):
        T = state[0]  # T kom. podatne
        I = state[1]  # I kom. zainfekowane
        dT = L - d * T - (1 - E) * b * T * I
        di = (1 - E) * b * T * I - a * I
        return array([dT, di])


    def Runge_Kutta(y, t, dt, derivative):
        k1 = dt * derivative(y, t)
        k2 = dt * derivative(y + k1 / 2., t + 0.5 * dt)
        k3 = dt * derivative(y + k2 / 2., t + 0.5 * dt)
        k4 = dt * derivative(y + k3, t + dt)
        y_next = y + 1 / 6. * (k1 + 2 * k2 + 2 * k3 + k4)
        return y_next


    To = L / d
    Io = 1

    dt = 0.1
    to = 0
    te = 20
    t = arange(to, te, dt)

    N = len(t)
    y = zeros([N, 2])
    y[0, 0] = To
    y[0, 1] = Io

    for i in range(N - 1):
        y[i + 1] = Runge_Kutta(y[i], t[i], dt, HIV)

    Tt = [y[j, 0] for j in range(N)]
    It = [y[j, 1] for j in range(N)]

    plt.subplot(2, 1, 1)
    plt.plot(t, Tt)
    plt.ylabel("T")
    plt.xlabel("time")
    plt.subplot(2, 1, 2)
    plt.plot(t, It)
    plt.ylabel("I")
    plt.xlabel("time")
    plt.show()

def z2(eps, br, bs, t):
    def Runge_Kutta(y, t, dt, derivative):
        k1 = dt * derivative(y, t)
        k2 = dt * derivative(y + k1 / 2., t + 0.5 * dt)
        k3 = dt * derivative(y + k2 / 2., t + 0.5 * dt)
        k4 = dt * derivative(y + k3, t + dt)
        y_next = y + 1 / 6. * (k1 + 2 * k2 + 2 * k3 + k4)
        return y_next

    def HIV(state, t):
        T = state[0]  # T kom. podatne
        Is = state[1]  # I kom. zainfekowane
        Ir = state[2]  # ilość aktywnego wirusa
        dT = L - d*T - ((1-E)*bs*Is + br*Ir)*T
        dIs = (1-E)*(1-M)*bs*Is*T - a*Is
        dIr = br*T*Ir - a*Ir + (1-E)*M*bs*Is*T
        return array([dT, dIs, dIr])

    # nowe parametry w tym modelu
    bs = bs # współczynnik infekcji komórek nieordpornych
    br = br # współczynnik infekcji komórek odpornych
    M = 10 ** (-5) # współczynnik mutacji wirusa

    # epsilon będziemy jeszcze zmieniać (od 0 do 1)
    E = eps

    # reszta tak jak wcześniej
    d = 0.5  # szybkosc apoptozy kom. podatnych
    L = 5  # L szybkosc odtwa. kom. podatnych
    a = 1  # szybkosc niszczenia kom. zak.

    stabilne = M / (1 - (br / bs))
    To = L / d
    Io = 1
    Iro = 0  # na początku nie mamy odpornych wirusów

    dt = 0.1
    to = 0
    te = t
    t = arange(to, te, dt)
    N = len(t)
    y = zeros([N, 3])
    y[0, 0] = To
    y[0, 1] = Io
    y[0, 2] = Iro

    for i in range(N - 1):
        y[i + 1] = Runge_Kutta(y[i], t[i], dt, HIV)

    Tt = [y[j, 0] for j in range(N)]
    Ist = [y[j, 1] for j in range(N)]
    Irt = [y[j, 2] for j in range(N)]


    plt.subplot(3, 1, 1)
    plt.plot(t, Tt)
    plt.ylabel("T")
    plt.xlabel("time")
    plt.subplot(3, 1, 2)
    plt.plot(t, Ist)
    plt.ylabel("Is")
    plt.xlabel("time")
    plt.subplot(3, 1, 3)
    plt.plot(t, Irt)
    plt.ylabel("Ir")
    plt.xlabel("time")
    plt.show()

    # na ten ostatni wykres będziemy patrzeć dokładniej
    plt.plot(t, Irt)
    plt.ylabel("Ir")
    plt.xlabel("time")
    plt.show()

    plt.axhline(y=stabilne, color='r', linestyle='-')
    plt.show()

#8
z2(0.9, 0.24, 0.25, 30)
z2(0.5, 0.24, 0.25, 30)
z2(0.1, 0.24, 0.25, 30)
#7
z2(0.9, 0.24, 0.2, 30)
#9
z2(0, 0.24, 0.25, 200)

