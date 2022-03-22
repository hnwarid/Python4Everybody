# Exercise 3: Write a program to read through a mail log,
# build a histogram using a dictionary to
# count how many messages have come from each email address, and
# print the dictionary.
#
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

inputfile = input("Enter file name: ")
try:
    fhand = open(inputfile)
except FileNotFoundError:
    print("File is not found. Check again.")
    quit()

emaildc = dict()

for line in fhand:
    if len(line) == 0 or len(line) < 3:
        continue
    if not line.startswith("From "):
        continue
    words = line.strip().lower().split()
    # print(words[1])
    emaildc[words[1]] = emaildc.get(words[1], 0) + 1
    # print(emaildc)
print(emaildc)
