# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     words = line.split()
#     # print('Debug:', words)
#     if len(words) == 0 : continue
#     if words[0] != 'From' : continue
#     print(words[2])
#
# Exercise 2: Figure out which line of the above program is still not properly guarded.
# See if you can construct a text file which causes the program to fail and then
# modify the program so that the line is properly guarded and
# test it to make sure it handles your new text file.

# The line that is not properly guarded is line 7,
# where we can encounter a line that contains "From"
# but then nothing else, which results in IndexError.
# See line 66 of the 8_02_mbox-short-mod.txt file about this.
# Also if the second word is not the name of the day it will ge printed,
# so we can guard it with a list of the name of days
# then check the lines whether contains it. See the line 67 about this.

fhand = open('8_02_mbox-short-mod.txt')
# count = 0
daylist = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    # count+= 1
    if len(words) == 0 or len(words) < 3: continue
    if words[0] != 'From': continue
    if line.startswith('From') and words[2] not in daylist: continue
    # print(count)
    print(words[2])
