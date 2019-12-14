allGuests = {'Alice':{'apples':5,'oranges':12},
             'Bob':{'sandwiches':3,'apples':2},
             'Keshu':{'cups':3,'apple pies':1}}

def totalBrought(guests,items):
    numBought = 0
    for k,v in guests.items():
        numBought = numBought + v.get(items,0)
    return numBought

print('Number of things Bought :')
print(' -- Apples -- ' + str(totalBrought(allGuests,'apples')))
print(' -- Cups -- ' + str(totalBrought(allGuests,'cups')))
print(' -- Cakes -- ' + str(totalBrought(allGuests,'cakes')))
print(' -- Oranges -- ' + str(totalBrought(allGuests,'oranges')))
print(' -- Sandwiches -- ' + str(totalBrought(allGuests,'sandwiches')))
print(' -- Apple Pies -- ' + str(totalBrought(allGuests,'apple pies')))
