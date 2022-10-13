#this function is used to calculate the curved 
#surface area for a cylinder
def CSA()
#radius of the cylinder taken as input
R = int(input("Enter the radius of the cylinder: "))
#height of the cylinder taken as input
H = int(input("Enter the height of the cylinder: "))
#formula to calculate curved surface
#area of cylinder
curved_surface_area = (2*22*(R * H))/7   
print ("the Curved Surface Area of the cylinder is: ", curved_surface_area);   
CSA()