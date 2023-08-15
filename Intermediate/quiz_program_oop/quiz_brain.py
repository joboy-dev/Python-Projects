from data import question_data

class QuizBrain:
    
    def calculate_score(self, user_ans, correct_ans, score, question_no):
        '''Function to calculate score from quiz'''
        
        # FOR DEBUGGING PURPOSES
        # print(f'Correct answer is {correct_ans}')
        # print(f'User answer is {user_ans}')
                    
        # check if user answer and the correct answer are the same
        if user_ans == correct_ans:
            # score += 1  # add 1
            score = question_no + 1
            print('You got it right')
            print(f'The correct answer was: {correct_ans}')
            print(f"Your current score is: {score}/{question_no+1}\n\n")
        else:
            score = question_no
            print('That is wrong')
            print(f'The correct answer was: {correct_ans}')
            print(f"Your current score is: {score}/{question_no+1}\n\n")
            exit()
        