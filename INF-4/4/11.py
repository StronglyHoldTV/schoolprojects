import random

n = 10

x = [random.randint(0,100) for i in range(n-1)]

x.sort()

def binVyhladavanie(number):
    for i in x:
        if bin(number) == bin(i):
            print(number)

print(x)
