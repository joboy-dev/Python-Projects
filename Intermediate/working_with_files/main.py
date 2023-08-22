# # open a file
# file = open("Intermediate\working with files\my_file.txt")

# # read from the file
# contents = file.read()

# print(contents)

# # close the file
# file.close()

# OR
# to prevent forgetting to close a file, do this:
# with open("Intermediate\working with files\my_file.txt") as f:
#     contents = f.read()
#     print(contents)

# -------------------------------------------
# -------------------------------------------

# # writing to a file. this will clear the file and replace with new text
# with open("Intermediate\working with files\my_file.txt", 'w') as f:
#     f.write('\nHello')

# -------------------------------------------
# ------------------------------------------- 

# appending text to a file
# writing to a file. this will clear the file and replace with new text
with open("Intermediate\working with files\my_file.txt", 'a') as f:
    f.write('\nHello')