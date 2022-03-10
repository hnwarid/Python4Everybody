# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except ValueError:
    print("Error, please enter numeric input")
    quit()
if hours > 40:
    pay = 40 * rate + (hours-40) * rate*1.5
else:
    pay = hours * rate
print(f"Pay: {pay}")
