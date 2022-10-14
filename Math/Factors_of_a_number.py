# This program prints Factors of a number
# If the given number i perfectly divides a number n,
# then i is said to be a factor n 

def Factors(n):
    for i in range (1,n+1):
        if n%i==0:
            print(i,"is a factor of",n)

Factors(36)

