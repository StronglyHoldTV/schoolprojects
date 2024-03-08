with open('hodiny.txt', 'r') as file:
    d = {}
    lines = file.readlines()
    for i in range(0, len(lines)-1, 3):
        d.update({ lines[i].strip(): [int(lines[i+1]), int(lines[i+2])]})
    with open('vsetkyospravedlnene.txt', 'w') as out:
        for x in d:
            if(d[x][1] == 0):
                print(x + ' ' + str(d[x][0]), file = out)
    with open('vsetkyneospravedlnene.txt', 'w') as out:
        t = False
        for x in d:
           if(d[x][1] != 0):
            print(x + ' ' + str(d[x][1]), file = out)
            t = True
        if(t == False):
            print('Vsetci maju ospravedlnene hodiny.')
