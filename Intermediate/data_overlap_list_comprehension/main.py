with open('Intermediate/data_overlap_list_comprehension/file1.txt') as file_1:
    file_1_numbers = file_1.readlines()
    file_1_numbers_cleaned = [int(number.strip()) for number in file_1_numbers]
    print(file_1_numbers_cleaned)
    
with open('Intermediate/data_overlap_list_comprehension/file2.txt') as file_2:
    file_2_numbers = file_2.readlines()
    file_2_numbers_cleaned = [int(number.strip()) for number in file_2_numbers]
    print(file_2_numbers_cleaned)
    
# compare both lists for same numbers
same_numbers = [number for number in file_1_numbers_cleaned if number in file_2_numbers_cleaned]
print(same_numbers)
