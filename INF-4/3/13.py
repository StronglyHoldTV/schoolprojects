with open(input('zadaj vstupny subor'), 'r') as i:
    with open('output.txt', 's') as o:
        r = i.read()
        co = input('Co chces urobit? Rozdelit riadky [1] Duplikovat pod seba[2] duplikovat vedla seba[3]')
        if(co == 1):
            with open('output2.txt', 's') as o2:
                for x, y in enumerate(r):
                    if(x%2 == 0):
                        o.write(x)
                        continue
                    o2.write(x)
        if(co == 2):
            for x in i:
                o.write(x)
                o.write(x)
        if(co == 3):
            for x in i:
                o.write(x + '', x)
