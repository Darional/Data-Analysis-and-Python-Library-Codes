import numpy as np

# Create a NumPy array of ages
ages = np.array([15, 18, 16, 19, 36, 34, 27, 21, 23, 25])

# Select adults age under 30 years
adults = ages[(ages < 30) & (ages > 18)]
print("Adults:", adults)