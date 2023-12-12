def paper_doll(name):
    list1=[]
    for i in range (len(name)):
        x=1
        while x<=3:
            list1.append(name[i])
            x=x+1
    return ''.join(list1)
res=paper_doll('hello')
print(res)
        
        
