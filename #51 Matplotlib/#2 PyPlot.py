'''
import matplotlib.pyplot as plt

a = [1,2,3,4,5,1]
b = [90,87,92,56,94,90]

plt.plot(a , b)
plt.show()
'''
'''
'''
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

print(x)
print(y)

plt.plot(x , y)
plt.show()

# x and y now contain the coordinates to plot the heart shape