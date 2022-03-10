# Exercise 2: Write another program that prompts for a list of numbers as above and
# at the end prints out both the maximum and minimum of the numbers instead of the average.

min = None
max = None

while True:
    number = input("Enter a number: ")
    if number == "done":
        print(f"Minimum number = {round(min)}\nMaximum number = {round(max)}")
        break
    try:
        if min is None or float(number) < min:
            min = float(number)
        if max is None or float(number) > max:
            max = float(number)
    except ValueError:
        print("Invalid input")
