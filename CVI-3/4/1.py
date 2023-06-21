first = int(input("zadaj km pre prvý deň"))
goal = int(input("zadaj cielove km"))
day = 1
while first < goal:
    first *= 1.1
    day += 1
print(f'zadaj {day}. den prebehne {first:.2f}km')
