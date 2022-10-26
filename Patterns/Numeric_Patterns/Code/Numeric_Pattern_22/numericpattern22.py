x= int(input())
if x%2==0:
    for i in range(0,int(x/2)):
        print('1'*x)
        print('0'*x)        
elif x%2!=0:
    for i in range(0,x//2):
        print('1'*x)
        print('0'*x)
    print('1'*x)

