# Exercise 2: This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line by
# finding the time string and then
# splitting that string into parts using the colon character.
# Once you have accumulated the counts for each hour,
# print out the counts, one per line, sorted by hour as shown below.
#
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

input_file = input("Enter a file name: ")

try:
    fhand = open(input_file)
except FileNotFoundError:
    print("File not found. Check again.")
    quit()

time_data = dict()

for line in fhand:
    if not line.startswith("From "):
        continue
    words = line.split()
    hours = words[5].split(":")
    time_data[hours[0]] = time_data.get(hours[0], 0) + 1

print(time_data)

time_list = list()
for hour, count in time_data.items():
    time_list.append((hour, count))
time_list.sort()

for time_tuple in time_list:
    print(time_tuple[0], time_tuple[1])