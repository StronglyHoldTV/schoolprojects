a = input('Retazec')
b = input('Podretazec')

def odstran(retazec, podretazec):
    text = ""
    c = retazec.split(podretazec)
    for i in c:
        text += i
    return (text, len(c))

print(odstran(a, b))
