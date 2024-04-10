n = int(input('zadaj n'))

fibo = [1,1]
for i in range(n-2):
    fibo.append(fibo[len(fibo)-1]+fibo[len(fibo)-2])

#print(str(fibo).replace('[', '').replace(']', ''))
print(''.join([str(i) + ', ' for i in fibo])[:-2])
