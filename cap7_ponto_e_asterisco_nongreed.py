import re

greedRegex = re.compile(r'<.*>')
mo1 = greedRegex.search('<To serve man> for dinner.>')
var1 = mo1.group()

print('greed ' + var1)


nongreedRegex = re.compile(r'<.*?>')
mo2 = nongreedRegex.search('<To serve man> for dinner.>')
var2 = mo2.group()

print('nongreed ' + var2)
