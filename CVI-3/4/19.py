import random

s = int(input('zacinam so sumov'))

i1, i2, i3 = random.randint(1, 21), random.randint(1, 21), random.randint(1, 21)

if(i1 == i2 and i2 == i3):
    'vsetky rovnake'

elif(i1 == i2 or i2==i3 or i1==i3):
    'dva rovnake'
else
    'ziadna rovnaka'

