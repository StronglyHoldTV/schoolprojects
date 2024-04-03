cislo = input('zadaj rodne cislo')

r = cislo[0:2]
m = cislo[2:4]
d = cislo[4:6]
zena = False
valid = int(cislo)%11==0

if(int(m)-50 > 0):
    m = int(m)-50
    zena = True

print(r, m, d, zena, valid)
