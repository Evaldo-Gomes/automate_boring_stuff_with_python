import re

wholeStringIsNum = re.compile(r'^\d+$')
var = wholeStringIsNum.search('1234567890')

var2 = var.group()

print(var)
print(var2)
