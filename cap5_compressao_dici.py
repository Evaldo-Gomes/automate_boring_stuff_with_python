dici1 = {'chave1': 10, 'chave2': 20, 'chave3': 30}

dici2 = {'chave4': 40, 'chave5': 50, 'chave6': 60}

#for i in dici2:
#    dici1[i] = dici2[i]

dici1.update(dici2)
print(dici1)


dici3 = {i: '9' + str(dici1[i]) for i in dici1}
print(dici3)

dici3 = {i: 9 + dici1[i] for i in dici1}
print(dici3)
