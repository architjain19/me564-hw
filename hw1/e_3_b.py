'''
Filename: e_3_b.py
Date Created: 10/09/2025
Created by: Archit Jain
Email: architj@uw.edu
Student No: 2426587
Description: Excercise 1-3: (b)
Compute the Taylor series expansion by hand for f (x).
For each function, plot f (x) = (cos(x) - 1)/x
and the three-term expansion (i.e., the first three nonzero terms) from x = -5 to x = 5.
'''

# Importing libraries
import math                         # for math operations
import numpy as np                  # for arrays data storage
import matplotlib.pyplot as plt     # for plotting graphs

# Define the function f(x)
def compute_f(x):
    '''
    A function that computes f(x) = (cos(x) - 1)/x for different values of x
    and also handles values where x=0 to be used as 0
    '''
    if x==0:
        # limit of (cos(x) - 1)/x as x->0 is 0
        return 0
    return (np.cos(x) - 1) / x

# Define the three-term Taylor expansion
def compute_taylor_expansion(x):
    '''
    A function that returns 3-term taylor expansion of f(x) = (cos(x) - 1)/x
    # P_3(x) = [(-x/2) + (x^3/4!) - (x^5/6!)]
    '''
    first_term = -1*x/2
    second_term = (x**3) / math.factorial(4)
    third_term = (x**5) / math.factorial(6)
    return first_term + second_term - third_term

# Setting a x array from -5->5 with 100 points from x=-5 to x=5
x_val = np.linspace(-5, 5, 100)

# Calculate y values for f(x) for each value of x
f_x = [compute_f(val) for val in x_val]
# Calculate the Three-term Taylor expansion
y_val = compute_taylor_expansion(x_val)

# Setting graph dimensions 10x8
plt.figure(figsize=(10, 8))
# Plotting points on graph
plt.plot(x_val, f_x, label='f(x) = (cos(x) - 1)/x', color='purple')
plt.plot(x_val, y_val, label='Taylor Expansion - Three-term', color='red', linestyle='--')
# Adding title and legends to graph plotted
plt.xlabel('x')
plt.ylabel('y')
plt.title('Excercise 1-3 (b)\nPlot of f(x) and its Three-term Taylor Expansion for function (cos(x) - 1)/x')
plt.legend()
# Show grid to the plot
plt.grid(True)
# Highlighting the origin lines
plt.axvline(0, color='gray', linestyle='-', linewidth=0.5)
plt.axhline(0, color='gray', linestyle='-', linewidth=0.5)
# Display the graph plotted
plt.show()