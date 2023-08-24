from data import question_data

class QuizBrain:
    
    def __init__(self):
        self.score = 0
        
    def calculate_score(self, user_ans, correct_ans):
        '''Function to calculate score from quiz'''
        
        # check if user answer and the correct answer are the same
        if user_ans == correct_ans:
            self.score += 1  # add 1
            
        else:
            if self.score == 0: 
                self.score = 0 
            else: 
                self.score = self.score  # leave score as the same
        
        return self.score