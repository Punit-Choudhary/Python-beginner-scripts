def LCM(a,b):
    if a==1:
        print("The LCM is ",b)
    elif b==1:
        print("The LCM is ",a)
    else:
        n = max(a,b)
        for i in range (1,n+1):
            if a%i==0 and b%i==0:
                hcf = i
        lcm = (a * b)/hcf
        print("The LCM is ",lcm)  
        
a = int(input("Enter first number: "))
b = int(input("Enter Second number: "))
LCM(a,b)