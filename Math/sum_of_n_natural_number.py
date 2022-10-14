n=int(input("Enter the number:"))     #to take input from user
sum=0    #variable to store the sum
for i in range(1,n+1):     #range work from 1 to n-1 if used range(1,n+1) so to use n we have to use range(1,n+1) 
    sum=sum+i         
print("The sum of",n,"natural number is:",sum)      #to print the sum