# temperature_conversion.py
# Task 3: Temperature Conversion Function

# A function that changes Celsius to Fahrenheit
def convert_temperature(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# Ask the user for the temperature
celsius = float(input("Enter temperature in Celsius: "))

# Call the function
result = convert_temperature(celsius)

# Show the answer with 2 decimal places
print("Temperature in Fahrenheit:", round(result, 2))
