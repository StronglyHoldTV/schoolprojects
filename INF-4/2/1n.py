def prevod(cislo, zaklad):
    vysledok = ""
    znaky = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if (zaklad <= 1 or zaklad > len(znaky)):
        raise Exception(f'Zaklad is less than 1 and more than {len(znaky)}')
    while(cislo > 0):
        modulo = cislo%zaklad
        vysledok += znaky[modulo]
        cislo = cislo//zaklad
    return vysledok[::-1]

def prevodtodec(cislo, zaklad):
    znaky = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    vysledok = 0
    for no, i in enumerate(cislo[::-1]):
        vysledok += znaky.index(i) * (zaklad** (no))
    return vysledok
    

while True:
   # a = int(input("Zadajte cislo v desiatkovej sustave"))
   # b = int(input("Do akej sústavi prevádzaš?"))
    #print(prevod(a, b))
   a = input("Zadajte cislo v nejakej sustave")
   b = int(input("V akej sustave je to cislo?"))
   print(prevodtodec(a, b))
