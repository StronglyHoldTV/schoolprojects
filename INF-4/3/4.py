a = input('Meno suboru: ')

with open(a, 'r') as f:
    for l in f:
        if(len(l.split(' ')) == 3):
            print(l, end='')
