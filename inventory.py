import pprint
stuff = {'rope':1,
         'torch':6,'gold coins':42,'dagger':1,'arrow':12}
count={}
def displayInventory(inventory):
    print("Inventory is:")
    itemTotal = 0
    for k,v in inventory.items():
        count[v] = k
        itemTotal = itemTotal + v
    count['Total'] = itemTotal
    return count
displayInventory(stuff)
pprint.pprint(count)
    
