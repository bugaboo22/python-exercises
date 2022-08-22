fh = open("mbox-short.txt")
count = 0

for i in fh :
    i = i.rstrip()
    if not i.startswith("From") : continue
    words = i.split() 
    print(words[1])
    count = count+1

print("There were", count  , "lines in the file with From as the first word")