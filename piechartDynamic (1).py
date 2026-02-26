import matplotlib.pyplot as plt

labels_input = input("enter the labels")
sizes_input = input("enter the sizes")


labels = list(map(str, labels_input.split()))
sizes = list(map(int, sizes_input.split()))

plt.pie(sizes,labels=labels)
plt.title("pie chart Dynamic")
plt.show()