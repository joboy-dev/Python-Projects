# SUM OF HEIGHT
height = []
sum_of_height = 0
count= 0

heights = input('Enter students height. Separate different students height with comma\n').split(',')
for i in heights:
    height.append(float(i))

for z in height:
    sum_of_height += z
    count += 1  # no of items in list 
    
print(sum_of_height)
print(count)

print(sum_of_height/count)
# print(round(sum(height)/len(height)))