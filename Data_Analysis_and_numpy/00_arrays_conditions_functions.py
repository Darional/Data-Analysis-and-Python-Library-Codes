import numpy as np

'''
Functions to create arrays and matrixes
'''
ages = np.zeros((2, 5))  # Create an array with zeros
ages = np.ones((1, 5))  # Create an array with ones
ages = np.empty((2, 2))  # Create an array with none, can have aleatory values depending on the memory state.
ages = np.arange(4)  # Create an 1D array with sorted values
ages = np.arange(1,10,2) # Also create 1D array, but with an start, end and step defined
ages = np.linspace(1,10, num=5)  # Generates "num" values equally spaced between start and stop 
ages = np.identity(n=3)  # Creates an n x n identity matrix 
ages = np.full((4, 9), 3.5)  # Creates a 4x9 matrix full with the value 3.5 
rng = np.random.default_rng()  # instance of an random generator
ages = rng.integers(5, size=(2, 4))  # generating a 2 x 4 matrix with values bewteen 0 to 4

# Create a NumPy array of ages
ages = np.array([15, 18, 16, 19, 36, 34, 27, 21, 23, 25])
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 3, 6, 8, 1], dtype=int)
# Can concatenate 2 arrays
c = np.concat((a, b))

# Select adults age under 30 years
adults = ages[(ages < 30) & (ages > 18)]
print("Adults:", adults)


'''
Working with arrays and creating functions to modify arrays
'''

# Array of temperatures in Celsius for 5 consecutive days
temperatures_c = np.array([20.5, 25.3, 19.6, 22.7, 24.1])

# TODO: Write a function to convert temperatures from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

# TODO: Apply the function to the temperatures_c array and transform them to Fahrenheit scale
fahrenheit_values = np.vectorize(celsius_to_fahrenheit)
temperatures_f = fahrenheit_values(temperatures_c)

print("Temperatures in Celsius: ", temperatures_c)
# TODO: Print the transformed Fahrenheit temperatures
print("Temperatures Fahrenheit: ", temperatures_f)


'''
Dimensions, shape, size, reshape, transpose of arrays
'''

arr_ejemplo = np.array([[[0, 1, 2, 3],[4, 5, 6, 7]],
                        [[0, 1, 2, 3],[4, 5, 6, 7]],
                        [[0 ,1 ,2, 3],[4, 5, 6, 7]]])
print(f'\n\n\n example array: \n{arr_ejemplo}')
print(f'Shape: {arr_ejemplo.shape}   ||   Size: {arr_ejemplo.size}   ||   Dimension: {arr_ejemplo.ndim}\n')

a = np.arange(6)
a_reshaped = a.reshape(3,2)
print(f'Example array: {a}   ||  Reshaped Array: {a_reshaped}')
print(f'Transpose a_reshaped (a_reshaped.transpose()): {a_reshaped.transpose()}')