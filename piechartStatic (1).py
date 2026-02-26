import matplotlib.pyplot as plt

labels ='Apple', 'Mango','Banana','Grapes','Orange'
sizes = [12,45,65,56,34]

plt.pie(sizes,labels=labels)
plt.title("pie chart static")
plt.show()