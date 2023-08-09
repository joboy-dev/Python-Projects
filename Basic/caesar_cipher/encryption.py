from utils import alphabet, continuation

continuing_game = continuation

def encrypt(text, shift):
    # using list comprehension to create a new list free of any white spaces
    alphabet_list = [item for item in alphabet if item != ' ']
    
    encrypted_list = []
    
    # create a copy of the original list
    encrypted_alphabet_list = alphabet_list.copy()
    
    # use list slicing to get a hold of the elements you want to remove from the list and store in a variable
    popped_items = encrypted_alphabet_list[0:shift]
    encrypted_alphabet_list[0:shift] = []
    
    # extend the removed items into the encrypted_alphabet_list list
    encrypted_alphabet_list.extend(popped_items)
    
    print(text)
    
    for letter in text:
        if letter == ' ':
            alphabet_list.append(' ')
            encrypted_alphabet_list.append(' ')
            
        # get the index of all the letters in the alphabet list so as to use that index in the alphabet copy list
        index_position = alphabet_list.index(letter)
        
        # debugging
        print(index_position)
        print(encrypted_alphabet_list[index_position])
        
        encrypted_list.append(encrypted_alphabet_list[index_position])
        
    print(encrypted_list)
        
    # debigging
    print('ALPHABET COPY LIST')
    print(encrypted_alphabet_list)
    
    print('ALPHABET ORIGINAL LIST')
    print(alphabet_list)
    
    print(f"The encrypted message is {''.join(encrypted_list)}")
    
    answer = input("Type 'yes' if you wish to continue and 'no' if you wish to stop: ").lower()
    
    if answer == 'yes':
        continuation = True
    else:
        print('Thanks for using Caeasr Cipher. Come back later')
        exit()