def easy(number):
    '''Easy level'''
    
    attempts = 10
    print(f'You have {attempts} attempts remaining to guess the number')
    
    while True:
        try:
            guess = int(input('Make a guess: '))
            
            # check whether guess is too high or too low 
            if guess > number:
                attempts -= 1
                print('Too high')
            elif guess < number:
                attempts -= 1
                print('Too low')
            if guess == number:
                print('You have guessed the correct number. Congratulations.')
                exit()
            
            print('Guess again')
            
            # perform checks on attempts
            if attempts > 1:
                print(f'You have {attempts} attempts remaining to guess the number')
            elif attempts == 1:
                print(f'You have {attempts} attempt remaining to guess the number')
            elif attempts == 0:
                print(f'You have run out of attempts')
                exit()
        except ValueError:
            print("Sorry. Try again.")
    

def hard(number):
    '''Hard level'''
    
    attempts = 5
    print(f'You have {attempts} attempts remaining to guess the number')
    
    while True:
        try:
            guess = int(input('Make a guess: '))
            
            # check whether guess is too high or too low    
            if guess > number:
                attempts -= 1
                print('Too high')
            elif guess < number:
                attempts -= 1
                print('Too low')
            if guess == number:
                print('You have guessed the correct number. Congratulations.')
                exit()
            
            print('Guess again')
            
            # perform checks on attempts
            if attempts > 1:
                print(f'You have {attempts} attempts remaining to guess the number')
            elif attempts == 1:
                print(f'You have {attempts} attempt remaining to guess the number')
            elif attempts == 0:
                print(f'You have run out of attempts')
                exit()
        except ValueError:
            print("Sorry. Try again.")
            