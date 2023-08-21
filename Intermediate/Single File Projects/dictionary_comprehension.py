import random
names = ['Alex', 'Sam', 'Jude', 'Tom', 'Dominic', 'Sarah', 'Joy']

students_score = {name:random.randint(1, 100) for name in names}

print(students_score)

passed_students = {
    name:score for name, score in students_score.items() if score >= 50
}

print(passed_students)