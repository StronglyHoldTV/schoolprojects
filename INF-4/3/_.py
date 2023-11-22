with open('cvicny.txt', 'r') as subor:
    with open('cvicny2.txt', 'w') as subor2:
        #subor2.write(subor.read())
        print(subor.read(), file=subor2)
with open('cvicny2.txt', 'a') as s:
    print("Hello", file=s)

with open('cvicny2.txt', 'r') as r:
    print(repr(r.read()))
