# Exercise 5: Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the colon character and then
# use the float function to convert the extracted string into a ﬂoating point number.

str = 'X-DSPAM-Confidence:0.8475'
str_col_pos = str.find(":")
# print(str_col_pos)
str_val = float(str[str_col_pos+1:])
print(str_val)
print(type(str_val))
