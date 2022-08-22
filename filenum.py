# Use the file name mbox-short.txt as the file name

count = 0
total = 0

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    parts = line.split()
    total = float(parts[1]) + total
    count = count + 1

average = total/count
print("Average spam confidence:", average )