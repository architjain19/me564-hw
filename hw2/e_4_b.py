'''
Filename: e_4_b.py
Date Created: 10/27/2025
Created by: Archit Jain
Email: architj@uw.edu
Student No: 2426587
Description: Excercise 1-4: (b)
For the following ODE as a system of first order ODEs:
 x^(3) + 2 ̈x - ̇x - 2x = 0
with condition A) x(0) = 1; ̇x(0) =  1; ̈x(0) = 1
 and condition B) x(0) = 1; ̇x(0) = -1; ̈x(0) = 1
Please plot the response for t ∈ [0, 10] using a Runge-Kutta 4th order integrator
for each of these initial conditions.
'''

# Importing libraries
import numpy as np                      # for arrays data storage
import matplotlib.pyplot as plt         # for plotting graphs
from scipy.integrate import solve_ivp   # for Runge-Kutta solver

# Define the function to compute system of 1st order ODEs
def ode_system(t, y):
    '''
    A function that returns ODE system for "solve_ivp" method
    for  following inputs -> independent variable time (t) and dependent variable state vector (y)
    '''
    # For x''' = 2x + x' - 2x'' -> Lets assume, y1 = x; y2 = x'; y3 = x''
    y1, y2, y3 = y

    # y1' = y2 = x'
    dy1_dt = y2
    
    # y2' = x''
    dy2_dt = y3
    
    # y3' = y2'' = x''' = 2x + x' - 2x'' = 2*y1 + y2 - 2*y3
    dy3_dt = 2*y1 + y2 - 2*y3
    
    return [dy1_dt, dy2_dt, dy3_dt]

# Setting the time interval over which ODE will be solved
t = (0, 10)
# Setting a time array of 1k evenly spaced time points between 0 -> 10
t_arr = np.linspace(t[0], t[1], 1000)

# A) Initial Condition:
# x(0)   = 1
# x'(0)  = 1
# x''(0) = 1
initial_conditions_a = [1, 1, 1]
res_a = solve_ivp(ode_system, t, initial_conditions_a, t_eval=t_arr, method='RK45')

# B) Initial Condition:
# x(0)   = 1
# x'(0)  = -1
# x''(0) = 1
initial_conditions_b = [1, -1, 1]
res_b = solve_ivp(ode_system, t, initial_conditions_b, t_eval=t_arr, method='RK45')

# Setting graph plotting dimensions 10x10
plt.figure(figsize=(10, 10))

# Plot for condition A:
plt.subplot(3, 2, 1)
plt.plot(res_a.t, res_a.y[0], label='x(t)', color='red')
plt.title('Excercise 1-4 : Condition A\nFor x(0) = 1, x\'(0) = 1, x\'\'(0) = 1')
plt.xlabel('Time (t)')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)

plt.subplot(3, 2, 3)
plt.plot(res_a.t, res_a.y[1], label="x'(t)", color='green')
plt.xlabel('Time (t)')
plt.ylabel('x\'(t)')
plt.legend()
plt.grid(True)

plt.subplot(3, 2, 5)
plt.plot(res_a.t, res_a.y[2], label="x''(t)", color='blue')
plt.xlabel('Time (t)')
plt.ylabel('x\'\'(t)')
plt.legend()
plt.grid(True)

# Plot for condition B:
plt.subplot(3, 2, 2)
plt.plot(res_b.t, res_b.y[0], label='x(t)', color='red')
plt.title('Excercise 1-4 : Condition B\nFor x(0) = 1, x\'(0) = -1, x\'\'(0) = 1')
plt.xlabel('Time (t)')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)

plt.subplot(3, 2, 4)
plt.plot(res_b.t, res_b.y[1], label="x'(t)", color='green')
plt.xlabel('Time (t)')
plt.ylabel('x\'(t)')
plt.legend()
plt.grid(True)

plt.subplot(3, 2, 6)
plt.plot(res_b.t, res_b.y[2], label="x''(t)", color='blue')
plt.xlabel('Time (t)')
plt.ylabel('x\'\'(t)')
plt.legend()
plt.grid(True)

# Display the graph plotted
plt.tight_layout()
plt.show()
