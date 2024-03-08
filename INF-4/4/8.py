def vzostupne(zoznam):
    for x, i in enumerate(zoznam):
        if(x == len(zoznam)-1):
            return True
        if i > zoznam[x+1]:
            return False

print(vzostupne([1, 5, 5, 8, 100]))
print(vzostupne(['pyton', 'python', 'pytliak']))
