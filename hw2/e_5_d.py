'''
Filename: e_5_d.py
Date Created: 10/27/2025
Created by: Archit Jain
Email: architj@uw.edu
Student No: 2426587
Description: Excercise 1-5: (d)
Consider the system of weakly coupled pendulua (equations below).
Both pendula are mounted to a board that is placed on rollers,
so that it can move from side to side, slightly.
 θ1'' = -ω_1^2 * θ1 + ε*(θ2 - θ1)
 θ2'' = -ω_2^2 * θ2 + ε*(θ1 - θ2)
Now, assume that ω1 = 1 and ω2 = 1.5.
Increase ε from 0 to 0.5 (in increments of 0.005),
and compute the eigenvalues of the system of equations.
Plot the two frequencies as a function of ε.
Now plot the difference of the two frequencies against ε.
'''

# Importing libraries
import numpy as np                      # for arrays data storage
import matplotlib.pyplot as plt         # for plotting graphs


# Defining omega constants (Given)
ω_1 = 1
ω_2 = 1.5
ω_1_square = ω_1**2
ω_2_square = ω_2**2

# Create a range for Epsilon (ε) from [0, 0.5] in increment of 0.005
ε = np.arange(0, 0.505, 0.005)

# Initializing two frequency lists to store the frequencies
freq_1 = []
freq_2 = []

# Loop through each ε value to compute and append the frequencies
for epsilon in ε:
    # Define A matrix as [       0          1           0           0
    #                     - (ω_1^2 + ε)     0           ε           0
    #                            0          0           0           1
    #                            ε          0    - (ω_2^2 + ε)      0   ]
    A = np.array([
        [0, 1, 0, 0],
        [-ω_1_square - epsilon, 0, epsilon, 0],
        [0, 0, 0, 1],
        [epsilon, 0, -ω_2_square - epsilon, 0]
    ])
    
    # Computing the the eigenvalues
    eigenvalues = np.linalg.eigvals(A)
    

    # Extract the frequencies from the imaginary part of the eigenvalues
    # By taking the absolute value of the imaginary part to get the positive frequency.
    frequencies = np.abs(eigenvalues.imag)
    
    # There are four eigenvalues, two for each frequency mode.
    # We sort them to consistently track the "lower" and "higher" frequencies.
    unique_frequencies = np.sort(np.unique(frequencies))

    # Appending frequencies to their respectiver lists
    freq_1.append(unique_frequencies[0])
    freq_2.append(unique_frequencies[1])

# Setting plot dimensions 10x10
plt.figure(figsize=(10, 10))

# Plotting the frequencies ω_1 and ω_2
plt.subplot(2, 1, 1)
plt.plot(ε, freq_1, label='Frequency 1 (ω_1)')
plt.plot(ε, freq_2, label='Frequency 2 (ω_2)')
plt.title('Excercise 1-5 (d) : \n\nFrequencies (ω) v/s Epsilon (ε)')
plt.xlabel('Epsilon (ε)')
plt.ylabel('Frequency (ω)')
plt.legend()
plt.grid(True)

# Plotting the difference in frequencies
freq_diff = np.array(freq_2) - np.array(freq_1)

plt.subplot(2, 1, 2)
plt.plot(ε, freq_diff)
plt.title('\nDifference in Frequencies (ω) v/s Epsilon (ε)')
plt.xlabel('Epsilon (ε)')
plt.ylabel('Frequency Difference (ω_2 - ω_1)')
plt.grid(True)

# Display the graph plotted
plt.tight_layout()
plt.show()