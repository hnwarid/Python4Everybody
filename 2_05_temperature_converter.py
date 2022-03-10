# Exercise 5: Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit,
# and print out the converted temperature.

celcius_temp = input("Celcius temperature: ")

fahrenheit_temp = (float(celcius_temp) * 9/5) + 32

print(f"Fahrenheit temperature of that is {fahrenheit_temp}")