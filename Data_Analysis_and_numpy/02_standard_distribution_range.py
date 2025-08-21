import numpy as np
'''
The function np.ptp returns the difference between the max and the minimum value in an array, in this case is 24 because it's 96-72
'''
scores = np.array([72, 88, 80, 96, 85])
range_scores = np.ptp(scores)
print(f'Range scores: ', range_scores)


'''
The function np.var returns the Variance of each value. The variance is calculated like the sum of (x_i - x_mean)**2 divided by
n. Where x_i is the sample and "n" is the number of samples. the next functions are the hand-made calculus for mean and variance

def mean_manual(array):
    mean = 0
    for value in array:
        mean += value
    mean = mean/len(array)
    return mean

def variance_manual(array, mean):
    total_sum = 0
    for value in array:
        total_sum += (value - mean)**2
    return total_sum/(len(array))

Editor note: The variance calculated corresponds to the population. If we were calculating the variance from a sample, we have to divide
the sum by n - 1 (n is the sample size), this is called the Bessel Correction and helps to avoid the bias arised when estimating
from a reduced sample instead the entire population


##############
# Covariance #
##############
The covariance studies the relation between 2 variables, x and y. It's calculated similar to variance, this means

            Sum( ( x_i - x_mean ) * ( y_i - y_mean ) ) /(N-1)
Where N is a sample from a population.
'''

mean_score = np.mean(scores)
variance_score = np.var(scores)  # if Bessel Correction needed, then you can do np.var(scores, ddof=1)
print(f'\nMean: {mean_score} || Variance: {variance_score}')


'''
The function np.std(scores) returns the standard deviation, the standard deviation is how a data is spread arround the mean, values closer
to zero indicate the data are more tightly clustered. The Hand-Calculation Standard Deviation is the square root of the variance.
Careful with you are working with a sample instead the entire population, in that case you may need apply Bessel Correction.
'''

std_scores = np.std(scores) #  if Bessel Correction needed, then you can do np.std(scores, ddof=1)
print(f"\nStandard deviation of scores: {std_scores}")



'''
Significance test for Pearson's correlation (t-test)
----------------------------------------------------

Formula:
    t = r * sqrt(N - 2) / sqrt(1 - r^2)

Where:
    r  -> correlation coefficient
    N  -> Sample size
    t  -> t-statistic following Student's t-distribution
          with df = N - 2 degrees of freedom

Purpose:
    Tests whether the observed correlation is statistically significant.
    Null hypothesis (H0): r = 0  (no linear relationship)
    Alternative (H1):    r ≠ 0  (linear relationship exists)


Pearson's Correlation
----------------------------------------------------

Formula:
    r_xy = Sum( (x_i - x_mean) * (y_i - y_mean) ) / sqrt( variance(x) * variance(y) )

Where:
    r_xy -> Correlation Coefficient for x and y
        
'''