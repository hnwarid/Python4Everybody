# Exercise 1: Write a while loop that starts at the last character in the string and
# works its way backwards to the ﬁrst character in the string,
# printing each letter on a separate line, except backwards.

word = input("Enter the word to be iterated backwards: ")
# try:
index = len(word)-1
while index >= 0:
    print(word[index])
    index -= 1
# except ValueError:
#     print("Enter a word")
#     quit()
# except TypeError:
#     print("Type not supported")
#     quit()
# unnecessary since input() function type is a string