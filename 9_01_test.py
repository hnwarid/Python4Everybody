fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File", fname, "not found")
worddict = dict()
count = 0
for line in fhand:
    if len(line) == 0 : continue
    line = line.split()
    for word in line:
        worddict[word] = count
        count = count +1
print(worddict)
