

with open(input('Zadaj nazov suboru') + '.txt', 'r') as f:
    print(f.readlines()[1], end='')
