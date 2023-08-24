from tkinter import *
from question_model import QuestionModel
from quiz_brain import QuizBrain
from data import question_data
import html
import random
import time

THEME_COLOR = "#375362"

class UI():
    
    def __init__(self):
        '''Class initialization code'''
        
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=40, pady=40)
        
        self.question_model = QuestionModel()
        self.quiz_brain = QuizBrain()
        
        self.question_no = 0
        self.score = 0
        
        self.total_questions = len(question_data)
        
    
    def load_ui(self):
        '''Function to load up the user interface'''
        
        # score label
        self.score_label = Label(text=f"Score: {self.score}", font=('Arial', 12, 'bold italic'), bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=2)
        
        # question canvas
        self.question_canvas = Canvas(width=400, height=300, bg='white', highlightthickness=0)
        self.question_text = self.question_canvas.create_text(200, 150, text='New question', font=('Arial', 14, 'italic'), anchor='center', justify='center', width= 350,fill='black')
        self.question_canvas.grid(row=1, column=0, columnspan=3, pady=40)
        
        # button images
        self.true_image = PhotoImage(file='Intermediate/GUI_quiz_app/images/true.png')
        self.false_image = PhotoImage(file='Intermediate/GUI_quiz_app/images/false.png')
        
        # buttons
        self.true_button = Button(image=self.true_image, highlightthickness=0, borderwidth=0, command=self.picked_true)
        self.true_button.grid(row=2, column=0)
        
        self.false_button = Button(image=self.false_image, highlightthickness=0, borderwidth=0, command=self.picked_false)
        self.false_button.grid(row=2, column=2)
        
        self.load_questions()
        
        self.window.mainloop()
        
        
    def load_questions(self):
        '''Function to load up questions in the UI'''
        
        # self.question_no = random.randint(0, len(question_data)-1)
        
        current_question = self.question_model.load_question(self.question_no)
        
        # debugging
        # print(current_question)
    
        if current_question:
            # unescape html entities from text
            question_text = html.unescape(current_question['question'])
            
            self.question_canvas.config(bg='white')
            self.question_canvas.itemconfig(self.question_text, text=f"{question_text}\n\n(True or False)", fill='black')
            
            return current_question
        else:
            self.question_canvas.config(bg='white')
            self.question_canvas.itemconfig(self.question_text, text=f'QUIZ OVER!\n\nYour final score is:\n{self.score}/{self.total_questions}', fill='black')
            self.score_label.config(text='')

    
    def picked_answer(self, user_answer):
        '''Function to run if user picked true for answer'''
        
        question = self.load_questions()
        
        if question['correct_answer'] == user_answer:
            self.question_canvas.config(bg='green')
            self.question_canvas.itemconfig(self.question_text, fill='white')
            
            self.score = self.quiz_brain.calculate_score(user_answer, question['correct_answer'])
            
            self.score_label.config(text=f'Score: {self.score}')
        else:
            self.question_canvas.config(bg='red')
            self.question_canvas.itemconfig(self.question_text, fill='white')
            
        self.question_no += 1
            
        self.window.after(1500, self.load_questions)
        
    
    def picked_true(self):
        '''Function to run if user picked true for answer'''
        
        user_answer = 'True'
        self.window.after(500, self.picked_answer, user_answer)
        
        
    def picked_false(self):
        '''Function to run if user picked false for answer'''
        
        user_answer = 'False'
        self.window.after(500, self.picked_answer, user_answer)
        