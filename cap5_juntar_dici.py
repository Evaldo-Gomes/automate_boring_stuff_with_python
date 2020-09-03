dici1 = {'chave1': 10, 'chave2': 20, 'chave3': 30}

dici2 = {'chave4': 40, 'chave5': 50, 'chave6': 60}

for i in dici2:
    dici1[i] = dici2[i]

print(dici1)
print(dici2)
