import os
import random
from art import logo, vs
from game_data import data

os.system('cls')
print(logo)

correct = False
score = 0

while True:
    if correct == True:
        print(f'You are right! Current score: {score}')
    
    # store random data in variables
    data_a = random.choice(data)
    data_b = random.choice(data)
    
    # check if both data gotten are the same
    if data_a['name'] != data_b['name']:
        # debugging
        # print(data_a)
        # print(data_b)
        
        print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}")
        print(vs)
        print(f"Against B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}")
        
        follower_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        follower_count_a = data_a['follower_count']
        follower_count_b = data_b['follower_count']
        
        if follower_answer == 'A':
            if follower_count_a > follower_count_b:
                os.system('cls')
                score += 1
                correct = True
            else:
                os.system('cls')
                print(logo)
                print(f'Sorry, that is wrong. Final score: {score}')
                exit()            
                
        elif follower_answer == 'B':
            if follower_count_b > follower_count_a:
                os.system('cls')
                score += 1
                correct = True
            else:
                os.system('cls')
                print(logo)
                print(f'Sorry, that is wrong. Final score: {score}')
                exit()
                
        else:
            print('Invalid input. Try again.')
            
    else:
        print('Loading fresh data...')
    
