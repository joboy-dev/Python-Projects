from data import espresso, cappuccino, latte
from operations import resource_check, get_report, process_payment
    

while True:
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()

    # check if resources are sufficient for the drink
    check = resource_check(choice)
    
    # check if return value is True. if it is, proceed to next stage of ordering
    if check:
        while True:
            # get report
            report_request = input("Type 'report' to get a description of your order: ")
            
            if report_request == 'report':
                get_report(choice)
                break
            else:
                print('Invalid input. Try again')
        
        # process coins
        payment = process_payment(choice)
        
        while True:
            # check if payment is complete or not. payment will be true if it is compelete
            if payment:
                maintainer_input = input("Type 'redo' to take another customer's order, type 'off' to turn off the machine: ").lower()
                
                if maintainer_input == 'redo':
                    break
                elif maintainer_input == 'off':
                    exit()
                else:
                    print('Invalid input. Try again')
                
            else:
                break
    elif check == '':
        exit()


