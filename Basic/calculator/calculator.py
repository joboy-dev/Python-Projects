from logo import logo
from calculate import operate

def calculate():
    print(logo)
    
    result = 0
    first_number = int(input("What's the first number? "))
    
    print('+\n')
    print('-\n')
    print('*\n')
    print('/\n')
    
    while True:
        result = operate(first_number)

        while True:
            user_query = input(f"Type 'y' to contnue calculating with {result}, or type 'n' to start a new calculation, or type 'exit' to close the calculator: ").lower()

            if user_query == 'y':
                first_number = result
                result = operate(first_number)
            elif user_query == 'n':
                calculate()
            else:
                print('Good bye. See you soon')
                exit()

calculate()
