import random
from simple_operation import operate_logic

while True:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    cards_pool = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    player_cards = []
    computer_cards = []

    if play == 'y':
        for i in range(2):
            player_cards.append(random.choice(cards_pool))
            computer_cards.append(random.choice(cards_pool))
        
        print(f"Your cards: {player_cards}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        while True:
            get_another_card = input("Type 'y' to get another card, type n to pass: ")
            
            if get_another_card == 'y':
                player_cards.append(random.choice(cards_pool))
                operate_logic(player_cards, computer_cards)
                break
            elif get_another_card == 'n':
                operate_logic(player_cards, computer_cards)
                break
            else:
                print('Invalid input. Try again')

    elif play == 'n':
        print('Bye. See you later')
        exit()
    else:
        print('Invalid input. Try again.')