allGuests = {'Alice':   {'apples': 5, 'pretzels': 12},
                        'Bob':  {'ham sandwiches': 3, 'apple': 2},
                        'Carol':  {'cups': 3, 'apples pies': 1}}

def totalBrought(guest, item):
    numBrought = 0
    for k, v in guest.items():
        numBrought = numBrought + v.get(item,0)
    return numBrought

print('Number of things being brought: ')
print(' - Apples        ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups            ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiche ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))
print(allGuests.items())


