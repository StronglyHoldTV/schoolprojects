n = int(input('zadaj číslo n='))
a = n
print(n, end=' = ')
while(a < n):
    if(n%a == 0):
        print(int(a), end = ' ')
        n = int(n/a)
    a+=1
    
