import matplotlib.pyplot as plt
import numpy as np
import seaborn

plt.figure(figsize=(10, 6), dpi=100) 

circle1 = plt.Circle((0, 0), 1, color='black', fill=False)
u = np
fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()
plt.xlim(-1.5,1.5)
plt.ylim(-1.01,1.11)
ax.add_patch(circle1)
plt.rcParams['figure.dpi'] = 180 # dpi for speed/quality
plt.rcParams['figure.figsize'] = 6,4
real = [np.exp((1j*np.pi/6)*(2*k+3-1)).real for k in range(0,6)]
imag = [np.exp((1j*np.pi/6)*(2*k+3-1)).imag for k in range(0,6)]
names = ['$s_0$', '$s_1$', '$s_2$', '$s_3$', '$s_4$', '$s_5$'] 

linex = [0, 0.6]
liney = [0, 0.80]
ax.plot(linex,liney, color = 'black')
plt.text(0.08, 0.3, '$\Omega_c$')

ax.scatter(real,imag, marker = 'x')
ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_color('grey')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.arrow(1.5, 0, 0.001, 0, color="black", clip_on=False, head_width=0.06, head_length=0.045)
plt.arrow(0, 1.1, 0, 0.001, color="black", clip_on=False, head_width=0.045, head_length=0.06)
plt.xlabel(r'$\sigma$', x=0.98, fontsize = 9)
plt.ylabel(r'$j\Omega$', rotation = 0, y=0.945, fontsize = 9)
ax.yaxis.set_label_coords(0.53,0.97)

for i, txt in enumerate(names):
    ax.annotate(txt, (real[i], imag[i]), xycoords = 'data')

plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False,
    left = False,
    labelleft = False) # labels along the bottom edge are off

