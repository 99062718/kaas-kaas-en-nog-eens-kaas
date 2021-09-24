import random

#to do: numberOfOperators, difficulty, additionSubtractionNumber

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
    if randomNumber == 1 or randomNumber == 2:
        randomNumber2 = random.randint(1, additionSubtractionNumber)
        randomNumber3 = random.randint(1, additionSubtractionNumber)
        return ["What is " + str(randomNumber2) + " + " + str(randomNumber3) + "? ", randomNumber2 + randomNumber3] if randomNumber == 1 else ["What is " + str(randomNumber2) + " - " + str(randomNumber3) + "? ", randomNumber2 - randomNumber3]
    elif randomNumber == 3 or randomNumber == 4:
        randomNumber2 = random.randint(1, additionSubtractionNumber)
        return ["Name a number higher than " + str(randomNumber2) + ": ", randomNumber2] if randomNumber == 3 else ["Name a number lower than " + str(randomNumber2) + ": ", randomNumber2]
    elif randomNumber == 5:
        randomNumber2 = random.randint(1, multiplicationNumber)
        randomNumber3 = random.randint(1, multiplicationNumber)
        return ["What is " + str(randomNumber2) + " * " + str(randomNumber3) + "? ", randomNumber2 + randomNumber3]