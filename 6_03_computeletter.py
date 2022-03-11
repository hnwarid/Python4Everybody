# Exercise 3: Encapsulate this code in a function named count, and
# generalize it so that it accepts the string and the letter as arguments.
#
# word = 'banana'
# count = 0
# for letter in word:
# 	if letter == 'a':
# 		count = count + 1
# print(count)

def computeletter(word, letter):
    count = 0
    for iletter in word:
        if iletter == letter:
            count += 1
    return f"Letter \"{letter}\" count = {count}"

word = input("Enter the word: ")
letter = input("Enter the letter: ")

wordvar = computeletter(word, letter)
print(wordvar)
