import random
import time

score = 0 

quiz_questions = []
print("Hello! Welcome to the quiz! Let's do this!!")

def generate_quiz():
    quiz_question = ("First question! What is 2+2?")
    print(quiz_question)
    user_answer = input("Enter your answer: ")

    if user_answer == "4":
        score +=1
        print("Hooray! Thats correct! :D")
    else:
        print("No sorry!:( Thats incorrect")

    return quiz_question 

quiz_questions = create_quiz()


def generate_quiz():
    quiz_question = ("Second question! What is 4+4?")
    print(quiz_question)
    user_answer = input("Enter your answer: ")

    if user_answer == "8":
        score +=1
        print("Amazing!! Correct again! :D")
    else:
        print("No sorry!:( Thats incorrect")

    return quiz_question 


quiz_questions = create_quiz()

def generate_quiz():
    quiz_question = ("Second question! What is 7 x 2?")
    print(quiz_question)
    user_answer = input("Enter your answer: ")

    if user_answer == "14":
        score +=1
        print("Fantastic!! :D")
    else:
        print("No sorry!:(")

print("You got " + str(score) + "/3")
return quiz_question 

quiz_questions = create_quiz()

print("Thanks for playing!")