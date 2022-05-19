 
# Python program to find Area of a circle 
  
def findArea(r): 
    PI = 3.142
    return PI * (r*r); 
  
# Driver method
num=float(input("Enter r value:"))
print("Area is %.6f" % findArea(num)); 
 
