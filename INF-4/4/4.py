
def vypis(zoznam, pocet):
    a = zoznam.copy()
    for x, a in enumerate(zoznam):
        print(a, end = ' ')
        #print(x%pocet)
        if((x+1)%pocet == 0):
            print()
    print()
zoz = list(range(1, 19))
vypis(zoz, 4)
vypis(list('Python'), 2)
