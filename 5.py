from matplotlib.pylab import *
from numpy import array, arange, zeros

def metodyEulera():
    k = 2
    m = 1


    def oscillator(state,t):
        global k, m
        v = state[1]
        a = -k / m * state[0]
        return array([v, a])


    # def euler(y, t, dt, deriviative):
    #     y_next = y+deriviative(y,t) * dt
    #     return y_next

    def euler(y, t, dt, deriviative):
        y_next = y + (deriviative(y,t)+deriviative(y+deriviative(y,t)*dt, t+dt))*dt/2
        return y_next

    x0 = 10
    v0 = 0
    dt = 0.05
    t0 = 0
    te = 40
    t = arange(t0, te, dt)
    N = len(t)
    y = zeros([N, 2])
    y[0, 0] = x0
    y[0, 1] = v0

    for i in range(N - 1):
        y[i + 1] = euler(y[i], t[i], dt, oscillator)

    pos = [y[_,0] for _ in range(N)]
    vel = [y[_,1] for _ in range(N)]
    E_tot= [k*pos[i]**2/2 + m*vel[i]**2/2 for i in range(N)]
    subplot(3,1,1)
    plot(t, pos)
    ylabel('x')
    xlabel('t')
    subplot(3,1,2)
    plot(t,vel)
    ylabel('v')
    xlabel('t')
    subplot(3,1,3)
    plot(t,E_tot)
    ylabel('E_tot')
    show()

