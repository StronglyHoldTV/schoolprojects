r = [1,2,45,48,56,789,123,456,794,1659,461863,45685,48946,48975]

def rozdel(r):
    p = []
    n = []
    for i in r:
        if i%2==0:
            p.append(i)
        n.append(i)
    return (p,n)

l = ["x", 45, "asfasf", 46, 48984, "asofj", 8484, True, 167]

def ibaCisla(r):
    return [i for i in r if type(i) == int or type(i) == float]
