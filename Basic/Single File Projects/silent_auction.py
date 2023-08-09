import os

auction_dictionary = {}
continuation = True

logo = '''
 #####                                     #                                        
#     # # #      ###### #    # #####      # #   #    #  ####  ##### #  ####  #    # 
#       # #      #      ##   #   #       #   #  #    # #    #   #   # #    # ##   # 
 #####  # #      #####  # #  #   #      #     # #    # #        #   # #    # # #  # 
      # # #      #      #  # #   #      ####### #    # #        #   # #    # #  # # 
#     # # #      #      #   ##   #      #     # #    # #    #   #   # #    # #   ## 
 #####  # ###### ###### #    #   #      #     #  ####   ####    #   #  ####  #    # 
'''

while continuation:
    print(logo)
    name = input('What is your name? ')
    bid = int(input('How much are you bidding? $'))
    
    auction_dictionary.update({name:bid})
    
    another_bid = input("Type 'yes' is there is another bid and 'no' if there is none: ").lower()
    
    if another_bid == 'yes':
        # clear terminal screen
        os.system('cls')
        continuation = True
    else:
        # get the maximum value's key ie the name
        max_key = max(auction_dictionary, key=auction_dictionary.get)
        
        # get the max value based on the key gotten above
        max_value = auction_dictionary[max_key]
        
        print(f'The highest bid goes to {max_key} with a bid of ${max_value}')
        
        continuation = False
        print('Thanks for bidding. See you next time')
            
            
        
        