import re

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
var1 = mo.group(1)
var2 = mo.group(2)

print(var1)
print(var2)
