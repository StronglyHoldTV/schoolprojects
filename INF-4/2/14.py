def riadky(retazec):
    r = retazec.split('\n')
    for no, item in enumerate(r):
        print(f'{no+1}. {item}')
