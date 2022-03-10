# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number,
# detect their mistake using try and except and
# print an error message and skip to the next number.
#
count = 0
total = 0

while True:
    number = input("Enter a number: ")
    if number == "done":
        print(f"Total = {total}\nCount = {count}\nAverage = {total/count}")
        break
    try:
        number = float(number)
        count += 1
        total += number
    except ValueError:
        print("Invalid input")


# another way is to use list then use sum() on the list:
# line 8:
# total = []
# line 13:
#         print(f"Total = {sum(total)}\nCount = {count}\nAverage = {sum(total)/count}")
# line 18:
#         total.append(number)
