import numpy as np
import matplotlib.pyplot as plt

x_input = input("enter the value for x axis")
y_input = input("enter the value for y axis")

x = np.array(list(map(float, x_input.split())))
y = np.array(list(map(float, y_input.split())))

plt.figure()
plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Line Chart Dynamic")
plt.show()