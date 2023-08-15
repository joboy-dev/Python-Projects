from data import question_data
from quiz_brain import QuizBrain

class QuestionModel:
        
    def load_questions(self):
        '''Function to load up the quiz questions'''
        
        # initialize quiz brain class
        quiz_brain = QuizBrain()
        score = 0
        
        for question in range(len(question_data)):
            correct_answer = question_data[question]['answer']
            current_question = question_data[question]['text']
            user_answer = input(f"Q.{question+1}: {current_question} (True/False)? ").capitalize()
            
            # call function to calculate score
            quiz_brain.calculate_score(user_answer, correct_answer, score, question)
            