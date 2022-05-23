import numpy as np
import matplotlib.pyplot as plt  
from scipy import signal


# def freqresppeter(omega):
#     return np.abs(0.03178*(1+3*z**(-1)+3*z**(-2)+z**(-3))/(1-1.4590*z**(-1)+0.9104*z**(-2)-0.1978*z**(-3)))
# 
def freqresponse(omega):
    return np.abs((0.02049883518 + 0.06149650554*z**(-1) + 0.06149650554*z**(-2) + 0.02049883518*z**(-3))/(1.717660320 - 3.336062010*z**(-1) + 2.364335021*z**(-2) - 0.5819426497*z**(-3)))

def freqresponse1(omega):
    return np.abs(0.01193416122*(1 + 3*z**(-1) + 3*z**(-2)+1*z**(-3))/(1-1.94221288759*z**(-1)+1.37648578911*z**(-2)-0.33879961184*z**(-3)))

# We use this:

def freqresponseny(omega):
    return np.abs((0.004225599329 + 0.01267679799*z**(-1) + 0.01267679799*z**(-2) + 0.004225599329*z**(-3))/(1.379839977 - 3.258388824*z**(-1) + 2.637062420*z**(-2) - 0.7247087785*z**(-3)))

def freqresponseny1(omega):
    return np.abs(0.003062383609*(1+3*z**(-1) + 3*z**(-2)+1*z**(-3))/(1-2.36142514952*z**(-1)+1.91113640999*z**(-2)-0.52521219168*z**(-3)))

# def cba(omega):
    # return np.angle(0.03178*(1+3*z**(-1)+3*z**(-2)+z**(-3))/(1-1.4590*z**(-1)+0.9104*z**(-2)-0.1978*z**(-3)), deg=False)


plt.figure(figsize=(10,6), dpi = 120)

omega = np.linspace(0, np.pi, 999)
z = np.exp(1j*omega)

# Plot frequency response
# plt.plot(omega, freqresponseny(omega), color = 'b', label = r'$|H(\mathrm{e}^{j\omega})|$')
# plt.plot(omega, freqresponseny1(omega), color = 'b', label = r'$|H(\mathrm{e}^{j\omega})|$')

# plt.xlabel('Frequency', fontsize = 12)
# plt.ylabel('Amplitude', fontsize = 12)
# plt.text(3.11,-0.035,'$\pi$', fontsize = 12)

# # Plot Gain
plt.plot(omega, 20*np.log10(freqresponseny(omega)), color = 'b', label = r'$20\cdot log10(|H\left(\mathrm{e}^{j\omega})|\right)$')
a = [0.32057067893, 1.57079631975]
b = [-3, -45]
plt.xlabel('Frequency', fontsize = 12)
plt.ylabel('Amplitude [dB]', fontsize = 12)
plt.scatter(a,b, marker='x', c = ['black', 'r'])
plt.text(3.1,-156,'$\pi$', fontsize = 12)
plt.ylim(-150,7)
plt.xlim(0,3.4)

plt.vlines(0.32057067893, ymin = -150, ymax = -3, linestyles = 'dashed', color = 'black')
plt.hlines(-3, xmin = 0, xmax = 0.32057067893, linestyles = 'dashed', color = 'black')

plt.vlines(1.57079631975, ymin = -150, ymax = -45, linestyles = 'dashed', color = 'red')
plt.hlines(-45, xmin = 0, xmax = 1.57079631975, linestyles = 'dashed', color = 'red')
plt.text(0.01,-9,'-3dB', fontsize = 12)
plt.text(0.01,-52,'-45dB', fontsize = 12)


# Plot phase response
# sys = signal.TransferFunction([0.004225599329,0.01267679799,0.01267679799,0.004225599329],[1.379839977,-3.258388824,2.637062420,-0.7247087785], dt=0)
# w, mag, phase = signal.dbode(sys)
# w = np.linspace(0,np.pi,100)
# plt.plot(w, phase*np.pi/180, color = 'b', label = r'Arg(H(z))')    # Bode phase plot
# plt.xlabel('Frequency', fontsize = 12)
# plt.ylabel('Phase [rad]', fontsize = 12)
# plt.text(3.115,-5.1,'$\pi$', fontsize = 12)


# plt.xscale('log',basex=10)
# plt.xlim(0,8)
# plt.ylim(1,1.2)
plt.grid()
plt.legend(loc = 'best', fontsize = 12)

plt.show()

# print(transferfunc())

