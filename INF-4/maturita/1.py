def isPrime(number: int):
    if number < 0:
        raise Exception("This isn't natural number.")
    numbers = []
    for i in range(1, number+1):
        if number%i == 0:
            numbers.append(i)
    prime = False if len(numbers) == 2 else True
    return (prime, numbers)
    
