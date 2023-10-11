def ozatvorkuj(retazec, podretazec):
    retazec = retazec.replace(podretazec, "("+podretazec+")")
    return retazec


print(ozatvorkuj('Bratislava', 'a'))
