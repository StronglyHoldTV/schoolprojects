def priemer(meno_suboru):
    with open(meno_suboru, 'r') as file:
        a = []
        for line in file:
            a.append(int(line))
        return sum(a)/len(a)


print("priemer =" ,priemer('cisla.txt'))
