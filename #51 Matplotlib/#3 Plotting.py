'''
The plot() function is used to draw points (markers) in a diagram.

By default, the plot() function draws a line from point to point.

The function takes parameters for specifying points in the diagram.

Parameter 1 is an array containing the points on the x-axis.

Parameter 2 is an array containing the points on the y-axis.

If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.
'''


import matplotlib.pyplot as plt

'''
x = [1,8]
y = [3,4]

plt.plot(x,y,"r")
plt.show()
'''

xplot = [1,3,5,8,0,3,6,2,8,9,3]
yplot = [8,2,5,2,8,0,4,6,2,5,2]

# plt.plot(xplot, yplot, "y")
plt.hist2d(xplot, yplot)
plt.show()