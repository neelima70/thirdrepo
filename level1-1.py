def old_mcdonald(name):
    list=[]
    for i in range(len(name)):
        if i==0:
            list.append(name[i].upper())
        elif i==3:
            list.append(name[i].upper())
        else:
            list.append(name[i])
    return ''.join(list)
res=old_mcdonald('neelima')
print(res)
