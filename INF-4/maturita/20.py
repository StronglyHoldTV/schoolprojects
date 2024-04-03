import random

ret = input('zadaj retazec')
co = int(input('Chces rozdelit sriedavo na dva (0) alebo premiesat (1)'))

if co == 1:
    l = list(ret)
    random.shuffle(l)
    print(''.join(l))
if co == 0:
    print(''.join([x for no, x in enumerate(list(ret)) if no%2==0]))
    print(''.join([x for no, x in enumerate(list(ret)) if no%2==1]))
