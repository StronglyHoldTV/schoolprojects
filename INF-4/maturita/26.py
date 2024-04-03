with open('opravit.txt', 'r') as r:
    with open('opravene.txt', 'w') as w:
        for l in r:
            m = ''
            dalsie = True
            for ch in l:
                if(dalsie and ch.isAlpha()):
                    m += ch.upper()
                    dalsie = False
                if(ch == '.'):
                    dalsie = True
                m+=ch
            w.append(m)
                    
