import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.randint(50, size=100)
y = np.random.randint(50, size=100)
colors = np.random.randint(50, size=100)
sizes = 10 * np.random.randint(20, size=100)

# Scatter plot
plt.scatter(x, y, s=sizes, c=colors, cmap="nipy_spectral", alpha=0.5)
plt.colorbar()
plt.show()
