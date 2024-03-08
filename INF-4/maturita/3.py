def do(cislo, zaklad):
    znaky = "0123456789ABCDEFGHIJKLMNOPRSTUQVXYZ"
    vysledok = 0
    cislo = cislo[::-1]
    for i, j in enumerate(cislo):
        vysledok += znaky.index(j)*(zaklad**i)
    print(vysledok)

def z(cislo, zaklad):
    znaky = "0123456789ABCDEFGHIJKLMNOPRSTUQVXYZ"
    vysledok = ""
    while cislo != 0:
        modulo = cislo % zaklad
        cislo = cislo // zaklad
        vysledok += znaky[modulo]
    print(vysledok[::-1])


a = int(input("Chceš previesť z [0] alebo do [1] desiatkovej sústavy?"))
if(a == 0):
    b = int(input("Zadaj cislo"))
    c = int(input("Zaklad"))
    z(b, c)

if(a == 1):
    b = input("Zadaj cislo")
    c = int(input("Zaklad"))
    do(b, c)
