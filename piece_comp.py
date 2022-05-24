

import matplotlib.pyplot as plt
import numpy as np

c1= 500
c2 = 3000
c3 = 7350
a1 = 1
a2 = 0.2
a3 = 0.7

x1 = np.linspace(0, c1-1, 100)
x = np.linspace(c1, 7350, 1000)

def f1(x):
    return a1 * x1
def f2(x):
    return a2 * x + (c1-a2*c1)
def f3(x):
    return a3 * x + (c1 - a2*c1 + a2*c2 - a3*c2)

print(f3(4000))
print(f3(4500))
print(f3(7350))




y = np.piecewise(x, [x < c2, x >= c2], [lambda x : f2(x), lambda x : f3(x)])


plt.hlines(f2(c1),0,c1,color='grey', linestyle = '--', linewidth = 1)
plt.vlines(c1, ymin=0, ymax=f2(c1), color='grey', linestyle = '--', linewidth = 1)
plt.hlines(f2(c2),0,c2,color='grey', linestyle = '--', linewidth = 1)
plt.vlines(c2, ymin=0, ymax=f2(c2), color='grey', linestyle = '--', linewidth = 1)
plt.hlines(f3(c3),0,c3,color='grey', linestyle = '--', linewidth = 1)
plt.vlines(c3, ymin=0, ymax=f3(c3), color='grey', linestyle = '--', linewidth = 1)

plt.text(c1-100, f2(c1)+10, f'\u03B1\u2081 = {a1}', ha = 'center', va = 'bottom')
plt.text(c2, f2(c2)+10, f'\u03B1\u2082 = {a2}', ha = 'right', va = 'bottom')
plt.text(c3, f3(c3)+10, f'\u03B1\u2083 = {a3}', ha = 'right', va = 'bottom')

plt.text(c1-25, f2(c1)-200, u'I', ha = 'right', va = 'top')
plt.text(c2-25, f2(c2)-200, u'II', ha = 'right', va = 'top')
plt.text(c3-25, f3(c3)-200, u'III', ha = 'right', va = 'top')


plt.plot(x1, f1(x), color = 'b', label = 'Unchanged frequecy')
plt.plot(x, y, color = 'orange', label = 'Frequency lowering')
plt.xlim(0,7350)
plt.ylim(0,5000)
plt.title('Piecewise linear frequency compression')
plt.legend(loc="upper left")
plt.xlabel('$f_{in}$ [Hz]')
plt.ylabel('$f_{out}$ [Hz]')
plt.rcParams['figure.dpi'] = 400
plt.show()
