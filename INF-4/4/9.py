def rozdel(retazec):
    j = 0
    l = []
    for i, x in enumerate(retazec):
        if(x == ' ' or x == '\n'):
            if(retazec[j:i].strip()):
                l.append(retazec[j:i].strip())
            j = i
    return l
print(rozdel('  jeden   dva tri'))
print(rozdel('ah\noj\n'))
