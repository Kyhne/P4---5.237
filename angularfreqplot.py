import numpy as np
import matplotlib.pyplot as plt

n = 7
t = np.linspace(-10,11,1000)
# u = np.piecewise(t, [t>0, t>1, t>2, t>4, t>5, t>7, t>8, t>10, t>11], [lambda t: -t**2+1, 0,lambda t: -(t-3)**2+1, 0, lambda t: -(t-6)**2+1, 0, lambda t: -(t-9)**2+1, 0, lambda t: -(t-12)**2+1 ]) # step funktionen
u = np.piecewise(t, [t>=-10,t>2,t>4], [0, lambda t: -(t-3)**2+1, 0])
# def f(t):
#     return -(t-5)**2-10*t+26

# a = np.linspace(0,100,12000)

# plt.figure(figsize=(12, 6), dpi=100) 
plt.figure(figsize=(9, 6), dpi=100) 


plt.xlim(1,5)
plt.ylim(0,1.1)
plt.plot(t,u, color='b', label='$|\hat{x}_c(\Omega)|$')
plt.xlabel('Angular frequency [rad/s]', fontsize = 14)
plt.ylabel("$|\hat{x}_c(\Omega)|$", fontsize = 14)
# plt.xlim(-n,n)
plt.legend(loc='upper right', fontsize = 14)
# plt.ylim(0,1.1)
x = np.array(["","","","","",'',"","-$\Omega_N$","","$\Omega_N$","","",""])
default_x_ticks = np.arange(-5,12, step=1)
plt.xticks(default_x_ticks, x)

y = np.array(["0","0.2","0.4","0.6","0.8", "1.0"])
default_y_ticks = np.arange(0,1.2, step=0.2)
plt.yticks(default_y_ticks, y)
plt.rc('ytick', labelsize=14)   
plt.rc('xtick', labelsize=14)