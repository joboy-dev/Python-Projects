from operations import add, subtract, multiply, divide

def operate(first_number):
    
    result = 0
    
    while True:
        operation = input('Pick an operation: ')

        if operation == '+':
            second_number = int(input("What's the next number? "))
            result = add(first_number, second_number)
        elif operation == '-':
            second_number = int(input("What's the next number? "))
            result = subtract(first_number, second_number)
        elif operation == '*':
            second_number = int(input("What's the next number? "))
            result = multiply(first_number, second_number)
        elif operation == '/':
            second_number = int(input("What's the next number? "))
            result = divide(first_number, second_number)
        else:
            print('operation not supported. Try again.')
                
                        
        print(f'{first_number} {operation} {second_number} = {result}')
        
        return result