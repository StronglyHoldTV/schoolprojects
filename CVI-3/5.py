import math
print("    x     |  sin(x)")
for d in range(0,90,5):
    print("{:^10.2f}|{:^10.2f}".format(d,math.sin(math.radians(d))))
