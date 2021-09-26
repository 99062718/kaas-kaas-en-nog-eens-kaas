import random
import time

character = "hero"

#to do: make function for putting questions on screen and automatically choose answerCheck or answerCheckAlternate, give ability to check current health during levels without having to get hit

def theInfoDumper(info):
    for x in info:
        print(x)
        time.sleep(6)

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
        return ["What is " + str(randomNumber2) + " * " + str(randomNumber3) + "? ", randomNumber2 * randomNumber3]

def diffselect():
    global difficulty
    global numberOfOperators
    global additionSubtractionNumber
    global multiplicationNumber

    difficulty = input("Enter the difficulty you would like to play on (easy, medium or hard): ").lower()
    if difficulty == "easy":
        numberOfOperators = 4
        additionSubtractionNumber = 100
        multiplicationNumber = 20
    elif difficulty == "medium":
        numberOfOperators = 4
        additionSubtractionNumber = 1000
        multiplicationNumber = 100
    elif difficulty == "hard":
        numberOfOperators = 5
        additionSubtractionNumber = 5000
        multiplicationNumber = 500
    else:
        print("This is not a possible difficulty!")
        diffselect()

diffselect()

if character == "hero": #to do: Add forrest path first, Log level
    theInfoDumper([
        "There was once a village. A village like any other village. A village with inhabitants like any other village. A village with troubles like any other village had.",
        "None would have ever expected what could have come out of a village like any other. A hero who would one day slay all evil that threatened the land. A hero that would bring hope to any in dispair.",
        "Until that day arives, the inhabitants of this world must deal with what evil god throws at them.",
        "In another village close to the village like any other, a boy resides. This boy was really like any boy inside that village, with the exception for his above avarage performance with the blade.",
        "The boy had one goal in life: Become a member of the elite swordsmen that guarded the royal family. It was a comfortable life inside the walls of the castles. Much better than what the villages were like.",
        "One day the boy had a chance. A less prominent member of the royal family had been kidnapped on their way to one of the capital of the country. If he could find them and strike down the people that kidnapped them, they might land him a job in a lesser castle. From where he could then work up to the royal family.",
        "And so the boy set out on an adventure. To find and rescue the royal member from certain doom!\n"
    ])