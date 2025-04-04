import random
import time


quiz_questions = []
print("Hello! Welcome to the quiz! Let's do this!!")

def generate_quiz():
    quiz_question = ("First question! What is 2+2?")
    print(quiz_question)
    user_answer = input("Enter your answer: ")

    if user_answer == "4":
        print("Hooray! Thats correct! :D")
    else:
        print("No sorry!:( Thats incorrect")

    return quiz_question 
quiz_questions = generate_quiz()


def generate_quiz():
    quiz_question = ("Second question! What is 4+4?")
    print(quiz_question)
    user_answer = input("Enter your answer: ")

    if user_answer == "8":
        print("Amazing!! Correct again! :D")
    else:
        print("No sorry!:( Thats incorrect")

    return quiz_question 


quiz_questions = generate_quiz()

def generate_quiz():
    quiz_question = ("Third question! What is 7 x 2?")
    print(quiz_question)
    user_answer = input("Enter your answer: ")

    if user_answer == "14":
        print("Fantastic!! :D")
    else:
        print("No sorry!:(")

    return quiz_question 
quiz_questions = generate_quiz()


def generate_quiz():
    quiz_question = ("Last Question! What color is the sky")
    print(quiz_question)
    user_answer = input("Enter your answer: ")

    if user_answer == "blue":
        print("Double Amazing! You're on a winning streak!")
    else:
        print("Incorrect! :(")

    return quiz_question 
quiz_questions = generate_quiz()

print("Thanks for playing my mini quiz game! For all your hard work you get a medal! 🥇")
