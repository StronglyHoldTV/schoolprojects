def prevrat(s):
    r = ""
    for i in range(len(s)-1, 0, -1):
        r += s[i]
    return r   

print(prevrat('tseb eht si nohtyP'))