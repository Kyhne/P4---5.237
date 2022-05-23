import numpy as np
import matplotlib.pyplot as plt

N = np.linspace(1,500,500)

def FFT(N):
    return 3/2*N*np.log2(N)-N/2 #FFT computations

def DFT(N):
    return 2*N**2-N #DFT computations


def plot():
    plt.figure(figsize=(10, 6), dpi=100) 
    plt.grid()
    FFTplot = plt.plot(N, FFT(N), color='b', label=r'$C_{FFT}$')
    DFTplot = plt.plot(N, DFT(N), color='black', label=r'$C_{DFT}$')
    plt.legend((FFTplot, DFTplot))
    plt.ylim(0,6500)
    plt.xlim(0,500)
    plt.xlabel('N', fontsize=13)
    plt.ylabel('Complexity',fontsize=13)
    plt.rc('ytick', labelsize=13)   
    plt.rc('xtick', labelsize=13)
    plt.legend(loc='best', fontsize=15)
    plt.show()
    
plot() # Plot figures