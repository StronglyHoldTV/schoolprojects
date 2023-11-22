

with open(input('Zadaj nazov suboru') + '.txt', 'r') as f:
    s = ''
    for a, b in enumerate(f.readline()):
        if a%2 == 0:
            s += b
    print(s, end='')
