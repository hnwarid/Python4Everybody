# Exercise 5: This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from
# (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.
#
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

input_file = input("Enter a file name: ")
site_data = dict()

try:
    fhand = open(input_file)

except FileNotFoundError:
    print("File is not found. Check again.")
    quit()

for line in fhand:
    if not line.startswith("From "):
        continue
    words = line.strip().lower().split()  # default split() method argument is space
    # atmail_pos = words.find("@")
    # site = words[atmail_pos + 1:]
    # this line below is simpler:
    site = words[1].split("@")  # here we use "@" as argument
    # print(email)
    site_data[site[1]] = site_data.get(site[1], 0) + 1

print(site_data)
