'''
Filename: e_2_b.py
Date Created: 10/09/2025
Created by: Archit Jain
Email: architj@uw.edu
Student No: 2426587
Description: Excercise 1-2: (b)
A given mass x of a radioactive element obeys the following differential equation in time:
 ̇x = λx,
where λ is a constant describing the rate of decay.
Plot the solution for an initial condition x(0) = 10
From time t = 0 to t = 5 for λ = -5, -1, 0, 0.01, 0.1.
Please plot these all on the same figure. Include a legend.
'''

# Importing libraries
import numpy as np                  # for arrays data storage
import matplotlib.pyplot as plt     # for plotting graphs

# Define the function to compute x(t)
def compute_x_t(x_0, t, lambda_const):
    '''
    A function that loops and plot for each lambda_const with graph dim 10x8
    '''
    plt.figure(figsize=(10, 8))
    # looping for lambda in given list
    for λ in lambda_const:
        # x(t) = x(0) * e^(λ*t)
        x_t = x_0 * np.exp(λ * t)
        plt.plot(t, x_t, label=f'λ = {λ}')
    return plt

# Given: Initial condition
x_0 = 10

# Setting a time array from 0->5 with 50 points from t=0 to t=5
t = np.linspace(0, 5, 50)

# Setting list for decay constants λ from the given list:
lambda_const = [-5, -1, 0, 0.01, 0.1]

# Compute x(t) and plot them w.r.t t for differnet lambda
plt = compute_x_t(x_0, t, lambda_const)

# Adding legends to graph plotted
plt.xlabel('Time (t)')
plt.ylabel('Mass (x)')
plt.title('Excercise 1-2 (b)\nRadioactive Element Decay for Multiple Decay Constants λ')
plt.legend()
# Show grid to the plot
plt.grid(True)
# Display the graph plotted
plt.show()
