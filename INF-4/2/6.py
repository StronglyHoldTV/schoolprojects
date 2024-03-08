def stvorec(n, znak):
    r = ""
    r += znak*n
    r += "\n"
    for i in range(0, n-2):
        r += znak + " "*(n-2) + znak
        r += "\n"
    r += znak*n
    return r

print(stvorec(5, '#'))
