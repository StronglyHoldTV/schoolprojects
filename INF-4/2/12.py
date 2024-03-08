import re

veta = input("Zadaj vetu")

l = re.findall('(\w+)', veta)

print(max(l, key=len))


