mn = int(input('zadaj od: '))
mx = int(input('zadaj do: '))

for i in range(mn, mx+1):
    line = f"{i:4} |"
    for j in range(mn, mx+1):
        if(i == mn):
            txt = " "*5 + "|"
            for k in range(mn, mx+1):
                txt += f"{k:5}"
            print(txt)
            print("="*5 + "|" + "="*(5*(mx-mn+1)))
        line+= f"{i*j:5}"
    print(line)
