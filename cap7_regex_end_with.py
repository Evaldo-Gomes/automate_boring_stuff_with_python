import re

endWithNumber = re.compile(r'(\d)*$')
var = endWithNumber.search('Hello Word! 1101')

var2 = var.group()

print(var)
print(var2)
