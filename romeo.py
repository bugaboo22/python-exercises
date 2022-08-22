fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh :
    text = line.split()
    for word in text :
        if word not in lst :
            lst.append(word)

lst.sort()
print(lst)