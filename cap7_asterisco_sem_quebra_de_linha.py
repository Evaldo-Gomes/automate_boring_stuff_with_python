import re

noNewLineRegex = re.compile('.*')
var1 = noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(var1)
