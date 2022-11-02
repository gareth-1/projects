#initialisation 
product_price = 0 
weight = 0 
total_price = 0 
shipping_cost = 0 
shipping_price = 0 #price if weight under 20kg 
shipping_price2 = 0 #price for every kg after 20kg 
weight_over_20kg = 0
weight_over_50kg = 0 
shipping_price3 = 0 

#user input code 
product_price = float(input("what is the price of the product? "))
weight = float(input("what is the weight of the product in KG? "))

#variables 
shipping_price = float(2.50)
shipping_price2 = float(1.75)
shipping_price3 = float(2.15)
weight_over_20kg = float(weight - 20)
weight_over_50kg = float(weight - 50)





#shipping cost calculation + output code 
if weight <= 20 : 
    shipping_cost = float(weight*shipping_price )
    total_price = float(product_price + shipping_cost)
    print(f"The total cost is ${total_price:.2f} , with a shipping cost of ${shipping_cost:.2f}")
elif weight <50 :
    shipping_cost = float((shipping_price*20) + (shipping_price2*weight_over_20kg))
    total_price = float(product_price + shipping_cost)
    print(f"The total cost is ${total_price:.2f} , with a shipping cost of ${shipping_cost:.2f}")
elif weight >50 :
    shipping_cost = float(weight*2.15)
    total_price = float(product_price + shipping_cost)
    print(f"the total cost is ${total_price:.2f} with a shipping_cost of ${shipping_cost:.2f}")