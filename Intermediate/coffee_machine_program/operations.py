from data import espresso, cappuccino, latte, resources

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']

def resource_check(drink):
    '''Function to perform resource check'''
    
    # access the global variables
    global water, milk, coffee
    
    # ESPRESSO
    if drink == 'espresso':
        # check for water availability
        if water >= espresso['ingredients']['water']:
            print('Sufficient water available')
            
            # deduct water from resource pool
            water -= espresso['ingredients']['water']
            print(water)
            
            # check for coffee availability
            if coffee >= espresso['ingredients']['coffee']:
                print('Sufficient coffee available')
                
                # deduct coffee from resource pool
                coffee -= espresso['ingredients']['coffee']
                print(coffee)
                return True
            else:
                print('Sorry, there is not enough coffee')
                return ''
    
        else:
            print('Sorry, there is not enough water')
            return ''    

    
    # LATTE
    elif drink == 'latte':
        # check for water availability
        if water >= latte['ingredients']['water']:
            print('Sufficient water available')
            
            # deduct water from resource pool
            water -= latte['ingredients']['water']
            print(water)
            
            # check for coffee availability
            if coffee >= latte['ingredients']['coffee']:
                print('Sufficient coffee available')
                
                # deduct coffee from resource pool
                coffee -= latte['ingredients']['coffee']
                print(coffee)
                
                # check for milk availability
                if milk >= latte['ingredients']['milk']:
                    print('Sufficient milk available')
                    
                    # deduct milk from resource pool
                    milk -= latte['ingredients']['milk']
                    print(milk)
                    return True
                else:
                    print('Sorry, there is not enough milk')
                    return ''
        
            else:
                print('Sorry, there is not enough coffee')
                return ''
    
        else:
            print('Sorry, there is not enough water')
            return ''

            
            
    # CAPPUCCINO
    elif drink == 'cappuccino':
        # check for water availability
        if water >= cappuccino['ingredients']['water']:
            print('Sufficient water available')
            
            # deduct water from resource pool
            water -= cappuccino['ingredients']['water']
            print(water)
            
            # check for coffee availability
            if coffee >= cappuccino['ingredients']['coffee']:
                print('Sufficient coffee available')
                
                # deduct coffee from resource pool
                coffee -= cappuccino['ingredients']['coffee']
                print(coffee)
                
                # check for milk availability
                if milk >= cappuccino['ingredients']['milk']:
                    print('Sufficient milk available')
                    
                    # deduct milk from resource pool
                    milk -= cappuccino['ingredients']['milk']
                    print(milk)
                    return True
                else:
                    print('Sorry, there is not enough milk')
                    return ''
        
            else:
                print('Sorry, there is not enough coffee')
                return ''
    
        else:
            print('Sorry, there is not enough water')
            return ''
    
    # NONE
    else:
        print('Drink not available. Try again')
        return False 


# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------


def get_report(drink):
    '''Function to get report for order'''
        
    if drink == 'espresso':
        print(f"Here's your report for {drink}\n")
        
        print(f"Water: {espresso['ingredients']['water']}ml")
        print(f"Coffee: {espresso['ingredients']['coffee']}g")
        print(f"Money: ${espresso['cost']}")
        
    elif drink == 'latte':
        print(f"Here's your report for {drink}\n")
        
        print(f"Water: {latte['ingredients']['water']}ml")
        print(f"Milk: {latte['ingredients']['milk']}ml")
        print(f"Coffee: {latte['ingredients']['coffee']}g")
        print(f"Money: ${latte['cost']}")
        
    elif drink == 'cappuccino':
        print(f"Here's your report for {drink}\n")
        
        print(f"Water: {cappuccino['ingredients']['water']}ml")
        print(f"Milk: {cappuccino['ingredients']['milk']}ml")
        print(f"Coffee: {cappuccino['ingredients']['coffee']}g")
        print(f"Money: ${cappuccino['cost']}")
        
    else:
        print('No report available for the drink requested. Try again.')
        

# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------


