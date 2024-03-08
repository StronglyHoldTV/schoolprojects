l = [1,2,3,4,5,8,9,10]
vzostupne = True
zostupne = True
konst = True
AP = True
k = l[1]-l[0] 
for no in range(0, len(l), 2):
    
    if l[no] < l[no+1]:
        zostupne = False
    if l[no] > l[no+1]:
        vzostupne = False
    if l[no] != l[no+1]:
        konst = False
    if(k != l[no+1]-l[no]):
        AP=False
    print(zostupne, vzostupne, konst, AP)
