n = int(input("zadaj n: "))

line = ""

for i in range(1, n+1):
    line += "*"*i + " "

print(line)
