import random
from levels import easy, hard

while True:
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of anumber between 1 to 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    number_to_guess = random.randint(1, 100)

    if difficulty == 'easy':
        easy(number_to_guess)
        break
    elif difficulty == 'hard':
        hard(number_to_guess)
        break
    else:
        print('Invalid input. Try again.')

