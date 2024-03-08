mn = int(input('zadaj od: '))
mx = int(input('zadaj do: '))

s = ''

for i in range(mn, mx+1):
    s += f'<{i}>'
print(s)
