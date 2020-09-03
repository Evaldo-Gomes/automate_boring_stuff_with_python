def convert(listValue):
    x = []
    name = ''
    for i in range(len(listValue)):
        if listValue[i] != listValue[-1]:
            x.append(listValue[i])
            name = str(x)[1:-1] + ', '
        else:
            name += 'and ' + str(listValue[i])
            for i in range(0, len(name)):
                name = name.replace("'",'')
    return name        
span = ['aples','bananas','tofu','cats']
print(convert(span))





