with open('hodiny.txt', 'r') as file:
    with open('ospravedlnene.txt', 'w') as o:
        with open('neospravedlnene.txt', 'w') as n:
            for line in file:
                name = line.strip()
                ospr = int(file.readline().strip())
                neospr = int(file.readline().strip())
                if neospr == 0:
                    print(f'{name} {ospr+neospr}', file = o)
                else:
                    print(f'{name} {ospr+neospr}', file = n)
