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


def assert_equals(actual, expected):
    assert actual == expected, f"Esperado: {expected}, obtenido: {actual}"

assert_equals(loose_change(29),  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1})
assert_equals(loose_change(91),  {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3})
assert_equals(loose_change(0),   {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
assert_equals(loose_change(-2),  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
assert_equals(loose_change(3.9), {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0})
                
print("¡Todos los tests superados!")

   