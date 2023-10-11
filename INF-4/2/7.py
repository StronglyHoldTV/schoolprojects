def vyhod_duplikaty(retazec):
    previous = ""
    s = ""
    for i in retazec:
        if(previous != i):
            s+=i
        previous = i
    return s

print(vyhod_duplikaty('Braatisssllavaaaaa'))
