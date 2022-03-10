# Exercise 7: Rewrite the grade program from the previous chapter using a function called
# computegrade that takes a score as its parameter and returns a grade as a string.
#
# Score   Grade
# >= 0.9    A
# >= 0.8    B
# >= 0.7    C
# >= 0.6    D
#  < 0.6    F
#
# Enter score: 0.95
# A
#
# Enter score: perfect
# Bad score
#

def computegrade(score):
    if score < 0 or score > 1.0:
        return "bad number"
    if score >= 0.9:
        return "A"
    if score >= 0.8:
        return "B"
    if score >= 0.7:
        return "C"
    if score >= 0.6:
        return "D"
    else:
        return "F"

try:
    score_input = float(input("Enter score: "))
except ValueError:
    print("bad score")
    quit()

score_entered = computegrade(score_input)
print(score_entered)