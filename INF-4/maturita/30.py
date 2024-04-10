def d():
    with open('znamky.txt', 'r') as file:
        meno = input('meno')
        for line in file:
            name = line.strip()
            znamky = file.readline().strip().split(' ')

            if(name.lower() != meno.lower()):
                continue
            print('nezmaturoval'if '5' in znamky else 'zmaturoval')

while True:
    d()
