stuff = {'rope':1, 'torch':6, 'gold coin': 42, 'dagger':1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in dragonLoot:
        stuff.setdefault(item,0)
        stuff[item]+=1

    return stuff

def displayInventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))



stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
