
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


n = 10
dt = 1.0

fig, ax = plt.subplots()

line, = ax.plot(np.random.rand(n),'ro')
ax.set_ylim(0, 1)


def update(data):
    line.set_ydata(data)
    return line,


def data_gen():
    while True:
        yield np.random.rand(n)

ani = animation.FuncAnimation(fig,
                              update,
                              data_gen,
                              interval=dt * 1000)
plt.show()
