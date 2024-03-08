import re

with open(input("Zadaj nazov suboru."), "r") as file:
    x = file.read().replace('\n', ' ').strip()
    print(repr(x))
    a = 0
    print(len(re.findall(r'\w+', x)))
    for i in x:
        if(i.isalpha()):
            a += 1
    print(a)
    print(max(re.findall(r'\w+', x), key = len))
    
    
