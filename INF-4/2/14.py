def riadky(retazec):
    r = retazec.split('\n')
    for i in r:
        if i[len(i)-1] == "\\":
            r.remove(r.index(i))
