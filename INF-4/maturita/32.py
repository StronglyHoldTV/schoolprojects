with open('vek.txt', 'r') as file:
    with open('mladsi.txt', 'w') as w:
        with open('ostany.txt', 'w') as w2:
            hranica = int(input('Hranica.'))
            m = 0
            o = 0
            for line in file:
                name = line.strip()
                vek = int(file.readline().strip())
                if vek < hranica:
                    m += 1
                    w.write(name)
                else:
                    o += 1
                    w2.write(name)

            if m == 0:
                print('nenasiel sa ziaden mladsi')
            if o == 0:
                print('nenasiel sa ziaden iny')
                    
    
