a = input('meno suboru')
b = input('počet riadkov')

with open(a, 'r') as f:
    l = f.readline()
    d = len(l)
    x = 1
    while l != '':
        l = f.readline()
        d = max(d, len(l))
        x += 1
    print(f'subor ma {x} riadkov')
    print(f'najdlhsi riadok ma {d} znakov')

a = input('meno suboru')
b = input('počet riadkov')

with open(a, 'r') as f:
    d = 0
    x = 0
    for l in f:
        d = max(d, len(l))
        x += 1
    print(f'subor ma {x} riadkov')
    print(f'najdlhsi riadok ma {d} znakov')

a = input('meno suboru')
b = input('počet riadkov')

with open(a, 'r') as f:
    l = f.read().split('\n')
    d = 0
    for i in l:
       d = max(d, len(l))
    print(f'subor ma {len(l)} riadkov')
    print(f'najdlhsi riadok ma {d} znakov')
