'''
Filename: e_4_a.py
Date Created: 10/09/2025
Created by: Archit Jain
Email: architj@uw.edu
Student No: 2426587
Description: Excercise 1-4: (a)
Please compute an analytic expression, by hand,
for the real and imaginary parts of the following complex functions.
Please also plot these for t = 0 : .01 : 10 where f (t) = e^it
'''

# Importing libraries
import numpy as np                  # for arrays data storage
import matplotlib.pyplot as plt     # for plotting graphs

# Setting a range for time from 0->10.01 with interval step size of 0.01
t = np.arange(0, 10.01, 0.01)

# Calculate the real and imaginary parts as f(t) = e^(i*t) = (cos(t)) + i(sin(t))
real_part = np.cos(t)
imaginary_part = np.sin(t)

# Setting graph dimensions 10x8
plt.figure(figsize=(10, 8))
# Plotting the real part on graph
plt.plot(t, real_part, label='Real Part (cos(t))', color='red')
# Plotting the imaginary part on graph
plt.plot(t, imaginary_part, label='Imaginary Part (sin(t))', color='blue', linestyle='--')

# Adding title and legends to graph plotted
plt.xlabel('t')
plt.ylabel('Value')
plt.title('Excercise 1-4 (a)\nPlot of Real and Imaginary Parts of function f(x) = e^(it)')
plt.legend()
# Show grid to the plot
plt.grid(True)
# Display the graph plotted
plt.show()