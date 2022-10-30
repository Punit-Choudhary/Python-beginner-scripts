def ctom():
     cm = float(input("Enter value in centimetres:"))
     m=cm/100
     print("The corresponding value in meters is:",m)
     return
 
def mtoc():
     m = float(input("Enter value in meters:"))
     cm =m*100
     print("The corresponding value in centimetres is:",cm)
     return
 
    
def main():
    option=0
    while(option!=3):
        print("\nMENU")
        print("Enter the conversion you want to do:")
        print("1.centimetres to meters")
        print("2.meters to centimetres")
        print("3.Exit")
        option = int(input("Enter your choice:"))
        if (option==1):
            ctom()
        if (option==2):
            mtoc()
        elif (option==3):
            print("THANK YOU!")
main()
