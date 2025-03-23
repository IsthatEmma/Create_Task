import random
import time

quiz_questions = []
print("Hello! Welcome to the quiz! Let's do this!!")

def generate_quiz():
    quiz_questions = [] 
    for i in range(18):
        quiz_questions.append("What is 2+2?")
        quiz_questions.append("What is 4+4?")
    for i in range(18):
        quiz_questions.append("What is 6+6?")
    return quiz_questions

print(generate_quiz())
