main_capacity_of_tank = 3606
time_required_to_fill_one_bottle = 1 # min
working_time_in_a_day = 12*60 # 720 min
capacity_of_one_bottle= 1 # liter

bottle_filled = 0
day_number = 1
while True:
    bottles_can_filled_in_one_day = working_time_in_a_day/time_required_to_fill_one_bottle
    max_capacity_can_filled_in_one_day = bottles_can_filled_in_one_day*capacity_of_one_bottle
    bottle_filled= bottle_filled + 1
    capacity_filled_in_one_day= bottle_filled*capacity_of_one_bottle
    main_capacity_of_tank = main_capacity_of_tank - capacity_of_one_bottle
    if(capacity_filled_in_one_day==max_capacity_can_filled_in_one_day):
        
        print(f'Day {day_number} , Botlles filled', bottle_filled)
        day_number = day_number+1
        bottle_filled = 0
      
    
    if(main_capacity_of_tank==0):
        print(f'Day {day_number} , Botlles filled', bottle_filled)
        print("Filling done!!")
        break


