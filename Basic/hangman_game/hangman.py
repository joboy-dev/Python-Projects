import random
import hangman_words, hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6

print(hangman_art.logo)

#Create blanks
display = []

for i in range(len(chosen_word)):
    display.append('_')
    
print('  '.join(display))

while '_' in display:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        
        # check if the guess is a letter in the chosen word
        if letter == guess:
            display[position] = letter
        elif guess in display:
            print(f"You have guessed this letter '{guess}'")
            
            
    # check if guess is not in chosen word so as to remove a life
    if guess not in chosen_word:
        print(f"Letter '{guess}' not in chosen word. You lose a life")
        lives -= 1
        if lives == 1:
            print(f'You have {lives} life left')
        else:
            print(f'You have {lives} lives left')
    
    # check if lives jas tun down to zero
    if lives == 0:
        print(hangman_art.stages[lives])
        print('You lose.')
        print(f'The word is {chosen_word}')
        break
    
    print(hangman_art.stages[lives])

    print('  '.join(display))

else:
    print('You win')
