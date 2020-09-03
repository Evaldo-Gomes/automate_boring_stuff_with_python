def join_list(lista):
     str = ', '.join(lista[:-1])
     return '{} and {}'.format(str, lista[-1])

spam = ['apples','bananas','tofu','cats']
print(join_list(spam))
