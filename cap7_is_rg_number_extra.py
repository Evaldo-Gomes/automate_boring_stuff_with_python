import re

rgNumRegex = re.compile(r'\d\d.\d\d\d.\d\d\d-\d')
mo = rgNumRegex.search('Meu RG é: 26.602.733-7.')
print('Número de RG encontrado: ' + mo.group())
