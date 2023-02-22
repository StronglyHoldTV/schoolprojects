w = input('zadaj slovo: ')
n = int(input('zadaj n: '))

for i in range(n):
    o = i%4
    print('        '*o + w)
