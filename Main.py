import matplotlib.pyplot as plt
  
# x-axis values
x = [1,2,3,4,5,6,7,8,9,10]
# y-axis values
y = [2,4,5,7,6,8,9,11,12,12]
  
# plotting points as a scatter plot
plt.scatter(x, y, color= "red", 
            marker= ".", s=30)
  
# x-axis label
plt.xlabel('Cell No.')
# frequency label
plt.ylabel('EME')
# plot title
plt.title('EME & Cell - @ Cycle 1')
# showing legend
plt.legend()
  
# function to show the plot
plt.show()