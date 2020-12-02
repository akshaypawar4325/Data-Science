import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[8,9,10,3,4]
plt.plot(x,y,color="r",marker="*")
plt.show()
#scatterplot
plt.scatter(x,y)
plt.show()
#barplot
plt.bar(x,y)
plt.show()
#histogram plot
plt.hist(x)
plt.show()
#boxplot
plt.boxplot(x)
plt.show()
#violinplot
plt.violinplot(x)
plt.show()
