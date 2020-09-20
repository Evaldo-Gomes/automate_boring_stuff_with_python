import re

newLineRegex = re.compile('.*', re.DOTALL)
var1 = newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(var1)
