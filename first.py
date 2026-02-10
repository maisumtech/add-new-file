items=[]
quantities=[]

while True:
    item=(input("enter item name (or enter 'stop' to finish)"))
    if item.lower()=='stop':
        break
    quantity=int(input("enter the quantity"))

    items.append(item)
    quantity.append(quantity)

i=0
while i < len(items):
    print("f{items[i]:<15}: {quantities}")
    i+=1