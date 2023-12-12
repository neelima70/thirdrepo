def blackjack(*args):
    sum=0
    for i in range (len(args)):
        sum=sum+args[i]
        if sum>21 and args[i]==11:
            sum =sum-10
    if sum<21:
        print(sum)
    else:
        print('BUST')
blackjack(9,9,11)
