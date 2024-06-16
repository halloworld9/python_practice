import matplotlib.pyplot as plt
from numpy import sqrt, arange

x = arange(-50, -2, 0.1)
y = sqrt(-x - 2)


plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.plot(x, -y)
plt.axhline(y=0, color="black")
plt.axvline(x=-2, color="gray", linestyle="--")
plt.axvline(color="black")
plt.show()
