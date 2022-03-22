# Exercise 4: Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created,
# look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to
# find who has the most messages and
# print how many messages the person has.
#
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
#
# Enter a file name: mbox.txt
# zqian@umich.edu 195

inputfile = input("Enter a file name: ")

try:
    fhand = open(inputfile)
except FileNotFoundError:
    print("File is not found. Check again.")
    quit()

max_count = None
max_email = None
# min_count = None
# min_email = None
email_data = dict()

for line in fhand:
    if not line.startswith("From "):
        continue
    words = line.strip().lower().split()
    email_data[words[1]] = email_data.get(words[1], 0) + 1

for email, counter in email_data.items():
    if max_count is None or counter > max_count:
        max_count = counter
        max_email = email
# for minimum it is similar:
#     if min_count is None or counter < min_count:
#         min_count = counter
#         min_email = email
print(max_email, max_count)
