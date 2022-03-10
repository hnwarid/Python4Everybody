# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate):
    if hours > 40:
        pay = 40 * rate + (hours-40)*1.5 * rate
    else:
        pay = hours * rate
    return pay


try:
    hour_input = float(input("Enter Hours: "))
    rate_input = float(input("Enter Rate: "))
except ValueError:
    print("Error, please enter numeric input")
    quit()

payment = computepay(hour_input, rate_input)
print(f"Pay: {payment}")
