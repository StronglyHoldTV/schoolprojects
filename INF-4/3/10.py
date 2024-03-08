with open(input('Zadaj nazov suboru: '), 'r') as f:
    with open('pravopisnecvicenie.txt', 'w') as s:
        s.write(f.read().replace('i', '_').replace('y', '_').replace('í', '_').replace('ý', '_'))
