def factorial(number: int):
    n = 1
    for i in range(1, number+1):
        n*=i
    return n

def combNumber(n: int, k: int):
    return factorial(n)/(factorial(k)*factorial(n-k))
    
