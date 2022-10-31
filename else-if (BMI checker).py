#initialisation 
weight = 0
height = 0 
BMI = 0 

#variable 1 
weight = float(input("what is your weight in KG? "))
height = float(input("what is your height in meters? "))

#variable 2 
BMI = weight / (height**2)

#checking of BMI 
if BMI >= 25 : 
    print("you are overweight")
else :
    print("you are ok")
