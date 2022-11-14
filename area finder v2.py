#menu interface 
print("=" * 40)
print("Calculate Area")
print("Please choose one of the following: ")
print("A or a - area of a rectangle")
print("B or b - area of a right angle triangle")
print("C or c - area of a circle")
print("Q or q - quit")
print("=" * 40)

#start of loop 
temp = True

while temp : 
    choice = input("please select an option: ")
    if choice == "A" or choice == "a" :
        length = float(input("please enter the length of the rectangle (in m): "))
        width = float(input("please enter the width of the rectangle (in m): "))
        area = length * width 
        print(f"The area of the rectangle is {area:.1f}m^2")
    elif choice == "B" or choice == "b" : 
        base = float(input("please enter the base length of the triangle (in m): "))
        height = float(input("please enter the height of the triangle (in m): "))
        area = 0.5 * base *height
        print(f"The area of the triangle is {area:.1f}m^2") 
    elif choice == "C" or choice == "c" :
        radius = float(input("please enter the radius of the circle (in m): "))
        area = 3.142 * radius**2
        print(f"The area of the circle is {area:.1f}m^2")
    elif choice == "Q" or choice == "q" :
        print("thank you for using the system")
        print("goodbye")
        break
    else : 
        print("invalid option, please select A,B,C or Q")


