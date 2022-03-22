# Exercise 1: Download a copy of the ﬁle www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and
# stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can
# use the in operator as a fast way to check whether a string is in the dictionary.
try:
    fhand = open("words.txt")
except FileNotFoundError:
    print("File not found. Check again.")
    quit()

words_dc = dict()

for line in fhand:
    if len(line) != 0:
        words = line.split(" ")
    for word in words:
        if word.isalpha():
            if word not in words_dc.keys():
                words_dc[word] = 1
            else:
                words_dc[word] += 1

for key, value in words_dc.items():
    print(key, "=", value)

print(words_dc)
