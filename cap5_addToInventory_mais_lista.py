stuff = {}
entrada = True

while entrada:
    item = input('\nName an item of your inventory, or  type exit to finish: ')
    if item == 'exit':
        break
        entrada = False
    quantidade = input('Which quantit?: ')
    stuff.setdefault(item, quantidade)
 
def displayInventory(inventoryTela):
    print('\n--- Inventory: ---')
    item_total = 0
    for k, v in inventoryTela.items():
        print(str(v) +  ' ' + k)
        item_total += int(v)
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
        for i in addedItems:
            if i in inventory.keys():
                inventory = {i: 1 + int(inventory[i]) for i in inventory}
            else:
                inventory[i] = 1
        return inventory

dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']

stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
