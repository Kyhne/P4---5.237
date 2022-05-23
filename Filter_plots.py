# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 21:36:53 2022

@author: Astrid Uni
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import scipy
import matplotlib.patches as mpatches

def amp_response(w, M):
    return abs(np.sin(w*(M+1)/2))/abs(np.sin(w/2))

def freq_response(w, M):
    return np.exp(-1j*w*M/2)*(np.sin(w*(M+1)/2)/np.sin(w/2))

"""
# Amplitude response plot
w = np.linspace(-np.pi,np.pi,10000)

plt.figure(1)
plt.plot(w,amp_response(w,7))
#plt.ylabel('Amplitude response' abs(W(exp(j np.omega))))
plt.ylabel(r'$|W(\mathrm{e}^{j\omega})|$')
plt.xlabel('$\omega$')
#plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'-$\pi$',r'-$\frac{\pi}{2}$','0',r'$\frac{\pi}{2}$',r'$\pi$'])
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'-$\pi$',r'-$\pi/2$','0',r'$\pi/2$',r'$\pi$'])
plt.arrow(-1,6,0.4,-0.5, width=0.06, facecolor='black', edgecolor='none')
plt.annotate('Main lobe', xy=(-1.6,6.2))
plt.arrow(1.13,3.3,-0,-1.1, width=0.06, facecolor='black', edgecolor='none')
plt.annotate('Peak side lobe', xy=(0.55,3.5))
plt.arrow(1.95,2.7,-0,-1.1, width=0.06, facecolor='black', edgecolor='none')
plt.annotate('Side lobe', xy=(1.5,2.85))
#plt.savefig('Rect_amp.png', dpi=100)
plt.show()
"""
    
"""
#Gain of the rectangular window
h = signal.boxcar(7)
h1 = signal.boxcar(35)
h2 = signal.boxcar(70)

w, freqz = signal.freqz(h)
w1, freqz1 = signal.freqz(h1)
w2, freqz2 = signal.freqz(h2)

freqz = freqz/max(freqz) 
freqz1 = freqz1/max(freqz1)
freqz2 = freqz2/max(freqz2)


plt.figure(2, figsize=(10,4.8))
plt.plot(w, 20 * np.log10(abs(freqz)),label="M=7")
plt.plot(w1, 20 * np.log10(abs(freqz1)),label="M=35")
plt.plot(w2, 20 * np.log10(abs(freqz2)),label="M=70")
plt.axhline(y = -12.75, color = 'grey', linestyle = 'dashed', linewidth=1)
plt.ylim(-80,5)
plt.xlim(0, np.pi)
plt.xticks([0,0.2*np.pi,0.4*np.pi,0.6*np.pi,0.8*np.pi,np.pi],[0,r'$0.2\pi$',r'$0.4\pi$',r'$0.6\pi$',r'$0.8\pi$',r'$\pi$'], fontsize=12)
plt.yticks([0,-13,-20,-40,-60,-80], fontsize=12)
plt.xlabel(r'$\omega$', fontsize=12)
plt.ylabel('Amplitude [dB]', fontsize=12)
plt.legend(fontsize=12)
#plt.savefig('Rect_windows', dpi=100)
plt.show()
"""


"""
#Gain of different windows
h = signal.boxcar(35)
h1 = signal.bartlett(35)
h2 = signal.hanning(35)
h3 = signal.hamming(35)
h4 = signal.blackman(35)

w, freqz = signal.freqz(h)
w1, freqz1 = signal.freqz(h1)
w2, freqz2 = signal.freqz(h2)
w3, freqz3 = signal.freqz(h3)
w4, freqz4 = signal.freqz(h4)

freqz = freqz/max(freqz) 
freqz1 = freqz1/max(freqz1)
freqz2 = freqz2/max(freqz2) 
freqz3 = freqz3/max(freqz3)
freqz4 = freqz4/max(freqz4) 

plt.figure(3)
plt.plot(w, 20 * np.log10(abs(freqz)),label="Rectangular")
plt.plot(w1, 20 * np.log10(abs(freqz1)),label="Rectangular")
plt.plot(w2, 20 * np.log10(abs(freqz2)),label="Rectangular")
plt.plot(w3, 20 * np.log10(abs(freqz3)),label="Rectangular")
plt.plot(w4, 20 * np.log10(abs(freqz4)),label="Rectangular")
plt.show()
"""

