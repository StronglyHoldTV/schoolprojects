last = '  '
l = []
while last!='':
    x = input('Zadaj priezvisko')
    if(x != ''):
        l.append(x)
    last = x

def pridat(priezvisko):
    for no, i in enumerate(l):
        if i < priezvisko:
            continue
        else:
            l.insert(no, priezvisko)
            break
    return l

def odstan(priezvisko):
    for no, i in enumerate(l):
        if i.lower() != priezvisko.lower():
            print(no, i)
            continue
        l.pop(no)
        print(no)
    return l
    
