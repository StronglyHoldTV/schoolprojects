def obdlznik(sirka:int, znak='*'):
    for i in range(0, sirka+1):
        print(znak, end="")
    print()
    print(znak, end="")
    for i in range(0, sirka-1):
        print(" ", end="")
    print(znak, end="")
    print()
    for i in range(0, sirka+1):
        print(znak, end="")
    print()
obdlznik(30, '#')
obdlznik(6)
obdlznik(19, 'O')
