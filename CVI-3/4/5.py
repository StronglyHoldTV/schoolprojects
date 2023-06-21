n = int(input('zadaj cislo: '))
cs = 0
while n > 0:
    print(n % 10)
    cs = n % 10
    n = int(n / 10)

print(f'ciferny sucet {cs}')
