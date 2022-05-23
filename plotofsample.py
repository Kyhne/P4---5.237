import numpy as np
import matplotlib.pyplot as plt


# t = np.linspace(-4.01,4.01,500)
t = np.linspace(-4,4, 9)
u = np.piecewise(t, [t>=-4], [-t**3+4*t**2+3*t+4]) # step funktionen
print(u)
def f(t):
    return -t**3+4*t**2+3*t+4

plt.figure(figsize=(9, 6), dpi=100) 
# plt.plot(t,f(t), color='b', label='$x_c(t)$')
# plt.xlabel('t [s]')
# plt.ylabel("$x_c(t)$")


(markers, stemlines, baseline) = plt.stem(t,u, 'b' , basefmt="white", use_line_collection=True,markerfmt = "o", bottom=0, label="$x_s[n]$")
plt.legend(loc='best', fontsize = 14)
# plt.plot(t,f(t), color = 'b', label = '$x_c(t)$')
plt.legend(loc='best', fontsize = 14)
# plt.ylim(-2,130)
plt.setp(stemlines, color="blue", linewidth = 1)
plt.setp(markers, markersize = 9, color = "b")
plt.setp(baseline, visible=False, color = 'b', linewidth = 3)
plt.ylim(0,130)
# plt.xlabel('n')
# plt.ylabel("$x_s[n]$")
plt.xlabel('n', size = 14)
plt.ylabel("$x_s[n]$", size = 14)

x = np.array(["-4","-3","-2","-1",'0','1','2','3','4','5'])
default_x_ticks = np.arange(-4,5, step=1)
plt.xticks(default_x_ticks, x)

# y = np.array(["0","","","","", "$2\pi/T$"])
# default_y_ticks = np.arange(0,1.2, step=0.2)
# plt.yticks(default_y_ticks, y)
plt.rc('ytick', labelsize=14)   
plt.rc('xtick', labelsize=14)
