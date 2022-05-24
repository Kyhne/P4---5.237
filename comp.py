

import matplotlib.pyplot as plt
import numpy as np

c1= 500
c2 = 3000
c3 = 7350
a = [1,0.7,0.4,0.2]

x = np.linspace(0, 7350, 1000)

def f1(x):
    return a[0] * x
def f2(x):
    return a[1] * x 
# def f3(x):
#     return a[2] * x
def f4(x):
    return a[3] * x

print(f1(4500))
print(f2(4500))
# print(f3(4500))
print(f4(4500))


plt.plot(x, f1(x), color = 'b', label = f'\u03B1\u2081 = {a[0]}')
plt.plot(x, f2(x), color = 'orange', label = f'\u03B1\u2082 = {a[1]}')
# plt.plot(x, f3(x), color = 'green', label = f'\u03B1\u2083 = {a[2]}')
plt.plot(x, f4(x), color = 'green', label = f'\u03B1\u2083 = {a[3]}')
plt.xlim(0,7350)
plt.ylim(0,7350)
plt.title('Linear frequency compression')
plt.legend(loc="upper left")
plt.xlabel('$f_{in}$ [Hz]')
plt.ylabel('$f_{out}$ [Hz]')
plt.rcParams['figure.dpi'] = 400
plt.show()


