s = 'Sedí mucha na stene, sedí a spí.'
h = input('zadaj samohlasky: ')
a = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'y' ,'ý']
for i in h:
    for j in a:
        s = s.replace(j, i)
    print(s)
