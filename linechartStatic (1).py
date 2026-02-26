import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5])
y = np.array([0,1,2,3,4,5])

plt.figure()
plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Line chart static")
plt.show()