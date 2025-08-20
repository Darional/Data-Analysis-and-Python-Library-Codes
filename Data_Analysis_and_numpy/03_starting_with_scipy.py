from scipy import stats
import numpy as np

'''
Simulating data

'''
# loc is the mean of the normal distribution, scale is the spread and size is the population
temp_data = np.random.normal(loc=30, scale=10, size=365)


data = np.random.normal(size=1000)
'''
Skew and Taildness calculations

Skewness:
 - Skewness ≈ 0 → Symmetric distribution.
 - Skewness > 0 → Positive skew (longer right tail).
 - Skewness < 0 → Negative skew (longer left tail).

 Kurtosis (default in SciPy uses Fisher's definition):
 - Kurtosis ≈ 0 → Perfectly normal distribution.
 - Kurtosis > 0 → Leptokurtic: heavier tails, more outliers.
 - Kurtosis < 0 → Platykurtic: lighter tails, fewer outliers.

This helps to detect possible skew and tailness, check 02_standard_distribution_range.py to find the outliers.
'''
print(temp_data)
print(f"for the function np.random.normal(size=1000), the skew parameter is: {stats.skew(data)}")
print(f"for the function np.random.normal(size=1000), the tailedness (outliers) is: {stats.kurtosis(data)}")
