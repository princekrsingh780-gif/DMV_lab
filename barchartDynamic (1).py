import matplotlib.pyplot as plt

x_input = input("enter the x values")
y_input = input("enter y values")

x = list(map(str, x_input.split()))
y = list(map(float, y_input.split()))

plt.bar(x,y)
plt.title("Bar Chart dynamic")
plt.show()