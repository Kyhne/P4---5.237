import matplotlib.pyplot as plt
import numpy as np

y = [0,3,3,8,10,10,10,15,15,15,15,15,16,17,17,17,17,17,20,20,23]
x = np.linspace(0,20,21)


plt.figure(figsize=(20, 10), dpi=100)
plt.ylim(0,23)
plt.xlim(0,20)
plt.xticks(x)
plt.plot(x,y)
plt.ylabel("Accumulated errors", fontsize=30)
plt.xlabel("Sentence number", fontsize=30)
plt.grid()
# plt.savefig("acc_errors")
plt.show()