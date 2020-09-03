import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My phone number is 415-555-4242.')
print('Phone number found: ' + mo.group())

'''

1) IMPORTE O MÓDULO REGEX

import re

2) CRIE UM OBJETO REGEX USANDO A FUNÇÃO re.compile() *USANDO UMA STRING PURA

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

3) PASSE A STRING QUE VOCÊ QUER PESQUISAR AO MÉTODO search() DO OBJETO REGEX
ISSO FARÁ O OBJETO Match SER RETORNADO

mo = phoneNumRegex.search('My phone number is 415-555-4242.')

4)CHAME O MÉTODO group() DO OBJETO Match PARA
RETORNAR UMA STRING COM O TEXTO CORRESPONDENTE

print('Phone number found: ' + mo.group())

'''
