with open('znamky.txt', 'r') as f:
    l = f.readlines()
    d = {}
    for i in range(0, len(l)-1, 2):
        m = l[i+1].strip().split(' ')
        d.update({l[i].strip(): [int(m[0]), int(m[1]), int(m[2]), int(m[3])]})
    n = input('zadaj prizvisko ziaka').lower()
    for i in d:
        if (i.lower() == n):
            q = d[i]
            print(i)
            print('ma tieto znamky')
            print(*q)
            print('jeho priemer je')
            print(sum(d[i])/len(d[i]))
            print('a')
            print('nezmaturoval' if 5 in d[i] else 'zmaturoval')
