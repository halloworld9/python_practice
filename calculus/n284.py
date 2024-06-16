import matplotlib.pyplot as plt
from numpy import sin, arange, pi

x = arange(0, pi*2, 0.001)
y = sin(x)

plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y, label=r"y(t) = sin(x)")
plt.plot(x, 10*y, label=r"y(t) = 10sin(x)")
plt.plot( x, -2 * y, label=r"y(t) = -2sin(x)")
plt.axhline(y=0, color="black")
plt.legend(fontsize=10)
plt.axvline(color="black")
plt.show()
