import numpy as np
import matplotlib.pyplot as plt

A = np.array([[3, 3], [3, 3]])
transform = lambda x, y: A @ np.array([x, y]).T
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
colors = ['red', 'green', 'blue', 'yellow']

for i, ax in enumerate(axs.flatten()):
    color = colors[i]
    for x in range(-15, 15):
        for y in range(-15, 15):
            p1 = transform(x, y)
            p2 = transform(x + 1, y)
            p3 = transform(x, y + 1)
            p4 = transform(x + 1, y + 1)
            if color == 'red':
                ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, linewidth=2, alpha=0.5)
            elif color == 'green':
                ax.plot([p1[0], p3[0]], [p1[1], p3[1]], color=color, linewidth=2, alpha=0.5)
            elif color == 'blue':
                ax.plot([p2[0], p4[0]], [p2[1], p4[1]], color=color, linewidth=2, alpha=0.5)
            elif color == 'yellow':
                ax.plot([p3[0], p4[0]], [p3[1], p4[1]], color=color, linewidth=2, alpha=0.5)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_xticks(np.arange(-5, 6, 1))
    ax.set_yticks(np.arange(-5, 6, 1))
    ax.grid()

plt.tight_layout()
plt.show()