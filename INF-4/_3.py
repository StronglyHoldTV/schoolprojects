##a  =  """Lorem ipsum dolor sit amet,
## consectetur adipiscing elit.
## Phasellus lobortis dui eu quam maximus,
## volutpat scelerisque ligula vulputate.
## Maecenas volutpat metus massa, et malesuada
## erat rutrum posuere. Curabitur vel eros nec
## dui iaculis bibendum eget vel massa."""
##
##def dlzka(re):
##    """Docu docu docu docu???"""
##    return len(re)
##
##r = input('Zadaj retazec: ')
##print('t' in r)
##print(dlzka(r))
##
##"asfasf".replace('a', 'b')

import re

def jeCislo(s: str):
    return True if re.match("[a-z]|[A-Z]", s) else False

def prveSlovo(s: str):
    return re.findall("^([\w\-]+)", s)
    
