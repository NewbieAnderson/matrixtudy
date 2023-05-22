import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([2, 4])
v2 = np.array([3, 1])
axis_max = max(v1[0], v1[1], v2[0], v2[1])
angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

print(f'angle: {angle} rad, {np.rad2deg(angle)} degree')
plt.arrow(0, 0, v1[0], v1[1], head_width=0.1, head_length=0.1, fc='red', ec='red')
plt.arrow(0, 0, v2[0], v2[1], head_width=0.1, head_length=0.1, fc='blue', ec='blue')
plt.xlim(0, axis_max + 1)
plt.ylim(0, axis_max + 1)
plt.grid()
plt.legend()
plt.show()
