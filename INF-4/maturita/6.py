import random

f = int(input("Od?"))
t = int(input("Do?"))

cislo = random.randint(f, t+1)

hadaj = None
pokus = 0

while hadaj != cislo:
    hadaj = int(input("Hadaj cislo"))
    pokus += 1
    if hadaj > cislo:
        print('Menej')
    if hadaj < cislo:
        print('Viac')

print(f'Hura cislo bolo {cislo}, uhadol si na {pokus} pokus')
