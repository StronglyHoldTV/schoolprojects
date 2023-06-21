import math

mn = int(input('Zadaj od: '))
mx = int(input('Zadaj od: '))
step = int(input('Zadaj krok: '))

for i in range(mn, mx+1, step):
    iRad = math.radians(i)
    sin = math.sin(iRad)
    cos = math.cos(iRad)
    suma = sin**2+cos**2
    print(f'{i:3} sin**2={sin**2:6.4f} cos**2={cos**2:6.4f} sucet={suma}')
