class Stock:    #Zadefinujem si classu s properties name count a price
    def __init__(self, name, count, price):
        self.name = name
        self.count = count
        self.price = price

stock_objects = []  #list objektov classy Stock
database = "sklad.txt"   #path mojho textaku

def add_object(name,count,price):   #funkcia ktora pridava objekty do classy a uklada ich do listu
    stock_object = Stock(name,count,price)
    stock_objects.append(stock_object)

def hepl():     #vypise vsetky commands
    print(com_dict.keys())

def list():     #vypise vsetky objekty v Stock
    print("-"*60)
    for i,object in enumerate(stock_objects):
        print(f"{i+1}. Name: {object.name: <12}Count: {object.count: <12}Unit price: {object.price: <12}")
    print("-"*60)

def add():      #ziska user input a posle dalej do add_object
    name = input("Name of the product: ")
    count = int(input("Number of items: "))
    price = float(input("Set a unit price: "))
    add_object(name,count,price)

def clear():    #prepise textak na blank a clearne list s objectami
    if input("Are you sure? Clear the database - type: \"Y\"/\"N\" ") != "Y":
        pass
    else:
        file = open(database,"w",encoding="UTF-8")
        stock_objects.clear()
        file.close()

def read_file():    #precita textak a zapise kazdu line ako objekt do Stock
    file = open(database,"r",encoding="UTF-8")
    stock_objects.clear()
    for line in file:
        properties = line.split(" ")
        add_object(properties[0],int(properties[1]),float(properties[2]))
    file.close()

def save():     #prepise textak objektami zo Stocku
    file = open(database,"w",encoding="UTF-8")
    for object in stock_objects:
        file.write(f"{object.name} {object.count} {object.price} \n")
    file.close()

def edit():
    num = int(input("Number of the product to be edited: "))-1
    name = input("Edit name (blank if unchanged): ")
    count = input("Edit number of items (blank if unchanged): ")
    price = input("Edit unit price (blank if unchanged): ")
    if name != "":
        stock_objects[num].name = name
    if count != "":
        stock_objects[num].count = int(count)
    if price != "":
        stock_objects[num].price = float(price)

def remove():
    num = int(input("Number of the product to be removed (0 to cancel): "))-1
    if num != -1:
        stock_objects.pop(num)

#Dictionary kde ukladam commandy
com_dict = {"help":hepl,"exit":"Exit the program","list":list,"add":add,"clear":clear,"edit":edit,"remove":remove}

def main(): #mainloop
    read_file()
    com = input("Prompt: ")
    if com != "exit":
        try:
            com_dict[com]()
        except:
            print("Bad command...")
        save()
        main()
    else:
        save()


print("Input command (\"help\" for list of commands)")
main()
