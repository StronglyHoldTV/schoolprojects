fibArray = [0, 1]

def fibonacci_medzi(od, do):
    while fibArray[len(fibArray)-1] < do:
        i = len(fibArray)
        fibArray.append(fibArray[i-2]+fibArray[i-1])
    for i in fibArray:
        if od < i and i < do:
            print(i, end=" ")
    print()
    
    
fibonacci_medzi(10, 100)
fibonacci_medzi(1000, 3000)

