import numpy as np
import matplotlib.pyplot as plt


data_input = input("enter the values")

data = np.array(list(map(int, data_input.split())))

plt.figure()
plt.hist(data, bins=[0.5,1.5,2.5,3.5,4.5])

plt.xticks([1,2,3,4,5])
plt.yticks([1,2,3,4,5])

plt.xlabel("Values")
plt.ylabel("frequency")
plt.title("Histogram dynamic")
plt.show()
