def najdlhsie(zoznam):
    return max(zoznam, key=len)

zoz = ['prvy', 'druhy', 'treti', 'stvrty', 'piaty']
print(najdlhsie(zoz))
