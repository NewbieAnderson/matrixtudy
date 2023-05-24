import numpy as np
import matplotlib.pyplot as plt

A = np.array([[3, 1], [2, 3]])
transform = lambda x, y: A @ np.array([x, y]).T

for x in range(-15, 15):
    for y in range(-15, 15):
        p1 = transform(x, y)
        p2 = transform(x + 1, y)
        p3 = transform(x, y + 1)
        p4 = transform(x + 1, y + 1)
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='red', linewidth=2, alpha=0.5)
        plt.plot([p1[0], p3[0]], [p1[1], p3[1]], color='red', linewidth=2, alpha=0.5)
        plt.plot([p2[0], p4[0]], [p2[1], p4[1]], color='red', linewidth=2, alpha=0.5)
        plt.plot([p3[0], p4[0]], [p3[1], p4[1]], color='red', linewidth=2, alpha=0.5)

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xticks(np.arange(-10, 11, 1))
plt.yticks(np.arange(-10, 11, 1))
plt.grid()
plt.show()