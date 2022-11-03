#initialisation 
limousine_fare = float(0)
Taxi_fare = float(0)
Bus_fare = float(0)
MRT_fare = float(0)




#menu interface
print("Fare calculator - Changi Airport to City")
print("please choose transport mode")
print("a - limousine $55.00")
print("b - Taxi - $30.00")
print("c - Bus $2.50")
print("d - MRT $2.00")

#variables 
limousine_fare = float(55.00)
Taxi_fare = float(30.00)
Bus_fare = float(2.50)
MRT_fare = float(2.00)

#user input 
user_input = input("please select a transport mode (a,b,c,d): ")
if user_input == "a" or user_input =="A" :
    print(f"You have selected Limousine, the fare is ${limousine_fare:.2f} to city")    # :.2f makes in 2d.p.
elif user_input == "b" or user_input =="B" :
    print(f"you have selected Taxi, the fare will be ${Taxi_fare:.2f} to city")
elif user_input == "c" or user_input =="C" :
    print(f"you have selected Bus, the fare will be ${Bus_fare:.2f} to city")
elif user_input == "d" or user_input =="D" :
    print(f"you have selected MRT, the fare will be ${MRT_fare:.2f} to city")
else :
    print("invalid selection. No fare calculated")

# to be printed regardless
print("thank you and goodbye")
