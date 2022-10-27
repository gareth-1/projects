#initialise 
mass = 0.0
radius = 0.0 
inertia = 0.0 

#user inputs  
mass = float(input("what is the mass in KG? "))
radius = float(input("what is the radius in M? "))

#inertia calculation 
inertia = 0.5*mass*radius**2

#outputs
print("inertia of the disk" , inertia)