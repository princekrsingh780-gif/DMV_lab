import numpy as np
import matplotlib.pyplot as plt

data = np.array([1,1,2,2,2,3,3,3,3,4])

plt.figure()
plt.hist(data, bins=[0.5,1.5,2.5,3.5,4.5])
plt.xticks([1,2,3,4])
plt.yticks([1,2,3,4])
plt.xlabel("Values")
plt.ylabel("frequency")
plt.title("Histogram Static")
plt.show()