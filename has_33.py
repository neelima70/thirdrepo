def has_33(*args):
    for i in range (len(args)):
        if args[i]==3:
            if args[i+1]==3:
                print('true')
                break
            else:
                print('false')
        else:
            continue
res=has_33(1,2,3,4,3,6)
