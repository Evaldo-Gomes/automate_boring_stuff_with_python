import re

xmasRegex = re.compile(r'\d+\s\w+')
var1 = xmasRegex.findall('12 drummers, 11 pippers, 10 lods, 9 ladies, 8 maids, 7 swans,6 geese, 5 rings, 4 birds, 3 hens, 2 dovers, 1 patriage')
print(var1)
