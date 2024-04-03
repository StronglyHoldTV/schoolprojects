import re

veta = input('Zadaj vetu')

slova = re.findall('\w+',veta)

print(f'najdlhsie slovo = {max(slova, key = len)}')
