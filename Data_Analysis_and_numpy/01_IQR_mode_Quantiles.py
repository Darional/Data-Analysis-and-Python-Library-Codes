import numpy as np
import pandas as pd
from scipy import stats

"""
Array = [23, 22, 22, 23, 24, 24, 23, 22, 21, 24, 23]
Sorted Array = [21, 22, 22, 22, 23, 23, 23, 23, 24, 24, 24]

The mean is the sum of all the items divided by the lenght of the array, in this case the sum is 251 **try print(np.sum(data))**
and the lenght is 11. So the mean is: 251/11 = 22.82

The median it's the middle value of the sorted array when the lenght of the array is odd, but if it's even, then the median is the mean
between the 2 middle values. In this case the middle of the array is the sixth value, that means is the value 23

The mode is the most frequently value of an array, in this case is the value 23. In the case that is a tie, scipy handle it returning the lowest
value in the array, for example: if 20 and 23 were in a tie, then stats.mode(data).mode would return 20
"""


data = np.array([23, 22, 22, 23, 24, 24, 23, 22, 21, 24, 23], dtype=np.float64) # Turning the array into an numpy array   

mean = np.mean(data)
median = np.median(data)  
mode_age = stats.mode(data) # this returns an object, to get the value we have to do mode_age.mode
print(f'data: ', data, '\n')
print("Mean: ", round(mean, 2), " ||  Median: ", round(median, 2), " || Mode: ", mode_age.mode) 



"""
Quantiles 

In an usually sorted data, is considered the first quartile (Q1) is the poing below of the 25% of the data. Meanwhile, de third quartile (Q3)
is the point below 75% wich the data falls. The second quartile (Q2) or the median if the mid-point of the data. These values are important
to identify the spread and skewed of the data. 

We can observe the SPREAD with RIC or IQR that's calculated as Q3 - Q1, closer to the value 0, then the data are more tightly clustered, in the
contrary, the data is more spread.

Also, we can see if the data is asymetric, the difference between Q3 - Q2 has to be similar to Q2 - Q1 and we can aproximate the upper and
lower limits to see if there is outliers in a boxplot.
                        Upper Limit = Q3 - 1.5 * RIC
                        Lower Limit = Q1 - 1.5 * RIC
"""

scores = np.array([76, 85, 67, 45, 89, 70, 92, 82])
# Calculating the median
median_w1 = np.median(scores)
median_w2 = np.percentile(scores, 50)
print(f'\nMedian using np.percentile(scores, 50): {median_w2}   ||   Median using np.median(scores): {median_w1}')

# Calculating Q1 and Q3
Q1 = np.percentile(scores, 25)
Q3 = np.percentile(scores, 75)
RIC = Q3 - Q1
print(f'Other quantiles --> Q1: {Q1}   ||   Q3: {Q3}')
print(f'RIC: {RIC}   ||   Q3 - Q2 and Q2 - Q1: {Q3-median_w2} - {median_w2-Q1}  ||  Upper Limit = {Q3-1.5*RIC}  ||  Lower Limit = {Q1 - 1.5*RIC}')
print(f'')


# Detecting Outliers
math_scores = pd.DataFrame({
  'Name': ['Jerome', 'Jessica', 'Jeff', 'Jennifer', 'Jackie', 'Jimmy', 'Joshua', 'Julia'],
  'Score': [56, 13, 54, 48, 49, 100, 62, 55]
})
print(f'Detecting outliers of:\n{math_scores}')
# IQR for scores
Q1 = np.percentile(math_scores['Score'], 25)
Q3 = np.percentile(math_scores['Score'], 75)
IQR_score = Q3 - Q1
print(f'RIC: {IQR_score}   ||  Upper Limit = {Q3-1.5*RIC}  ||  Lower Limit = {Q1 - 1.5*RIC}')
scores = math_scores["Score"]
outliers_scores = scores[(scores < Q1 - 1.5 * IQR_score) | (scores > Q3 + 1.5 * IQR_score)]

print(f'\nThe Outliers values are: \n{outliers_scores}')


"""
Confidence interval

Is a range of values that estimates where the true population parameter (mean, proportion, etc) is likely to fall. It reflects the uncertainty
in using a sample to estimate a population value.
  - The most common 95% CI meaning:
      If we repeated the study many times, 95% of the calculated intervals would contain the true value
  - A CI provides two limits:
    * Lower Limit: minimum plausible value
    * Upper Limit: maximum plausible value

  - The formula is:
                  X ± Z * (σ/sqrt(n))

"""
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)
data = np.random.normal(loc=0.01, scale=0.04, size=120)  # Mean=1%, std=4%

# Basic Parameters
alpha = 0.05  # 99% confidence
n = len(data)
mean = np.mean(data)
std = np.std(data, ddof=1)

# Calculating CI (Using t distribution, σ unknown)
# Let's calculate Z for a 95% of Confidence Interval (CI)
#z = stats.norm.ppf(0.05/2, loc=0, scale=1) # Lower critical z-value for a 95% confidence interval (α=0.05)
t = stats.t.ppf(1-alpha/2, df=n-1)  # t critical value used to build a (1 - alpha)% confidence interval for the mean
error_margin = t *(std / np.sqrt(n))
ci_lower = mean - error_margin
ci_upper = mean + error_margin


print(f"Mean: {mean:.4f}")
print(f"Confidence Interval of 95%: [{ci_lower},{ci_upper}]")

# Graph
plt.figure(figsize=(8,5))
plt.hist(data, bins=20, alpha=0.7, color="skyblue", edgecolor="black")
plt.axvline(mean, color="red", linestyle="--", label="Mean Samples")
plt.axvline(ci_lower, color="green", linestyle="--", label="Lower Limit CI 95%")
plt.axvline(ci_upper, color="green", linestyle="--", label="Upper Limit CI 95%")
plt.title("Confidence Interval of 95% for the mean")
plt.xlabel("Item Production")
plt.ylabel("Frequency")
plt.legend()
plt.show()