# Exercise 3: Move the function call back to the bottom
# and move the definition of print_lyrics after the defnition of repeat_lyrics.
# What happens when you run this program?

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

repeat_lyrics()

# the result is still the same as if the definition of repeat_lyrics() is put after print_lyrics()
# because function definition only stores the information for later execution, until the functions themselves is called