def reversestr(name):
    list1=[]
    s=-1
    for i in range(len(name)):
        list1.append(name[s])
        s=s+(-1)
    return ''.join(list1)
def splitt(name1):
    res1=name1.split()
    list2=[]
    for x in range (len(res1)):
        list2.append(reversestr(res1[x]))
    return ' '.join(list2)
res=reversestr('I am home')
res3=splitt(res)
print(res3)
        
        
