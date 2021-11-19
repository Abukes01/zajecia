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
SIR(3,1,'31')







