def riadky_s_textom(meno_suboru, text):
    with open(meno_suboru, 'r') as f:
        for l in f:
            if text in l:
                print(l, end='')
