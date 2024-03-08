den = ['pondelok','utorok','streda','stvrtok','piatok', 'sobota', 'nedela']
day = ['Monday', 'Tuesday', 'Wensday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(*den, sep=', ')
print(*day, sep=', ')

for i in range(0, len(den)):
    print(den[i], day[i], sep=', ')
