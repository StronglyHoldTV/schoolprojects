with open('vek.txt', 'r') as f:
    vek = int(input('Zadaj vek: '))
    with open('mladsi.txt', 'w') as w:
        with open('ostatny.txt', 'w') as w2:
            d = {}
            lines = f.readlines()
            for i in range(0, len(lines)-1, 2):
                d.update({lines[i]: int(lines[i+1])})
            for i in d:
                if(d[i] < vek):
                    print(i, file=w)
                    continue
                print(i, file=w2)
        
        
