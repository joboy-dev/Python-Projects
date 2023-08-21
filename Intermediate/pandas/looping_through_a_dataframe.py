import pandas as pd

student_dict = {
    'name': ['Angela', 'Joseph', 'Sam'],
    'score': [70, 87, 88]
}

student_df = pd.DataFrame(student_dict)

# looping through a data frame
for index, row in student_df.iterrows():
    print(index)
    print(row)