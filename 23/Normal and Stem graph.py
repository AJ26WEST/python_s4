import numpy as np
import matplotlib.pyplot as plt

# Line plot
x = np.arange(0, 10)
y = np.sin(x)
plt.plot(x, y, label="Sine Wave")  # Added label for legend
plt.xlabel("X")
plt.ylabel("Y")
plt.title("NORMAL")
plt.legend()  # Display legend
plt.grid()
plt.show()  # Fixed missing parentheses

# Stem plot
x = np.arange(0, 10)
y = np.sin(x)
plt.stem(x, y, label="Sine Stem")  # Added label for legend
plt.xlabel("X")
plt.ylabel("Y")
plt.title("STEM")
plt.legend()  # Display legend
plt.grid()
plt.show()  # Correctly used parentheses
