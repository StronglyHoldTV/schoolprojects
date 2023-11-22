def priemer(c):
    with open('cisla.txt', 'r') as f:
        s = 0
        i = 0
        for l in f:
            s += int(l)
            i+=1
        return(s/i)
print('priemer =', priemer('cisla.txt'))
