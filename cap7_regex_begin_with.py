import re

beginWithHello = re.compile(r'^Hello')
var = beginWithHello.search('Hello Word! 1101')

var2 = var.group()

print(var)
print(var2)
