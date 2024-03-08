def ity(a, b):
    with open(a, 'r', encoding='utf-8') as f:
        return f.readlines()[b].strip()
