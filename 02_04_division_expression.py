# Exercise 4: Assume that we execute the following assignment statements:
#
# width = 17
# height = 12.0
#
# For each of the following expressions, write the value of the expression and the
# type (of the value of the expression).
#     1. width//2
#     2. width/2.0
#     3. height/3
#     4. 1 + 2 * 5
#
# Use the Python interpreter to check your answers.

width = 17
height = 12.0

exp_1 = width//2

exp_2 = width/2.0

exp_3 = height/3

exp_4 = 1 + 2 * 5

exp_list = [exp_1, exp_2, exp_3, exp_4]
for exp in exp_list:
    print(f"result: {exp}")
    print(f"type: {type(exp)}")

# 8, int
# 8.5, float
# 4.0, float
# 11, int
