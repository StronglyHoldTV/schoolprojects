def factorial(i: int) -> int:
    x = 1
    for i in range(1, i+1):
        x *= i
    return x

n = int(input("n"))
k = int(input("k"))

print(factorial(n)/(factorial(n-k)*factorial(k)))
        
