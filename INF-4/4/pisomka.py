import random
n = int(input('pocet hodov'))
print([[random.randint(1,6) for _ in range(n)].count(i) for i in range(1,7)])
