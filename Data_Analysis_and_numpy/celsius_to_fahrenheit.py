import numpy as np

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