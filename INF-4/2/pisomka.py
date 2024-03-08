def vyhod_duplikaty(s: str) -> str:
    a = ''
    last = ''
    for c in s:
        if(last != c):
            a += c
        last = c
    return a
