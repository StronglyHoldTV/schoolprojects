ord('z')


def ceasar(file, skok):
    with open(file, 'r') as f:
        with open('sifra.txt', 'w') as w:
            for a in f:
                s = ''
                for i in a:
                    if(not i.isalpha()):
                        s += i
                        continue
                    if 65 <= ord(i) <= 90:
                        if(ord(i) + skok)  > 90:
                            #s += chr(ord(i) + skok - 65)
                            continue
                        s += chr(ord(i) + skok)
                        #print(i, chr(ord(i) + skok), ord(i), chr(ord(i)))
                        continue
                    if 97 <= ord(i) <= 122:
                        if(ord(i) + skok) > 122:
                            #s+= chr(ord(i) + skok - 97)
                            continue
                        s += chr(ord(i) + skok)
                        continue
                    #s += a
                print(s)
                w.write(s)

ceasar('sifruj.txt', 0)
                
            
