cislo = input("Zadajte cislo v desiatkovej sustave")
zakladSustavy = int(input("Do akej sústavi prevádzaš?"))
znaky = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
vysledok = 0;

if (zakladSustavy > 1 and zakladSustavy <= len(znaky)):
    pozice = 0;
    for i in range(len(cislo)-1, 0, -1):
        cifra = znaky.index(cislo[i])
        print(i)
        print(cislo[i])
        print(znaky.index(cislo[i]))
        print(cifra)
        vysledok += cifra * (int)(zakladSustavy ** pozice);
        pozice += 1
print("Vysledok", vysledok)
