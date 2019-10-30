import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.arange(0, 1000, 1)
y = x

fig, ax = plt.subplots()
line, = ax.plot(x, y)

def animate(num, x, y, line):
    line.set_data(x[:num], y[:num])
    return line,

ani = animation.FuncAnimation(fig, animate, fargs=[x, y, line],
                          interval=1, blit=True)
plt.show()
