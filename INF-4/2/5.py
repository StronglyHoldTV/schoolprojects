def rozsekaj(text, sirka):
    s = ""
    p = 0
    for i in range(0, len(text)-1, sirka):
        print(len(text)-1)
        s += text[p:i]+"\n"
        print(text[p:i])
        print(p)
        print(i)
        p = i
    s += text[p:]
    return s


print(rozsekaj('Anicka dusicka, kde si bola', 10))
