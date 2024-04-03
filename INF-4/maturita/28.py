wtd = int(input('Co mam spravil. 1 = rozdelit do dvoch, 2 = pod dva pod seba, 3 = pod dva vedla seba'))

if(wtd == 1):
    with open('from.txt','r') as r:
        with open('to.txt','w') as w:
            with open('to2.txt','w') as w2:
            for no, l in enumerate(r):
                if no % 2 == 0:
                    w.append(l.strip())
                    continue
                w2.append(l.strip())
                
            

if(wtd == 2):
    with open('from.txt','r') as r:
        with open('to.txt','w') as w:
            for l in r:
                w.append(l.strip())
                w.append(l.strip())

if(wtd == 3):
    with open('from.txt','r') as r:
        with open('to.txt','w') as w:
            for l in r:
                w.append(l.strip() + ' ' + l.strip())
