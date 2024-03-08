def fibonacci(fr: int, n: int):
    f = [1,1]
    while True:
        if(f[len(f)-1] > n):
            f.remove(f[len(f)-1])
            break
        f.append(f[len(f)-2] + f[len(f)-1])
    r = []
    for i in f:
        if  fr <= i and i <= n:
            r.append(i)
    return r
    
