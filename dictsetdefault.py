dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}

def displayInventory(inventory):
    print('Inventory:')
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print('Total number of items: ' + str(total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
print('dagger' in inv)
print('dagger' in inv.values())
print('dagger' in inv.keys())
print('dagger' in inv.items())
print(('dagger',1) in inv.items())
print(inv.get('gold coin',0))
print(inv.get('gold',0))
print(inv.get('gold'))
