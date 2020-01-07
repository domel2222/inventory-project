import csv
from operator import itemgetter
from prettytable import PrettyTable
import time


def display_inventrory(inven):
    
    for item, amount in inven.items():
        print(item,':',amount)


def add_inventory(inven, added_item):
    dicionarynew = {}
    for i in added_item:
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
    
    
def print_table(inven):
    table = PrettyTable()
    table.field_names = ["item names","count"]
    order = input("Do you order descendin[d] or ascending[a]? ")
    if order == 'd':
        inven= dict(sorted(inven.items(), key=itemgetter(1)))
    elif order == 'a':
        inven= dict(sorted(inven.items(), key=itemgetter(1), reverse=True))
    else:
        inven = inven
    for k ,v in inven.items():
        table.add_row([k, v])
    print(table)


def import_inventory(inven,path):
    pola = []
    with open(path,encoding='utf-8') as testCSV:
        plikiCSV = csv.reader(testCSV, delimiter =',')
        pola = []
        pola = next(plikiCSV)
        add_inventory(inven,pola)


def export_inventory(inven):
    with open('export_inventory.csv',mode='w', encoding='utf-8')  as exportfile:
        writer = csv.writer(exportfile, delimiter=',', quotechar='"')
        lista = []
        for k , v in inven.items():
            lista.append(k)
            lista.append(v)
        # headers = ['item', 'count']
        writer =csv.DictWriter(exportfile, fieldnames=lista)
        writer.writeheader()
        # for x in lista:
        #     writer.writerow(x)







inven = {'rope': 1, 'torch': 6, 'gold coin': 42,
'dagger': 1, 'arrow': 12, 'bow': 1, 'elixir': 2}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'sword']
path = "/home/dominik/codecool/home_work/inventory/inventory-project/importinventory.csv"
display_inventrory(inven)
add_inventory(inven,dragon_loot)
display_inventrory(inven)
print_table(inven)
import_inventory(inven,path)
display_inventrory(inven)
print_table(inven)
export_inventory(inven)

