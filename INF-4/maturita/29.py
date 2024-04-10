with open('uspory.txt', 'r') as r:
    print('Priezvisko'.ljust(10) + '|' 'Suma'.rjust(5))
    print('-'*11)
    m, mv = '', 0
    mm, mmv = '', 0
    s = 0
    for line in r:
        name = line.strip().ljust(10)
        i = float(r.readline().strip())
        uspory = str(i).rjust(5)
        print(name + '|' + uspory)
        if mv < i:
            m = name
            mv = i
        if mmv == 0:
            mmv = i
            mm = name
        if mmv > i:
            mmv = i
            mm = name
        s += i
        
    print(f'SUM={s}')
    print(f'minimal = {mm} {mmv}')
    print(f'maximal = {m} {mv}')
