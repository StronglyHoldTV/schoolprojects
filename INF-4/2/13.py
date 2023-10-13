def male(retazec, i):
    return retazec[:i]+retazec[i].lower()+retazec[i+1:]

def velke(retazec, i):
    return retazec[:i]+retazec[i].upper()+retazec[i+1:]

print(male('PYTHON', 3))
print(velke('python', 5))
