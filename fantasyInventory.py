def displayInventory(inventory):
    total_items = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total_items = total_items + v
    print('Total number of items: ' + str(total_items))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] = inventory[i] + 1

player_inventory = {'cat': 1, 'dog': 1, 'banana': 1}
print('Welcome adventurer. What would you like to do? Press 1 to display current inventory. Press 2 to add items to your inventory.')
choice = (input())
if choice != 1 or 2:
    print('You didn\'t enter 1 or 2. Please try again')
elif int(choice) == 1:
    displayInventory(player_inventory)
else:
    print('Type your items, separated by a comma')
    added_items = input().split(', ')
    addToInventory(player_inventory, added_items)
    displayInventory(player_inventory)