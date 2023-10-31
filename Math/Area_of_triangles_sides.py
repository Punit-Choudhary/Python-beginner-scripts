print("Calculate the area of triangle through sides \n")
s1 = float(input("Enter the value of A :"))
s2 = float(input("Enter the value of B :"))
s3 = float(input("Enter the value of C :"))
def Area(a,b,c):
    sp = (a + b + c)/2
    area = (sp)*(sp-a)*(sp-b)*(sp-c)
    f_area = round((area**0.5),2)
    print(f"{f_area}"+" square units")
Area(s1,s2,s3)
