import re

robocop = re.compile(r'robocop', re.I)
var1 = robocop.search('Robocop is part man, part machine, all cop.').group()

robocop2 = re.compile(r'robocop', re.I)
var2 = robocop2.search('ROBOCOP protects innocents').group()

robocop3 = re.compile(r'robocop', re.I)
var3 = robocop3.search('Al, why does your programming book talk about robocop so much?').group()

print(var1)
print(var2)
print(var3)
