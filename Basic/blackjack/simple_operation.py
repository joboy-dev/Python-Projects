def operate_logic(player_cards, computer_cards):
    print(f"Your final hand: {player_cards}")
    print(f"Computer's final hand: {computer_cards}")
    
    sum_player_cards = sum(player_cards)
    sum_computer_cards = sum(computer_cards)
    
    if (sum_player_cards > sum_computer_cards) and sum_player_cards < 21:
        print('You Win')
    elif sum_player_cards == 21:
        print('Blackjack')
    elif sum_player_cards == sum_computer_cards:
        print('Push')
    else:
        print('You Lose')