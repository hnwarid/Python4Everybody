# Exercise 3: Sometimes when programmers get bored or want to have a bit of fun,
# they add a harmless Easter Egg to their program.
# Modify the program that prompts the user for the ﬁle name so that
# it prints a funny message when the user types in the exact file name “na na boo boo”.
# The program should behave normally for all other files which exist and don’t exist.
# Here is a sample execution of the program:
#
# python egg.py
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt
#
# python egg.py
# Enter the file name: missing.tyxt
# File cannot be opened: missing.tyxt
#
# python egg.py
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!
#
# We are not encouraging you to put Easter Eggs in your programs; this is just an exercise.

fname = input("Enter the file name: ")
try:
    if fname == "knock knock":
        print("who's there? Come on in!  But first...")
    fhand = open(fname)
except FileNotFoundError:
    print("Enter the correct file name.")
    exit()
line_count = 0
for line in fhand:
    line_count += 1
print(f"There are: {line_count} lines in the file.")
