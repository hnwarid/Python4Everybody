# Exercise 3: Write a program that reads a file and prints the letters in
# decreasing order of frequency. Your program should
# convert all the input to lower case and only
# count the letters a-z. Your program should
# not count spaces, digits, punctuation, or anything other than the letters a-z.
# Find text samples from several\different languages and
# see how letter frequency varies between languages.
# Compare your results with the tables at
# https://wikipedia.org/wiki/Letter_frequencies.

# this is actually word frequency, not letter as 10-3 exercise asked. so...

input_file = input("Enter a file name: ")

try:
    fhand = open(input_file)
except FileNotFoundError:
    print("File not found. Check again.")
    quit()

letters = dict()

for line in fhand:
    for letter in line.lower():
        if not letter.isalpha():
            continue
        letters[letter] = letters.get(letter, 0) + 1
# print(words)

letterlist = list()
for letter, count in letters.items():
    letterlist.append((count, letter))

letterlist.sort(reverse=True)
print("This is the letters in the file ranked from highest:")
for letter in letterlist:
    print(letter[1], letter[0])

# the top 10 result of mbox.txt compared to the wikipedia link:
# rank - wikipedia - file   comparison
#  1        e          e        same
#  2        t          a       +1 rank
#  3        a          i       +2 rank
#  4        o          o        same
#  5        i          t       -3 rank
#  6        n          r       +3 rank
#  7        h          s       +1 rank
#  8        s          c       +4 rank
#  9        r          u       +5 rank
# 10        d          n       -4 rank
