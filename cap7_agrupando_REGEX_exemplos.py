import re

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My number is 415-555-4242')
a = mo.group(1)
b = mo.group(2)
c = mo.group(0)
print(a)
print(b)
print(c)
