import csv
from operator import itemgetter
from prettytable import PrettyTable
import time


def display_inventrory(inven):
    
    for item, amount in inven.items():
        print(item,':',amount)


def add_inventory(inven, added_item):
    # dicionarynew = {}
    # for i in added_item:
    #     if i in dicionarynew:
    #         dicionarynew[i] +=1
    #     else:
    #         dicionarynew[i] = 1
    #print(dicionarynew)
    for k  in added_item:
        if k in inven:
            inven[k] += 1
        else:
            inven[k] = 1
    
    
def print_table(inven):
    table = PrettyTable()
    table.field_names = ["item names", "count"]
    order = input("Do you order descendin[d] or ascending[a]? ")
    if order == 'd':
        inven= dict(sorted(inven.items(), key=itemgetter(1)))
    elif order == 'a':
        inven= dict(sorted(inven.items(), key=itemgetter(1), reverse=True))
    # else:
    #     inven = inven
    for k ,v in inven.items():
        table.add_row([k, v])
    print(table)


def import_inventory(inven,path):
    pola = [] # try is file czy istnieje i czy moge go otworzyc
    with open(path,encoding='utf-8') as testCSV:
        plikiCSV = csv.reader(testCSV, delimiter =',')
        # pola = []
        pola = next(plikiCSV)
        add_inventory(inven,pola)


def export_inventory(inven):
    with open('export_inventory.csv', mode='w', encoding='utf-8')  as exportfile:
        writer = csv.writer(exportfile, delimiter=',', quotechar='"')
        lista = []
        for k , v in inven.items():
            for i in range(v+1):
                lista.append(k)
        # headers = ['item', 'count']
        writer =csv.DictWriter(exportfile, fieldnames=lista)
        writer.writeheader()
        # for x in lista:
        #     writer.writerow(x)







inven = {'rope': 1, 'torch': 6, 'gold coinfff': 42,
'dagger': 1, 'arrow': 12, 'bow': 1, 'elixir': 2}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coinfff', 'ruby', 'sword']
path = "/home/dominik/codecool/home_work/inventory/inventory-project/importinventory.csv"
# display_inventrory(inven)
# add_inventory(inven,dragon_loot)
# display_inventrory(inven)
# print_table(inven)
# import_inventory(inven,path)
# display_inventrory(inven)
# print_table(inven)
# export_inventory(inven)



def table_print(inventory, order=None):
    item_title = 'item name'
    count_title = 'count'
    dash_ch = "-"
    max_widh_item = max([len(str(item)) for item in inventory.keys()]+ [len(item_title)])
    max_of_column = max([len(str(column)) for column in inventory.values()]+ [len(count_title)])
    sep = " | "
    hor_line =(dash_ch * (max_widh_item + max_of_column + len(sep)))
    # lengh_of_item = []
    # for item in inventory.keys():
    #     lenght = len(str(item))
    #     lengh_of_item.append(lenght)
    # max(lengh_of_item)
    # print("-" * (max_widh_item + max_of_column + 3))
    # print(max_of_column)
# header line
    print(hor_line)
    print(f"{item_title :>{max_widh_item}}{sep}{count_title :>{max_of_column}}")
    print(hor_line)
# rows 
    inventory_item = []
    if order == "count des":
        inventory_item = sorted(inventory.items(), key=lambda item: item[1], reverse=True)

    elif order =="count asc":
        inventory_item = sorted(inventory.items(), key=lambda item: item[1])
    else:
        inventory_item = inventory.items()

    for item, count in inventory_item:
        print(f"{item:>{max_widh_item}}{sep}{count:>{max_of_column}}")

# footer
    print(hor_line)


table_print(inven, order="count asc")
