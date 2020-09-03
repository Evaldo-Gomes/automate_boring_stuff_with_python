stuff = {'gold coin': 1,'dagger': 1}
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        stuff.setdefault(item, 0)
        inventory[item] += 1
    return inventory    

stuff = addToInventory(stuff, dragonLoot)
print(stuff)
            
