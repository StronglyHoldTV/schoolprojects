def start(zoznam, n):
    return [x[:n] for x in zoznam]

mesiace = ['januar', 'februar', 'marec', 'april', 'maj',
               'jun', 'jul', 'august', 'september',
               'oktober', 'november', 'december']

print(start(mesiace, 3))
