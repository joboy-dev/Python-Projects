from data import question_data
import random

class QuestionModel:
    
    def __init__(self):
        # self.questions_answered = 0
        self.answered_questions = []
        

    def load_question(self, question_no):
        '''Function to load up the quiz questions'''
        
        if question_no != len(question_data):
            question = question_data[question_no]
            # self.answered_questions.append(question['question'])
            # print(self.answered_questions)
            return question
        else:
            return False
            