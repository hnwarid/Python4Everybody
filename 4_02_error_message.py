# Exercise 2: Move the last line of this program to the top,
# so the function call appears before the definitions.
# Run the program and see what error message you get.

repeat_lyrics()
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

# Traceback (most recent call last):
#   File "4_02_error_message.py", line 5, in <module>
#     repeat_lyrics()
# NameError: name 'repeat_lyrics' is not defined