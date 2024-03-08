t = [2,4,-7,-5,1,4,2,3]
a = list(filter(lambda x: x < 1, t))
a = [x for x in t if x < 1]

print(a)
print(len(a))
print(sum(a))
      
for n,i in enumerate(t):
    print(f'{n+1}. den bolo {i} stupnov.')
