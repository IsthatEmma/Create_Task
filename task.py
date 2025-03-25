import random
import time

quiz_questions = []
print("Hello! Welcome to the quiz! Let's do this!!")

def generate_quiz():
    question = "What is 2+2?"
    print(question)
    answer1 = input("Enter your answer: ")

    if answer1 == "4":
        print("Hooray! Thats correct! :D")
    else:
        print("No sorry!:( Thats incorrect")

    return question 


quiz_questions = generate_quiz()