"""
#Window functions
plt.figure(4, dpi=100)
plt.plot(signal.boxcar(51), linewidth=0.8, color='tab:blue', label='Rektangulær')
plt.plot([0,0],[0,1], linewidth=0.8, color='tab:blue')
plt.plot([50,50],[0,1], linewidth=0.8, color='tab:blue')
#plt.plot(np.bartlett(51), color='black', label='Bartlett', linewidth=0.8)
#plt.plot(np.hanning(51), color='darkolivegreen', label='Hann', linewidth=0.8)
plt.plot(np.hamming(51), color='gold', label='Hamming', linewidth=0.8)
plt.plot(np.blackman(51), color='tab:orange', label='Blackman', linewidth=0.8)
plt.legend()
plt.ylabel('w[n]')
plt.xlabel('n')
plt.xticks([0,25,50],[0,'M/2','M'])
plt.savefig('Window_functions.png', dpi=100)
plt.show()
"""

"""
#Convolution between window and desired frequency response
#n=200
#M=10
#w = np.linspace(-np.pi,1*np.pi,n)
#w1 = np.linspace(-np.pi,1*np.pi,2*n-1)
#Hd=np.piecewise(w,[abs(w)<0.5*np.pi, abs(w)>0.5*np.pi], [10,0])

#plt.figure(5)
#plt.plot(w1,np.convolve(Hd,freq_response(w,M)))
#plt.plot(w,freq_response(w,M))
#plt.plot(w,1/(2*np.pi)*scipy.integrate(Hd*freq_response(w-t,M)))
#plt.plot(w,Hd)
#plt.show()

theta=np.linspace(-0.7, 3*np.pi+0.7,999)
    

fig, ax = plt.subplots(figsize=(20,4))
plt.plot((4/np.pi)*(((np.sin((2*1-1)*theta))/(2*1-1))+((np.sin((2*2-1)*theta))/(2*2-1))+((np.sin((2*3-1)*theta))/(2*3-1))), color='black', label=r'$H(\mathrm{e}^{j\omega})$')
plt.plot([np.pi*20.5,np.pi*20.5],[1,-1.05], linewidth=1.5, linestyle='dashed', color='grey', label=r'$H_d(\mathrm{e}^{j\omega})$')
plt.plot([np.pi*112.5,np.pi*112.5],[1,-1.05], linewidth=1.5, linestyle='dashed', color='grey')
plt.plot([np.pi*205,np.pi*205],[1,-1.05], linewidth=1.5, linestyle='dashed', color='grey')
plt.plot([np.pi*297,np.pi*297],[1,-1.05], linewidth=1.5, linestyle='dashed', color='grey')
plt.plot([np.pi*20.5,np.pi*112.5],[1,1], linewidth=1.5, linestyle='dashed', color='grey')
plt.plot([np.pi*205,np.pi*297],[1,1], linewidth=1.5, linestyle='dashed', color='grey')
ax.spines['bottom'].set_position(('data', -1.05))
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(axis='y', which='minor', labelsize=0)
ax.tick_params(axis='y', which='major', labelsize=0)
ax.tick_params(axis='x', which='minor', labelsize=20)
ax.tick_params(axis='x', which='major', labelsize=20)
plt.xticks([200,500,800],[0,r'$\pi$',r'$2\pi$'])
#plt.xlabel(r'$\omega$', fontsize=20)
plt.legend(fontsize=20)
plt.text(1085,-1.25,'$\omega$', fontsize = 20)
plt.xlim(-10,1100)
plt.savefig('Convolution.png', dpi=100)
plt.show()
"""

