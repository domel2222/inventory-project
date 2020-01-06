

def display_inventrory(inven):
    # display inventory optional option print(item, ivent[item])
    for item, amount in inven.items():
        print(item,':',amount)



def add_inventory(inven, added_item):
    dicionarynew = {}
    for i in dragon_loot:
        if i in dicionarynew:
            dicionarynew[i] +=1
        else:
            dicionarynew[i] = 1
    print(dicionarynew)
    for k, v in dicionarynew.items():
        if k in inven:
            inven[k] += v
        else:
            inven[k] = v
    
    





inven = {'rope': 1, 'torch': 6, 'gold coin': 42,
    'dagger': 1, 'arrow': 12, 'bow': 1, 'elixir': 2}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'sword']

display_inventrory(inven)
add_inventory(inven,dragon_loot)
display_inventrory(inven)
