def postupnost(start, koniec):
    s = ""
    for i in range(int(start), int(koniec)+1):
        s += str(i)
        if(i != koniec):
            s += " "
    return s
