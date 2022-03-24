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

words = dict()

for line in fhand:
    for word in line.lower().split():
        if not word.isalpha():
            continue
        words[word] = words.get(word, 0) + 1
# print(words)

wordslist = list()
for word, count in words.items():
    wordslist.append((count, word))

wordslist.sort(reverse=True)
print("This is the most common word in the file:")
for word in wordslist:
    print(word[1], word[0])

