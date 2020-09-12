import matplotlib.pyplot as plt
from numpy import linspace
from numpy import log
from numpy import log10

x = linspace(0, 3, 1000)
y1 = x - 1
y2 = log10(x)
y3 = log2(x)
y4 = log(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
