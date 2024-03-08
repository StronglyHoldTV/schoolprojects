print('zadaj vysky ziakov:')
n = 1
y = 0
x = 1
chyba = False
while True:
    x = input(f'   vyska ziaka c. {n}')
    if(not x):
        break
    if(y > int(x)):
        chyba = True
        print('Sem')
    n += 1
    y = int(x)

if(chyba == True):
    print('Nespravne')
else:
    
    print('Spravne')
