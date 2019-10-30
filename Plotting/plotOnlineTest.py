#! /usr/bin python
import numpy as np
import matplotlib.pyplot as plt

plt.ion()
plt.show()
p = []
for i in range(10):
    p+=[i]
    plt.plot(p)
    plt.pause(0.5)
