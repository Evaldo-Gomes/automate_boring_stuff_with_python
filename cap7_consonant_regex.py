import re

consonantRegex = re.compile(r'[^aeiouAEIOU]')
var1 = consonantRegex.findall('Robocop eats baby food. BABY FOOD')

print(var1)
