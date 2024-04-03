with open(input('zadaj nazov suboru')+'.txt', 'r') as r:
    with open('cvicenie.txt', 'w') as w:
        for l in r:
            l.replace('y', '_')
            l.replace('i', '_')
            l.replace('ý', '_')
            l.replace('í', '_')
            w.append(l)
