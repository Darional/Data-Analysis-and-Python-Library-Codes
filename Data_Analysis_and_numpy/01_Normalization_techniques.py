import pandas as pd
import numpy as np
'''
Data Normalization

Is a process that brings your data into a common format, allowing fair and unbiased comparisons. If datasets are in various scale of units,
certain data elements may unfairly dominate de analysis. By adjusting these differences, data normalization ensures all data pieces stand
on a equal footing for comparative evaluations, no matter their original scale or unit. This prevents favor towards specific data as a 
result of their scale or units, promotnig accuracy and fairness in data analysis.


It is commonly used when the data will be used in machine learning models, especially those sensitive to feature scales. However, if the goal
is exploratory data analysis (EDA) or statistical modeling where the original scale and distribution are important, normalization is usually
not recommended, since it can distort meaningful information.
'''

df = pd.DataFrame({
    "Space Explorer": ['Spock', 'Kirk', 'McCoy', 'Scotty'], # Shotout to CodeSignal
    "Height": [183, 178, 170, 178]
})
print(f'Data Without Normalization: \n {df}')

print('\n')
print("###################################################")
print("#                                                 #")
print("#            Min-Max Normalization                #")
print("#                                                 #")
print("###################################################")

''' This rescales the feature in values between 0 and 1. The expression is 

                    x_new = (x - x_min) / (x_max - x_min) 
    Where:
        - x_min: Is the minimum value of the data
        - x_max: Is the maximum value of the data
        - x    : Is the value to rescale
        - x_new: Is the new value
'''
# Using Numpy Functions
df_min_max_normalizated = (df['Height'] - np.min(df["Height"])) / (np.max(df["Height"]) - np.min(df["Height"]))
print(f'\nMin-Max Normalization: \n {df_min_max_normalizated}')







print('\n\n')
print("###################################################")
print("#                                                 #")
print("#            Z-Score Normalization                #")
print("#                                                 #")
print("###################################################")

''' This transforms data to have a mean of 0 and standard devitation of 1. The expression is 

                    z = (x - μ) / σ
    Where:
        - μ        : Is the mean of the data
        - σ (Sigma): Is the Standard Deviation
        - x        : Is the value to transform
        - z        : Is the new value
'''
# Using Pandas functions
df_z_normalization = (df["Height"] - df["Height"].mean()) / df["Height"].std()
print(f'\nZ Normalization: \n{df_z_normalization}')