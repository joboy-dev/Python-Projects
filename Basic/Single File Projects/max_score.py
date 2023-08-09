# MAX SCORE
score = []
maximum_score = 0

scores = input('Enter students score. Separate different students score with comma\n').split(',')
for i in scores:
    score.append(float(i))
    
print(score)

for z in score:
    if z > maximum_score:
        maximum_score = z

print(f'Max score is {maximum_score}')