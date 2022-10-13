#this function is used to calculate the curved 
#surface area for a cone
def CSA()
#radius of the cone taken as input
R = int(input("Enter the radius of the cone: "))
#slant height of the cone taken as input
L = int(input("Enter the slant height of the cone: "))
#formula to calculate curved surface area of cone
curved_surface_area = (22*(R * L))/7   
print ("the Curved Surface Area of the cone is: ", curved_surface_area);   
CSA()