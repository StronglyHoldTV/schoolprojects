
def prevod_z():

    cislo = int( input("Zadaj číslo: ") )
    zaklad = int( input("Zadaj základ: ") )

    zv = ""

    hex_pismena = ["A","B","C","D","E","F"]

    while cislo > 0:
        if cislo%zaklad < 10:
            zv += str(cislo%zaklad)

        else:
            zv+= hex_pismena[cislo%zaklad-10]
            
            
        cislo //= zaklad

    return zv[::-1]

def prevod_na():

    cislo = input("Zadaj číslo: ") 
    zaklad = int( input("Zadaj základ: ") )

    
















    
    

        
