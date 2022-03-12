# Exercise 2: Write a program to prompt for a file name, and then
# read through the file and look for lines of the form:
#
# X-DSPAM-Confidence: 0.8475
#
# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the ﬂoating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines.
# When you reach the end of the file, print out the average spam confidence.

fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except FileNotFoundError:
    print("Enter correct file")
    exit()
file_count = 0
file_total = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence: "):
        fpos = line.find(" ")
        fpost = line.find("\n")
        fline = float(line[fpos:fpost])
        file_count += 1
        file_total += fline
        favg = file_total/file_count
        # print(fline)
print(f"Total count = {file_count}\nTotal value = {file_total}\nAverage spam confidence: {round(favg, 4)}")