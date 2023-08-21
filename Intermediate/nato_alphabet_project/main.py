import pandas as pd

alphabet_data = pd.read_csv('Intermediate/nato_alphabet_project/nato_phonetic_alphabet.csv', index_col='letter')
# print(alphabet_data)

alphabets = {
    key:value for key, value in alphabet_data.iterrows() 
}

alphabet_dict = {
    key:value.code for key, value in alphabets.items()
}
# print(alphabet_dict)

# Ask for a word
word = input('Enter a word: ').upper()

# store phonetic codes in list
phonetic_list = [alphabet_dict[letter] for letter in word]
print(phonetic_list)

