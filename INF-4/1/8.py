import random

def hadanie(od, do):
    print("Myslím si číslo, uhádni ho!")
    r = random.randint(od, do)
    pokus = 0
    while True:
        i = int(input('tvoj tip: '))
        pokus += 1
        if(i == r):
            print(f'Uhádol si na {pokus}. pokus. Gratulujem.')
            return
        if(r > i):
            print("*** pridaj")
        if(r < i):
            print("*** uber")
        if(pokus >= 10):
            print("Neuhádol si ani na 10 pokusov.")
            print(f"Myslel som si číslo {r}.")
            return
            
