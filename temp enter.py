temperature = []
days = ['mon','tues','weds','thurs','fri','sat','sun']

for temp in range(0,7) :
    temp_day = input(f"The temperature on {days[temp]} was :")
    temperature.append(temp_day)
for temp2, temp3 in enumerate(temperature) :
    print(f"Temperature on {days[temp2]} is {temperature[temp2]} degC")