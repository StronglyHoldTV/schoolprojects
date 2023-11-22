def posledny_riadok(s):
    with open(s, 'r', encoding='utf-8') as f:
        return f.readlines()[len(f.readlines()) - 1].strip()
def predposledny_riadok(s):
    with open(s, 'r', encoding='utf-8') as f:
        return f.readlines()[len(f.readlines()) - 2].strip()
def najdlhsi_riadok(s):
    with open(s, 'r', encoding='utf-8') as f:
        return max(f.readlines(), key = len).strip()
    
    
