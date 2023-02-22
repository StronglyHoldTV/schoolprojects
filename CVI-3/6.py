import random
for _ in range(10):
    slovo = ''
    for i in range(3):
        spolu = 'bcdfghjklmnprstvxz'
        samo = 'aeiouy'
        slovo+= random.choice(spolu) + random.choice(samo)
    print(slovo)