def process_payment(drink):
    '''Function to process payment'''
    
    # access the global variables
    global water, milk, coffee
    
    print("Before proceeding, NOTE the following:")
    print('1 quarter is equivalent to $0.25')
    print('1 dime is equivalent to $0.10')
    print('1 nickel is equivalent to $0.05')
    print('1 penny is equivalent to $0.01')
    
    while True:
        # catch exceptions
        try:
            quarters = int(input('How many quarters do you wish to insert? '))
            dimes = int(input('How many dimes do you wish to insert? '))
            nickels = int(input('How many nickels do you wish to insert? '))
            pennies = int(input('How many pennies do you wish to insert? '))
            
            total_amount_paid = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
            
            print(f"Amount paid: {total_amount_paid}")
            
            # ESPRESSO
            if drink == 'espresso':
                print(f"Cost of drink: ${espresso['cost']}")
                
                if total_amount_paid == espresso['cost']:
                    print(f'Here is your {drink}. Enjoy')
                    
                    return True
                
                elif total_amount_paid < espresso['cost']:
                    print(f"You owe a balance of ${espresso['cost'] - total_amount_paid}. Do you want to complete the balance?")
                    complete_balance = input("Type 'y' or 'n': ").lower()
                    
                    if complete_balance == 'y':
                        print(f"Balance of ${espresso['cost'] - total_amount_paid} paid.")
                        print(f'Here is your {drink}. Enjoy')
                        return True
                    else:
                        print('Re-allocating resources...')
                        
                        # add water to resource pool
                        water += espresso['ingredients']['water']
                        # print(water)
                        
                        # add coffee to resource pool
                        coffee += espresso['ingredients']['coffee']
                        # print(coffee)
                        
                elif total_amount_paid > espresso['cost']:
                    print(f'Here is your {drink}. Enjoy')
                    print(f"You receive a change of ${total_amount_paid - espresso['cost']}")
                    return True
            
            # LATTE
            elif drink == 'latte':
                print(f"Cost of drink: ${latte['cost']}")
                
                if total_amount_paid == latte['cost']:
                    print(f'Here is your {drink}. Enjoy')
                    return True
                
                elif total_amount_paid < latte['cost']:
                    print(f"You owe a balance of ${latte['cost'] - total_amount_paid}. Do you want to complete the balance?")
                    complete_balance = input("Type 'y' or 'n': ").lower()
                    
                    if complete_balance == 'y':
                        print(f"Balance of ${latte['cost'] - total_amount_paid} paid.")
                        print(f'Here is your {drink}. Enjoy')
                        return True
                    else:
                        print('Re-allocating resources...')
                        
                        # add water to resource pool
                        water += latte['ingredients']['water']
                        # print(water)
                        
                        # add coffee to resource pool
                        coffee += latte['ingredients']['coffee']
                        # print(coffee)
                        
                        # add milk to resource pool
                        milk += latte['ingredients']['milk']
                        # print(milk)
                        
                        return True
                        
                elif total_amount_paid > latte['cost']:
                    print(f'Here is your {drink}. Enjoy')
                    print(f"You receive a change of ${total_amount_paid - latte['cost']}")
                    return True
            
            # CAPPUCCINO
            elif drink == 'cappuccino':
                print(f"Cost of drink: ${cappuccino['cost']}")
                
                if total_amount_paid == cappuccino['cost']:
                    print(f'Here is your {drink}. Enjoy')
                    return True
                
                elif total_amount_paid < cappuccino['cost']:
                    print(f"You owe a balance of ${cappuccino['cost'] - total_amount_paid}. Do you want to complete the balance?")
                    complete_balance = input("Type 'y' or 'n': ").lower()
                    
                    if complete_balance == 'y':
                        print(f"Balance of ${cappuccino['cost'] - total_amount_paid} paid.")
                        print(f'Here is your {drink}. Enjoy')
                        return True
                    else:
                        print('Re-allocating resources...')
                        
                        # add water to resource pool
                        water += cappuccino['ingredients']['water']
                        # print(water)
                        
                        # add coffee to resource pool
                        coffee += cappuccino['ingredients']['coffee']
                        # print(coffee)
                        
                        # add milk to resource pool
                        milk += cappuccino['ingredients']['milk']
                        # print(milk)
                        
                elif total_amount_paid > cappuccino['cost']:
                    print(f'Here is your {drink}. Enjoy')
                    print(f"You receive a change of ${total_amount_paid - cappuccino['cost']}")
                    return True
            
            # NONE
            else:
                print('Invalid input. Try again.')
                
            return True
                
        except ValueError:
            print('Invalid input. Try again')
