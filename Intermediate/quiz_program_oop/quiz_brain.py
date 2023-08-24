from data import question_data

class QuizBrain:
    
    def __init__(self):
        self.score = 0
        
    def calculate_score(self, user_ans, correct_ans, question_no):
        '''Function to calculate score from quiz'''
        
        # FOR DEBUGGING PURPOSES
        # print(f'Correct answer is {correct_ans}')
        # print(f'User answer is {user_ans}')
        
        # check if user answer and the correct answer are the same
        if user_ans == correct_ans:
            self.score += 1  # add 1
            
            print('You got it right')
            print(f'The correct answer was: {correct_ans}')
            print(f"Your current score is: {self.score}/{question_no+1}\n\n")
        else:
            if self.score == 0: 
                self.score = 0 
            else: 
                self.score = self.score
                
            print('That is wrong')
            print(f'The correct answer was: {correct_ans}')
            print(f"Your current score is: {self.score}/{question_no+1}\n\n")
            # exit()
        