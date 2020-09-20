import re

namesRegex = re.compile(r'Agent \w+')
var1 = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(var1)


agentNamesRegex = re.compile(r'Agent (\w)\w*')
var2 = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(var2)
