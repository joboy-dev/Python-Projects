sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words = sentence.split(' ')

word_count_dict = {word:len(word) for word in words}

print(word_count_dict)