"""
#Squared amplitude response for Butterwoth filter
def ampl_butter(O,Oc,N):
    return 1/(1+((1j*O)/(1j*Oc))**(2*N))

O=np.linspace(0,40,100)

plt.figure(6)
plt.plot(O,ampl_butter(O,12,2))
plt.plot([0,12],[0.5,0.5], linewidth=0.8, linestyle='dashed', color='grey')
plt.plot([12,12],[0.5,0], linewidth=0.8, linestyle='dashed', color='grey')
plt.xticks([12],[r'$\Omega_c$'], fontsize=12)
plt.yticks([0,0.5,1], fontsize=12)
plt.xlim([0,40])
plt.ylim([0,1.05])
plt.xlabel(r'$\Omega$', fontsize=12)
plt.ylabel(r'$|H_c(j\Omega)|^2$', fontsize=12)
#plt.savefig('butter_squared', dpi=100)
plt.show()
"""


#amplitude response for Butterworth filter with varying N
def amp_butter(O,Oc,N):
    return np.sqrt(1/(1+((1j*O)/(1j*Oc))**(2*N)))

O=np.linspace(0,100,1000)
Oc = 15

plt.figure(7)
plt.plot(O,amp_butter(O,Oc,2), label='N=2')
plt.plot(O,amp_butter(O,Oc,4), label='N=4')
plt.plot(O,amp_butter(O,Oc,8), label='N=8')
plt.plot([0,Oc],[1/np.sqrt(2),1/np.sqrt(2)], linewidth=0.8, linestyle='dashed', color='grey')
plt.plot([Oc,Oc],[1/np.sqrt(2),0], linewidth=0.8, linestyle='dashed', color='grey')
plt.xticks([Oc],[r'$\Omega_c$'], fontsize=12)
plt.yticks([0,1/np.sqrt(2),1],[0,r'$\frac{1}{\sqrt{2}}$',1], fontsize=12)
plt.xlim([0,50])
plt.ylim([0,1.05])
plt.xlabel(r'$\Omega$', fontsize=12)
plt.ylabel(r'$|H_c(j\Omega)|$', fontsize=12)
plt.legend(fontsize=12)
plt.savefig('butter_amp', dpi=100)
plt.show()


"""
#Pre-warping
def amp_butter_z(w):
    #return (0.0007378*(1+w**(-1))**6)/((1−1.2686*w**(−1)+0.7051*w**(−2))*(1−1.0106*w**(−1)+0.3583*w**(−2))*(1−0.9044*w**(−1)+0.2155*w**(−2)))
    return (0.0007378*(1+w**(-1))**6)/((1-1.2686*w**(-1)+0.7051*w**(-2))*(1-1.0106*w**(-1)+0.3583*w**(-2))*(1-0.9044*w**(-1)+0.2155*w**(-2)))

w=np.linspace(0,4,999)

plt.figure(8)
#plt.plot(O,20*np.log10(amp_butter(O,Oc,2)), label='H_c(s)')
#plt.plot(O,20*np.log10(amp_butter_z(O,Oc,2)), label='H(z)')
#plt.plot(O,amp_butter(O,Oc,2), label='H_c(s)')
#plt.plot(O,amp_butter_z(w), label='H(z)')
plt.plot(w,amp_butter_z(w))
#plt.xticks([12],[r'$\Omega_c$'])
#plt.yticks([0,1/np.sqrt(2),1],[0,r'$\frac{1}{\sqrt{2}}$',1])
#plt.xlim([0,50])
#plt.ylim([0,1.05])
plt.xlabel(r'$\Omega$')
plt.ylabel(r'$|H_c(j\Omega)|$')
#plt.legend()
#plt.savefig('butter_amp', dpi=100)
plt.show()
"""

"""
plt.figure(9)
plt.plot(abs(0.0031*((1+3*O**(-1)+3*O**(-2)+O**(-3))/(1-2.3614*O**(-1)+1.911*O**(-2)-0.5252*O**(-3)))))
plt.xlim([0,30])
plt.show()
"""