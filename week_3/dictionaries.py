pizza_pref = [{'name': 'sandeep', 'toppings': 'mushrooms', 'pizza_type': 'round'},
            {'name': 'kylie', 'toppings': ['ham', 'pineapple'], 'pizza_type': 'square'},
            {'name': 'lisa', 'toppings': ['mushrooms', 'pepperoni'], 'pizza_type': 'square'},
            {'name': 'dan', 'toppings': ['bacon', 'sausage', 'pepperoni'], 'pizza_type': 'square'}]

print(pizza_pref)

for person in pizza_pref: 
    mushrooms_found = False

    if type(person['toppings']) is str:
        if(person['toppings']) == 'mushrooms':
            mushrooms_found = True 
    elif type(person['toppings']) is list: 
        if('mushrooms' in person['toppings']):
            mushrooms_found = True
    
    if mushrooms_found: 
        pizza_pref.remove(person)

print(pizza_pref)