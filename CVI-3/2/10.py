mn = int(input('zadaj od: '))
mx = int(input('zadaj do: '))

for i in range(mn, mx+1):
    print(f'{i:3} {i**2:6} {i**3:8} {i**4:10}')
