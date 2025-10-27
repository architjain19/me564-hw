'''
Filename: e_3_a.py
Date Created: 10/09/2025
Created by: Archit Jain
Email: architj@uw.edu
Student No: 2426587
Description: Excercise 1-3: (a)
Compute the Taylor series expansion by hand for f (x).
For each function, plot f (x) = sin(x)/x
and the three-term expansion (i.e., the first three nonzero terms) from x = -5 to x = 5.
'''

# Importing libraries
import math                         # for math operations
import numpy as np                  # for arrays data storage
import matplotlib.pyplot as plt     # for plotting graphs

# Define the function f(x)
def compute_f(x):
    '''
    A function that computes f(x) = sin(x)/x for different values of x
    and also handles values where x=0 to be used as 1 to avoid singularity errors.
    '''
    return np.where(x == 0, 1, np.sin(x) / x)

# Define the three-term Taylor expansion
def compute_taylor_expansion(x):
    '''
    A function that returns 3-term taylor expansion of f(x) = sin(x)/x
    # P_3(x) = [1 - (x^2/3!) + (x^4/5!)]
    '''
    first_term = 1
    second_term = (x**2) / math.factorial(3)
    third_term = (x**4) / math.factorial(5)
    return first_term - second_term + third_term

# Setting a x array from -5->5 with 100 points from x=-5 to x=5
x_val = np.linspace(-5, 5, 100)

# Calculate y values for f(x)
f_x = compute_f(x_val)
# Calculate the Three-term Taylor expansion
y_val = compute_taylor_expansion(x_val)

# Setting graph dimensions 10x8
plt.figure(figsize=(10, 8))
# Plotting points on graph
plt.plot(x_val, f_x, label='f(x) = sin(x)/x', color='purple')
plt.plot(x_val, y_val, label='Taylor Expansion - Three-term', color='red', linestyle='--')
# Adding title and legends to graph plotted
plt.xlabel('x')
plt.ylabel('y')
plt.title('Excercise 1-3 (a)\nPlot of f(x) and its Three-term Taylor Expansion for function sin(x)/x')
plt.legend()
# Show grid to the plot
plt.grid(True)
# Highlighting the origin lines
plt.axvline(0, color='gray', linestyle='-', linewidth=0.5)
plt.axhline(0, color='gray', linestyle='-', linewidth=0.5)
# Display the graph plotted
plt.show()