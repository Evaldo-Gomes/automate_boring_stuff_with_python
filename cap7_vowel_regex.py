import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
var1 = vowelRegex.findall('Robocop eats baby food. BABY FOOD')

print(var1)
