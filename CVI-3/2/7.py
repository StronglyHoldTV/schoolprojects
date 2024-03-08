w = input('zadaj cislo:')
i = 1
s = 0 
for l in w:
    print(str(i)+'. cifra ' + l)
    i += 1
    s += int(l)
print('ciferny sucet = ' + str(s))
    
