
import re

r = open("regex_sum_42.txt", "r")

numlist = list()
for line in r :
    line = line.rstrip()
    integers = re.findall('[0-9]+', line)
    if len(integers) < 1 : continue
    
    for i in range(len(integers)):
        num = float(integers[i])
        numlist.append(num)
print(sum(numlist))