#initial values 
length = 0
width = 0 
area = 0 
perimeter = 0 
#user input and computing 
length = int(input("length of rectangle in cm:"))
width = int(input("width of rectangle in cm:")) 
area = length*width 
perimeter = length*2 + width*2
print(area , "cm^2" , "and perimeter", perimeter)