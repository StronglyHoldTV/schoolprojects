import math

n = int(input('zadaj n: '))

for i in range(0, n):
    stars = int(1+2*i)
    spaces = int((2*n-stars)/2)
    #print(stars, spaces)
    #stars = (1) + (stars-2) +
    print(' '*spaces + '*' + '-'*(stars-2) + '*'*(min(i, 1)) + ' '*spaces)
