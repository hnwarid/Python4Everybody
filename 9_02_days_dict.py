# Exercise 2: Write a program that categorizes each mail message
# by which day of the week the commit was done. To do this
# look for lines that start with “From”, then
# look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).
#
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#
# Sample Execution:
#
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

try:
    fhand = open("mbox-short.txt")
except FileNotFoundError:
    print("File not found, check again.")

daysdc = dict()

daylist = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    # count+= 1
    if len(words) == 0 or len(words) < 3:
        continue
    if words[0] != 'From':
        continue
    if line.startswith('From') and words[2] not in daylist:
        continue
    # print(words[2])
    daysdc[words[2]] = daysdc.get(words[2], 0) + 1
print(daysdc)
