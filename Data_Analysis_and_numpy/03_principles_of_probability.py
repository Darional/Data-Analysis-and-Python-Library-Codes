import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Generaing randon uniform numbers between -1 and 1
uniform_data = np.random.uniform(-1, 1, 1000)
normal_data = np.random.normal(loc=0, scale=1, size=1000)

'''
Separated Plots

plt.hist(uniform_data, bins=20, density=True)
plt.title("Uniform Distribution")
plt.show()

plt.hist(normal_data, bins=20, density=True)
plt.title("Normal Distribution")
plt.show()
'''
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
ax[0].hist(uniform_data, bins=20, density=True, color="skyblue", edgecolor="black")
ax[0].set_title("Uniform Distribution")
ax[1].hist(normal_data, bins=20, density=True, color="salmon", edgecolor="black")
ax[1].set_title("Normal Distribution")

# Adjust layout
plt.tight_layout()
plt.show()


# Calculating properties
mean_normal, mean_uniform = np.mean(normal_data), np.mean(uniform_data)
var_normal, var_uniform = np.var(normal_data), np.var(uniform_data)
skew_normal, skew_uniform = skew(normal_data), skew(uniform_data)
kurt_normal, kurt_uniform = kurtosis(normal_data), kurtosis(uniform_data)

print(f"Mean Normal Distribution:     {mean_normal.round(4)}  ||  Uniform: {mean_uniform.round(4)}" )
print(f"Variance Normal Distribution: {var_normal.round(4)}   ||  Uniform: {var_uniform.round(4)}")
print(f"Skew Normal Distribution:     {skew_normal.round(4)}  ||  Uniform: {skew_uniform.round(4)}")
print(f"Kurtosis Normal Distribution: {kurt_normal.round(4)}  ||  Uniform: {kurt_uniform.round(4)}")