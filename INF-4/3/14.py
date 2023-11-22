with open('uspory.txt', 'r') as i:
    r = i.readlines()
    d = {}
    for x in range(0, len(r)-1, 2):
        d.update({r[x].strip(): float(r[x+1].strip())})
    maxlenkey = len(max(d.keys(),key=len))
    maxlenval = 7
    with open('formateduspory.txt', 'w') as j:
        print('Meno'.ljust(maxlenkey) + '| Naset', file=j)
        print('-'*(maxlenkey + maxlenval + 2), file=j)
        for x in d:
            print(x.ljust(maxlenkey) + '| ' + str(d[x]), file=j)
        print('-'*(maxlenkey + maxlenval + 2), file=j)
        print('MAX =', max(d.values()), file=j)
        print('MIN =', min(d.values()), file=j)
        print('AVERAGE =', sum(d.values())/len(d.values()), file=j)

