from matplotlib.pylab import *
from numpy import array, arange, zeros, meshgrid

def SIR(bet, sig, name, function = save):
    Population = 4 * 10 ** 7
    I = 10 ** 4
    S = Population - I
    R = 0
    Beta = bet
    Sigma = sig
    dt = 0.1
    t0 = 0
    te = 8
    t = arange(t0, te, dt)
    N = len(t)
    state = zeros([N, 3])
    state[0, 0] = S
    state[0, 1] = I
    state[0, 2] = R


    def deriviative(state):
        return array([-Beta * state[1] * state[0] / Population,
                      Beta * state[1] * state[0] / Population - Sigma * state[1],
                      Sigma * state[1]])


    def Runge_Kutta(state, dt, deriviative):
        k1 = dt * deriviative(state)
        k2 = dt * deriviative(state + k1 / 2)
        k3 = dt * deriviative(state + k2 / 2)
        k4 = dt * deriviative(state + k3)
        return state + ((1 / 6) * (k1 + (2 * k2) + (2 * k3) + k4))


    for i in range(N - 1):
        state[i + 1] = Runge_Kutta(state[i], dt, deriviative)

    S_end = [state[_, 0] for _ in range(N)]
    I_end = [state[_, 1] for _ in range(N)]
    R_end = [state[_, 2] for _ in range(N)]

    def save():
        subplot(3, 1, 1)
        title(f'Sig:{Sigma} Beta:{Beta}')
        plot(t, S_end, 'r')
        ylabel('S')
        subplot(3, 1, 2)
        plot(t, I_end, 'g')
        ylabel('I')
        subplot(3, 1, 3)
        plot(t, R_end)
        ylabel('R')
        savefig(f'./wykresySIR/{name}.png')
        close()
    return function()

# sigmas = arange(0,3.05,0.05)
# betas = arange(3, 0, -0.05)
# print(betas, sigmas, sep='\n')
# for beta in betas:
#     for sigma in sigmas:
#         print(f'working on {beta}_{sigma}...')
#         SIR(beta, sigma, f'{beta}_{sigma}')
# SIR(3,1,'31')



def HIV(wsp_inf, wsp_nisz, wsp_prod, wsp_dead, wsp_ubPod, podatne, t0, te, dt, T0, I0, V0):
    t = arange(t0, te, dt)
    y = zeros([len(t), 3])
    y[0, 0], y[0, 1], y[0, 2] = I0, T0, V0

    def deriviative(state):
        return array([wsp_inf*state[1]*state[2]/T0 - wsp_nisz*state[0],
                      -(wsp_inf*state[1]*state[2]/T0)-wsp_ubPod*state[1]+podatne,
                      wsp_prod*state[0]-wsp_dead*state[2]])

    def Runge_Kutta(state, dt, deriviative):
        k1 = dt * deriviative(state)
        k2 = dt * deriviative(state + k1 / 2)
        k3 = dt * deriviative(state + k2 / 2)
        k4 = dt * deriviative(state + k3)
        return state + ((1 / 6) * (k1 + (2 * k2) + (2 * k3) + k4))

    for i in range(len(t) - 1):
        y[i + 1] = Runge_Kutta(y[i], dt, deriviative)

    I_end = [y[_, 0] for _ in range(len(t))]
    T_end = [y[_, 1] for _ in range(len(t))]
    V_end = [y[_, 2] for _ in range(len(t))]

    subplot(3,1,1)
    ylabel('I')
    plot(t, I_end, 'r')
    subplot(3,1,2)
    ylabel('T')
    plot(t, T_end, 'g')
    subplot(3,1,3)
    ylabel('V')
    plot(t, V_end, 'b')
    show()

b=1.5
a=1
k=1
u=1
d=0.001
T0=10**9
I0=1
V0=10**2
dt=0.1
t0=0
te=12*30


HIV(b, a, k, u, d, 10**5, t0, te, dt, T0, I0, V0)





