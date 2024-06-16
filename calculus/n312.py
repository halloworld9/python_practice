import matplotlib.pyplot as plt
from numpy import arccos, arange

x = arange(-1, 1, 0.0001)
y = arccos(x)


plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.axhline(y=0, color="black")
plt.legend(fontsize=10)
plt.axvline(color="black")
plt.show()
