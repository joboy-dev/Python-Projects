# open gile with all the names
with open('Intermediate/mail_merge_project/Input/Names/invited_names.txt', 'r') as names_file:
    # store all names as a list in a variable
    names_file_lines = names_file.readlines()
    
    # clean the list by removing all whitespaces
    clean_name_list = [item.strip() for item in names_file_lines]
    
    # debugging
    # print(clean_name_list)
    
    # loop through the list of names
    for name in clean_name_list:
        # print(name)
        
        # open starting letter
        with open('Intermediate/mail_merge_project/Input/Letters/starting_letter.txt', 'r') as initial_letter:
            content = initial_letter.read()
            
            # modify content of the original file and store in a variable
            modified_content = content.replace('[name]', name)
            
            # debugging
            # print(modified_content)
            
        with open(f'Intermediate/mail_merge_project/Output/ReadyToSend/letter_for_{name}.txt', 'w') as final_letter:
            # write modified content to the appropriate file
            final_letter.write(modified_content)