import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


def wavefunc(x, t, x0 = 1):
    # m = omega = hbar = 1
    omega = 1
    hbar = 1
    m = 1
    xc = np.cos(omega*t)*x0
    pc = -m*omega*np.sin(omega*t)*x0
    return (m*omega/(np.pi*hbar))**(0.25)*np.exp(-0.5j/hbar*xc*pc + 1j/hbar*pc*x - m*omega/hbar*(x-xc)**2) 



from matplotlib.animation import FuncAnimation

t = 0
x0 = 10
x = np.linspace(-1.5*x0,1.5*x0,2000)
psi = wavefunc(x,t, x0)

fig = plt.figure()

lines = plt.plot(np.array([x,x,x]).T,
        np.array([psi.real, psi.imag, np.abs(psi)**2]).T)

plt.ylim([-1,1])


N = 100
dt = 2*np.pi/N

fps = 20

def update(i):
    t = dt*i
    
    psi = wavefunc(x,t,x0)

    lines[0].set_ydata(psi.real)
    lines[1].set_ydata(psi.imag)
    lines[2].set_ydata(np.abs(psi))
    return lines


ani = FuncAnimation(fig, update, N, interval = 1000/fps)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

ani.save('coherent.gif', writer = 'imagemagick' , fps = fps)
plt.show()
