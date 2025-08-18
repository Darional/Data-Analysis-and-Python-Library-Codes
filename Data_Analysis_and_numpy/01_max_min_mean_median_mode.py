import numpy as np
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