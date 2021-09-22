import random

#to do: numberOfOperators, difficulty

def answerCheck(userAnswer, correctAnswer):
    if userAnswer == correctAnswer:
        return 1
    elif userAnswer - correctAnswer <= 20 and userAnswer - correctAnswer >= 1 or correctAnswer - userAnswer <= 20 and correctAnswer - userAnswer >= 1:
        return 2
    elif userAnswer != correctAnswer:
        return 3

def answerCheckAlternate(userAnswer, question):
    if userAnswer > question:
        return 1
    elif userAnswer < question:
        return 2
    else:
        return 3

def healthCheck(currentHealth):
    if difficulty == "easy":
        return currentHealth - 3
    elif difficulty == "medium":
        return currentHealth - 5
    else:
        return 0

def questionMaker():
    randomNumber = random.randint(1, numberOfOperators)
    if randomNumber == 0:
        