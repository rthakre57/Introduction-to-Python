import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(10,5,200)
y = np.random.normal(10,5,200)
plt.scatter(x,y)
plt.show()

x = np.random.normal(10,5,200)
y = np.random.normal(10,5,200)
plt.scatter(x,y,c='r',s=20)
plt.title("Scatter plot")
plt.xlabel('$x$-axis')
plt.ylabel('$y$-axis')
plt.show()


Output:
https://github.com/rthakre57/Introduction-to-Python/issues/1#issue-2140057825
Figure_1
Figure_2
