def loose_change(cents):
    change_dict = {
        'Pennies' : 0,
        'Nickels' : 0,
        'Dimes' : 0,
        'Quarters' : 0
    }
    if cents <= 0:
        return change_dict
    
    cents = int(cents)
    coins = ['Quarters', 'Dimes', 'Nickels', 'Pennies']
    values = [25, 10, 5, 1]
        
    for i in range(4):
        change_dict[coins[i]] = cents // values[i]
        cents %= values[i]
    return change_dict
    
                
   
    