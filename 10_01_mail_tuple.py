# Exercise 1: Revise a previous program as follows:
# Read and parse the “From” lines and
# pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.
# After all the data has been read,
# print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary. Then
# sort the list in reverse order and
# print out the person who has the most commits.
#
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
#
# Enter a file name: mbox.txt
# zqian@umich.edu 195

input_file = input("Enter a file name: ")

try:
    fhand = open(input_file)
except FileNotFoundError:
    print("File is not found. check again.")
    quit()

mail_data = dict()

for line in fhand:
    if not line.startswith("From "):
        continue
    words = line.strip().lower().split()
    mail_data[words[1]] = mail_data.get(words[1], 0) + 1

# print(mail_data)
mail_list = list()

for key, value in mail_data.items():
    mail_list.append((value, key))

# print(mail_list)
mail_list.sort(reverse=True)
print(mail_list[0][1], mail_list[0][0])
