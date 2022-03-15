# Exercise 1: Write a function called chop that takes a list and modifies it,
# removing the first and last elements, and
# returns None. Then
# write a function called middle that takes a list and
# returns a new list that contains all but the first and last elements.
import random


def chop(list_to_chop):
    del list_to_chop[0]
    del list_to_chop[-1]

def middle(list_to_cut):
    return list_to_cut[1:-2]

list_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(f"Before chop() function applied list_x = {list_x}")
print(f"The chop() function returns {chop(list_x)}")
print(f"After chop() function applied list_x = {list_x}")
# the list_x is modified

print(f"Before middle() function applied list_y = {list_y}")
print(f"The middle() function returns {middle(list_y)}")
print(f"After middle() function applied list_y = {list_y}")
# the original list_y is not modified, and the middle() function creates new list


