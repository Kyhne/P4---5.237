# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 15:11:02 2022

@author: Hazad
"""
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize = (9,6),dpi = 100)
x = np.array([250, 500, 1000, 2000, 4000, 8000])
bone = np.array([0,0,0,0,0,0])
right = np.array([57,61,62,59,62,65])
left = np.array([58,60,57,58,64,63])
normal = np.array([0,0,0,0,0,0])
normal_SPL = np.array([13,8,5,3,-2,20])
default_x_ticks = range(len(x))
plt.ylim(-10,100)
plt.title('Audiogram for a person with a moderately severe hearing loss',fontsize = 16)
plt.xlabel('Frequency [Hz]', fontsize = 14)
plt.ylabel("Hearing level [dB HL]", fontsize = 14)
plt.grid(axis = 'both', linestyle = '-')
plt.gca().invert_yaxis()
# (markers, stemlines, baseline) = plt.stem(default_x_ticks,normal_SPL, 'red' , basefmt="darkblue", use_line_collection=True, markerfmt="o", label = "Right ear")
# plt.xticks(default_x_ticks, x)
# plt.setp(stemlines, visible = False)
# plt.setp(baseline, visible = False)
# plt.setp(stemlines, color="blue", linewidth = 22.2)
# plt.setp(markers, markersize = 8, color = "darkorange")

plt.text(x = 4, y = 15, s = "Normal")
plt.text(x = 4, y = 25, s = "Slight")
plt.text(x = 4, y = 40, s = "Mild")
plt.text(x = 4, y = 55, s = "Moderate")
plt.text(x = 4, y = 70, s = "Mod. severe")
plt.text(x = 4, y = 90, s = "Severe")
plt.text(x = 4, y = 100, s = "Profound")
plt.axhspan(-15, 16, facecolor='yellow', alpha=0.1)
plt.axhspan(16, 26, facecolor='royalblue', alpha=0.1)
plt.axhspan(26, 41, facecolor='blue', alpha=0.2)
plt.axhspan(41, 56, facecolor='darkblue', alpha=0.4)
plt.axhspan(56, 71, facecolor= 'orangered', alpha=0.1)
plt.axhspan(71, 90, facecolor='indianred', alpha=0.2)
plt.axhspan(90, 100, facecolor='firebrick', alpha=0.2)

(markers, stemlines, baseline) = plt.stem(default_x_ticks,right, 'red' , basefmt="darkblue", use_line_collection=True, markerfmt="o", label = "Right ear")
plt.xticks(default_x_ticks, x)
plt.setp(stemlines, visible = False)
plt.setp(baseline, visible = False)
plt.setp(stemlines, color="blue", linewidth = 22.2)
plt.setp(markers, markersize = 8, color = "darkorange")

(markers2, stemlines2, baseline2) = plt.stem(default_x_ticks,left, 'red' , basefmt="red", use_line_collection=True, markerfmt= "x", label = "Left ear")
plt.setp(stemlines2, visible = False)
plt.setp(baseline2, visible = False)
plt.setp(markers2, markersize = 9, color = "deeppink")

(markers5, stemlines5, baseline5) = plt.stem(default_x_ticks,bone, 'red' , basefmt="darkblue", use_line_collection=True, markerfmt = "x", label = "Bone conduction")
plt.setp(stemlines5, visible = False)
plt.setp(baseline5, visible = False)
plt.setp(markers5, markersize = 8, color = "blue", alpha = 0.5)

(markers6, stemlines6, baseline6) = plt.stem(default_x_ticks,normal, 'red' , basefmt="darkblue", use_line_collection=True, markerfmt = "_",label='Normal hearing threshold')
plt.setp(stemlines6, visible = False)
plt.setp(baseline6, visible = False)
plt.setp(markers6, markersize = 25, color = "black")
plt.legend()


(markers3, stemlines3, baseline3) = plt.stem(default_x_ticks,right, 'red' , basefmt="darkblue", use_line_collection=True, markerfmt = "w")
plt.setp(stemlines3, visible = False)
plt.setp(baseline3, visible = False)
plt.setp(markers3, markersize = 6, color = "forestgreen")

(markers4, stemlines4, baseline4) = plt.stem(default_x_ticks,left, 'red' , basefmt="darkblue", use_line_collection=True, markerfmt = "w")
plt.setp(stemlines4, visible = False)
plt.setp(baseline4, visible = False)
plt.setp(markers4, markersize = 6, color = "darkblue")


plt.loglog(basex= 1,basey=1)
plt.show()