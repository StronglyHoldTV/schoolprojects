def prime(number: int) -> True:
    delitele = []
    for i in range(1, number+1):
        if number % i == 0:
            delitele.append(i)
    if len(delitele) == 2:
        return True
    print(delitele)
    return False
