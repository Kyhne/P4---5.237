import numpy as np
import matplotlib.pyplot as plt
import seaborn
from matplotlib.ticker import MaxNLocator
from scipy import signal

m = np.linspace(-4,4,9)
# u = np.piecewise(m, [m>=0, m<0], [1, 0]) # step funktionen
u = signal.unit_impulse(9,4) # enheds impuls

fig, ax = plt.subplots()

ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_color('grey')
plt.rcParams['axes.linewidth'] = 0.8
seaborn.despine(ax=ax, offset=-19) # plcering af x akse
(markers, stemlines, baseline) = plt.stem(m,u, 'black' , basefmt="white", use_line_collection=True, bottom=0, markerfmt=None)
plt.setp(stemlines, color="black", linewidth = 2.2)
plt.setp(markers, markersize = 7, color = "black")
plt.setp(baseline, visible=False)

ax.spines['left'].set_position('center')
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
plt.arrow(4.4, 0.001, 0.001, 0, width=0.000015, color="black", clip_on=False, head_width=0.06, head_length=0.18)
plt.arrow(0, 1.5, 0, 0.001, width=0.000015, color="black", clip_on=False, head_width=0.18, head_length=0.06)
plt.rcParams['figure.figsize'] = 12,5.5

xticks = ax.yaxis.get_major_ticks()  #fjern dobbelt 0 
xticks[1].label1.set_visible(False)

ax.tick_params(axis='both', which='major', labelsize=12) #gør tallene større på akserne

plt.xlabel(r'$n$', x=0.99, fontsize = 14)
plt.ylabel(r'$\delta[n]$', rotation = 0, y=0.94, fontsize = 14)
plt.ylim(-0.1,1.5)
plt.rcParams['figure.dpi'] = 180 # dpi for speed/quality
plt.show()