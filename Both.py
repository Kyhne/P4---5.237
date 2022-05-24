

import matplotlib.pyplot as plt
import numpy as np


c = 1500 #cutting area
t = -500 #transpositionsvariable
a = 0.7 #comprssion on the output

x = np.linspace(0, c, 1000)
xd = np.linspace(c, 7350, 1000)
xt = np.linspace(c, 7350, 1000)

def f1(x):
    return x
def f2(xd):
    return xd
def f3(xt):
    return a * (xt + t)

print(f3(c))
print(f3(4000))
print(f3(7350))

plt.plot(x,f1(x), color = 'b', label = 'Unchanged frequency')
plt.plot(xd, f2(xd), color='b', alpha = 0.3, linestyle = '-', label = 'Source Band')
plt.plot(xt, f3(xt), color='orange', label = 'Destination Band')
plt.xlim(0,7350)
plt.ylim(0,7350)
plt.title('Combined')
plt.legend(loc="upper left")
plt.xlabel('$f_{in}$ [Hz]')
plt.ylabel('$f_{out}$ [Hz]')
plt.rcParams['figure.dpi'] = 400
plt.show()