#Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes.
#Some marks will be given for making the plot look nice.
#Author: Andrea Stanicic

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,4])
ypoints = np.array([0,4])
zpoints = np.array([0,4])

plt.plot(xpoints, ypoints, zpoints)
plt.show()


