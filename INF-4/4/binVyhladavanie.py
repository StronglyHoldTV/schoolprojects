import random, time

li = sorted([random.randint(1,1000) for i in range(100)])
z = [random.randint(1,1000) for i in range(100)]

def current_milli_time():
    return round(time.time() * 1000)

# linerarne vyhladavanie prechadzame vsetky prvsky

def linear(l, t):
    for i in l:
        if i==t:
            return True
    return False


#binarne vyhladavanie, neprechadza vsetky prvky, pozaduje utriedeny zoznam
def binar(l, t):
    if(l[0] > t > l[-1]):
        return False
    while (len(l) > 1):
        p = l[len(l)//2]
        if(t>=p):
            l = l[(len(l)//2):]
        else:
            l = l[0:(len(l)//2)]
    return l[0]==t


# bubble sort - prehadzuje dvojice

def bubble_sort(l):
    n = len(l)

    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l

def quick_sort(l):

    if len(l) <= 1:
        return l
    
    pivot = z[0]

    mensie = []
    rovny = []
    vacsie = []

    for i in l:
        if i < pivot:
            mensie.append(i)
        elif i == pivot:
            rovny.append(i)
        else:
            vacsie.append(i)
    return quick_sort(mensie)+rovny+quick_sort(vacsie)
        

        
            
