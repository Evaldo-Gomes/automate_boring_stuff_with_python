import re

corRegex = re.compile(r'.at')
var1 = corRegex.findall('The cat in the hat sat on the flat mat.')

print(var1)
