print('---------------------------------------------------------------')
print('Agrupando com parênteses')
import re

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My number is 415-555-4242')
a = mo.group(1)
b = mo.group(2)
c = mo.group(0)
print(a)
print(b)
print(c)
print('---------------------------------------------------------------')

print('Agrupando com o método groups() + atribuição múltipla')

mo.groups()
('415', '555-4242')
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

print('---------------------------------------------------------------')

print('Incluindo os parênteses "escapados" na string')

phoneNumberRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo2 = phoneNumberRegex.search('My number is (415)-555-4242')
d = mo.group(1)
e = mo.group(2)
print(d)
print(e)

print('---------------------------------------------------------------')
print('Correspondencia com vários grupos, usando o pipe "|"')

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
f = mo1.group()
print(f)
mo2 = heroRegex.search('Tina Fey and Batman')
g = mo2.group()
print(g)

print('---------------------------------------------------------------')
print('Corresponência entre diversos padrões com pipe "1"')

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
h = mo.group()
print(h)
i = mo.group(1)
print(i)

print('---------------------------------------------------------------')
print('Correspondência opcional usando "?"')

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
j = mo1.group()
print(j)
mo2 = batRegex.search('The adventures of Batwoman')
k = mo2.group()
print(k)


print('---------------------------------------------------------------')
print('Correspondendo a zero ou mais ocorrências usando "*"')

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
l = mo1.group()
print(l)
mo2 = batRegex.search('The adventures of Batwoman')
m = mo2.group()
print(m)
mo3 = batRegex.search('The adventures of Batwowowowoman')
n = mo3.group()
print(n)

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The adventures of Batwoman')
o = mo1.group()
print(o)
mo2 = batRegex.search('The adventures of Batwowowowoman')
o = mo2.group()
print(o)
mo3 = batRegex.search('The adventures of Batman')
mo3 == None
print(mo3)

print('---------------------------------------------------------------')
print('Correspondendo a repetições especcíficas usando "{}"')

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
p = mo1.group()
print(p)

print('---------------------------------------------------------------')
print('Correspondências com greedy e nongreedy')

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
q = mo1.group()
print(q)

print('---------------------------------------------------------------')
print('Método findall()')

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
r = mo.group()
print('Sem o findall()')
print(r)
print('Com o findall() e SEM grupos - *Retorna uma lista')
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)
print('Com o findall() e COM grupos - *Retorna uma lista de tuplas')
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
s = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(s)


print('---------------------------------------------------------------')



























