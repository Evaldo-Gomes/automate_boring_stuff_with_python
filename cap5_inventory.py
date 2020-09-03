stuff = {}

entrada = True

while entrada:
    item = input('\nName an item of your inventory, or  type exit to finish: ')
    if item == 'exit':
        break
        entrada = False
    quantidade = input('Which quantit?: ')
    
    stuff.setdefault(item, quantidade)
 
def displayInventory(inventory):
    print('\n--- Inventory: ---')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) +  ' ' + k)
        item_total += int(v)
    print('Total number of items: ' + str(item_total))

displayInventory(stuff)

