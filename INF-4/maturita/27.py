x = int(input('posun'))


with open('zasifrovat.txt', 'r') as r:
    with open('sifra.txt', 'w') as w:
        for l in r:
            l = l.strip()
            m = []
            for j in l:
                if(ord('a') < ord(j) and ord(j) < ord('z')):
                    c = ord(j)+x
                    if(c>ord('z')):
                        c -= ord('a')
                    m.append(chr(c))
                    continue
                if(ord('A') < ord(j) and ord(j) < ord('Z')):
                    c = ord(j)+x
                    if(c>ord('Z')):
                        c -= ord('A')
                    m.append(chr(c))
                    continue
                m.append(j)
            w.append(m)
