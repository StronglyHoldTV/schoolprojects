nazov = input('Zadaj subor ktory ches opravit.')

with open(nazov, 'r'):
    a = nazov.read()
    b = ""
    zmenit = True
    for i in a:
        if i.isAlpha() and zmenit:
            b+= i.upper() 
            zmenit = False
            continue
        if i == '.':
            zmenit = True
        b += i
    print(b)
