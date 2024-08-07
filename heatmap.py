import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)

plt.clf()
heatmap = plt.imshow(data, cmap = "YlGnBu", aspect="auto")
plt.colorbar(heatmap)
plt.title("heatmap example")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.savefig("./heatmap.png")
plt.show()

