import random
import time

characters = ["hero"]
maxHealth = 15
health = 15
damageMultiplier = 1

#to do: currently empty!

#---------------------------------------------------------------------------------------------------//Functions entire game needs to work.

#------------------------------------//Question makers and checkers

def questionChecker(listOfOutcomes, bosshealth=0): #print question and asks for input. then checks if answerCheck or answerCheckAlternate needs to be used
    questionAndAnswer = questionMaker()

    answer = int(input(questionAndAnswer[0]))

    if isAlternate == "no":
        correctOrNot = answerCheck(answer, questionAndAnswer[1])
    else:
        correctOrNot = answerCheckAlternate(answer, questionAndAnswer[1], questionAndAnswer[2])

    if correctOrNot == 1:
        print(listOfOutcomes[0])
        if bosshealth > 0:
            bosshealth -= 3 * damageMultiplier
    else:
        healthCheck(listOfOutcomes[3])
        a = print(listOfOutcomes[1]) if correctOrNot == 2 else print(listOfOutcomes[2])
        print("Health: " + str(health) + "/" + str(maxHealth))

def questionMaker(): #makes questions by choosing an operator based on a random number
    global isAlternate
    randomNumber = random.randint(1, numberOfOperators)
    if randomNumber is not(3 or 4):
        isAlternate = "no"
    else:
        isAlternate = "yes"
    
    if randomNumber == 1 or randomNumber == 2:
        randomNumber2 = random.randint(1, additionSubtractionNumber)
        randomNumber3 = random.randint(1, additionSubtractionNumber)
        return ["What is " + str(randomNumber2) + " + " + str(randomNumber3) + "?\n", randomNumber2 + randomNumber3] if randomNumber == 1 else ["What is " + str(randomNumber2) + " - " + str(randomNumber3) + "?\n", randomNumber2 - randomNumber3]
    elif randomNumber == 3 or randomNumber == 4:
        randomNumber2 = random.randint(1, additionSubtractionNumber)
        return ["Name a number higher than " + str(randomNumber2) + "\n", randomNumber2, "higher"] if randomNumber == 3 else ["Name a number lower than " + str(randomNumber2) + "\n", randomNumber2], "lower"
    elif randomNumber == 5:
        randomNumber2 = random.randint(1, multiplicationNumber)
        randomNumber3 = random.randint(1, multiplicationNumber)
        return ["What is " + str(randomNumber2) + " * " + str(randomNumber3) + "?\n", randomNumber2 * randomNumber3]

def answerCheck(userAnswer, correctAnswer): #checks the answer given to any question that is not higher or smaller than
    if userAnswer == correctAnswer:
        return 1
    elif abs(userAnswer) - abs(correctAnswer) <= 20 and abs(userAnswer) - abs(correctAnswer) >= 1 or abs(correctAnswer) - abs(userAnswer) <= 20 and abs(correctAnswer) - abs(userAnswer) >= 1:
        return 2
    elif userAnswer != correctAnswer:
        return 3

def answerCheckAlternate(userAnswer, question, higherOrLower): #checks the answer to higher or smaller than questions
    if userAnswer > question:
        return 1 if higherOrLower == "higher" else 3
    elif userAnswer < question:
        return 1 if higherOrLower == "lower" else 3

#------------------------------------//Battle innitiators

def battle(currentEventInfo, outcomeInfo): #for regular battles like snakes or trolls
    for x in range(0, len(outcomeInfo)):
        print(currentEventInfo[x])
        questionChecker(outcomeInfo[x])

def bossBattle(currentEventInfo, outcomeInfo, bossHealth): #for battles that need to end after the enemies health bar reaches 0 (so mostly bosses)
    x = 0
    while bossHealth != 0 or bossHealth < 0:
        print(currentEventInfo[x])
        questionChecker(outcomeInfo[x], bossHealth)
        x += 1

#------------------------------------//Story and decision functions

def theInfoDumper(info): #Give this function a list of strings and it will print it out for you with a delay. Good for large walls of text.
    for x in info:
        print(x)
        time.sleep(1)

def decision(inputQuestion, decisions): #Gives us the number corrospondend to the decision the player took (can also let the player open the option menu)
    whileNum = 0
    while whileNum == 0:
        choice = input(inputQuestion).lower()
        y = 0
        for x in decisions:
            if choice == x:
                return y
            elif choice != "health":
                y += 1
        
        if choice == "options":
            options()
        else:
            print("Please enter a valid choice.")

def options(): #Option menu
    whilenum = 0
    while whilenum == 0:
        choice = input("Welcome to the option menu!\nPlease select an option (health/level/cheatcodes) or exit to leave this menu\n").lower()
        if choice == "health":
            if health == maxHealth and difficulty != "hard":
                print("Your current health is: " + str(health) + "/" + str(maxHealth) + "\nDont worry, you won't die anytime soon ;)")
            elif health == maxHealth:
                print("Your current health is: " + str(health) + "/" + str(maxHealth) + "\nDont let that make you feel invincible though ;)")
            else:
                print("Your current health is: " + str(health) + "/" + str(maxHealth))
        elif choice == "level":
            print(currentLevel)
        elif choice == "cheatcodes":
            cheatCodes()
        elif choice == "exit":
            return ""
        else:
            print("Please select a valid option.")

def cheatCodes(): #I dont think ill have to explain this one
    global damageMultiplier
    global maxHealth
    global health
    
    whileNum = 0
    while whileNum == 0:
        choice = input("Enter a 4 digit cheatcode here or enter exit to leave this menu\n")
        if choice == "1111":
            print("1111? Seriously? Who do you take me for? A simpleton who can't think of hard cheatcodes?!?!?")
        elif choice == "9999":
            healthCheck("Shouldntve entered that code :)")
        elif choice == "0344":
            damageMultiplier = int(input("Enter a multiplier to your damage here\n"))
        elif choice == "up up down down left right left right b a":
            print("Your body feels light. Your muscles grow. The power of god has been put in your hands!")
            maxHealth = 9999
            health = 9999
        elif choice == "exit":
            return ""
        else:
            print("Please enter a valid cheatcode.")

#------------------------------------//Difficulty and character selection

def diffSelect(): #selects a difficulty
    global difficulty
    global numberOfOperators
    global additionSubtractionNumber
    global multiplicationNumber

    difficulty = input("Enter the difficulty you would like to play on (easy, medium or hard)\n").lower()
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
    elif difficulty == "":
        print("Uhm.... you were supposed to enter something here...")
        diffSelect()
    else:
        print("This is not a possible difficulty!")
        diffSelect()

def characterSelect(): #runs through the characters list than asks the user which one they want to be
    whileNum = 0
    while whileNum == 0:
        print("Choose one of the following characters:")
        for x in characters:
            print("- ", x)
        choice = input("").lower()
        for x in characters:
            if choice == x:
                return x
        if choice == "":
            print("Uhm.... you were supposed to enter something here...")
        else:
            print("This is not a possible option!")
        


#------------------------------------//Health system

def healthCheck(deathMessage): #removes health
    global health
    if difficulty == "easy":
        health -= 3
    elif difficulty == "medium":
        health -= 5
    else:
        health -= health
    
    if health <= 0:
        print(deathMessage + "\nGame over!")
        exit()

#---------------------------------------------------------------------------------------------------//start of the game

diffSelect()

character = characterSelect()

#---------------------------------------------------------------------------------------------------//hero character recurring levels

def continuePathForest(): #level 2: plains
    currentLevel = "level 2: plains"
    theInfoDumper([

    ])

def continueDeeperForest(): #level 2: deeper forest
    theInfoDumper([

    ])

#---------------------------------------------------------------------------------------------------//hero character story

if character == "hero": #to do: add continuation to forest path, add deeper forest path, add desert path, finish snake battle
    global currentLevel
    currentLevel = "level 0: the village"
    theInfoDumper([
        "There was once a village. A village like any other village. A village with inhabitants like any other village. A village with troubles like any other village had.",
        "None would have ever expected what could have come out of a village like any other. A hero who would one day slay all evil that threatened the land. A hero that would bring hope to any in dispair.",
        "Until that day arives, the inhabitants of this world must deal with what evil god throws at them.",
        "In another village close to the village like any other, a boy resides. This boy was really like any boy inside that village, with the exception for his above avarage performance with the blade.",
        "The boy had one goal in life: Become a member of the elite swordsmen that guarded the royal family. It was a comfortable life inside the walls of the castles. Much better than what the villages were like.",
        "One day the boy had a chance. A less prominent member of the royal family had been kidnapped on their way to one of the capital of the country. If he could find them and strike down the people that kidnapped them, they might land him a job in a lesser castle. From where he could then work up to the royal family.",
        "And so the boy set out on an adventure. To find and rescue the royal member from certain doom!\n"
    ])
    choice = decision("As you leave the village you come across a sign. One arrow points to the right and one points straight ahead. The arrows have 'forest' and 'desert' on them. Which way will you go? (forest or desert)\n (reminder that the options menu can be opened at any time by typing 'options'\n", ["forest", "desert"])
    if choice == 0: #level 1: forest
        currentLevel = "level 1: forest"
        theInfoDumper([
            "You chose to enter the forest!",
            "As you walk along the road to the forest the feeling of living on the countryside seems more apparent than ever.",
            "Everywhere you look you can only see fields, with the exception of the forest infront of you.",
            "As you reach the edge of the forest you see the trees stretch far above you.",
            "It was quite easy to see the path going through the forest, so you decided to follow it further.",
            "The inside of the forest is calm. No one was there. Althought the ocasional bird could be seend sitting on the branches of the trees."
        ])
        choice = decision("As your eyes wonder around you see a glint deeper into the forest. The glint is off the path. Will you go thowards the glint or stay on the path? (path or deeper forest)\n", ["path", "deeper forest"])
        if choice == 0: #level 2: plains
            continuePathForest()
        else: #level 2: deeper forest
            currentLevel = "level 2: deeper forest"
            theInfoDumper([
                "You chose to walk into the deeper part of the forest. Following the glint you were so curious about.",
                "As you get closer to the glint you can slowly start making out it's shape. It becomes clear to you what the glint is.",
                "The glint was a chest!"
            ])
            choice = decision("Would you like to open the chest? (yes or no)\n", ["yes", "no"])
            if choice == 0: #grab chest, fight snakes, get loot, life good.
                theInfoDumper([
                    "You walk thowards the chest and grab onto both sides of the top.",
                    "As you slowly open the chest you notice something. The inside of the chest is covered in green...",
                    "A group of snakes jump out of the chest!"
                ])
                battle([ #snakes, snakes, we are the snakes
                    "You pull out your sword and point it at the group of snakes. They are with many, and their long viper teeth are sure to inflict some damage if not handled carefully",
                    "The snakes advance thowards you. You step back a bit to keep the distance.",
                    "The snakes seem to be tired. A simple scream might be able to scare them off now."
                ], [
                    [
                        "You slash one of the snakes with your blade. It didnt kill it, but it did damage it.",
                        "You barely scraped by the skin of one of the snakes with your blade. The snakes strike back by biting your foot.",
                        "You stumble over. One of the snikes bites you in your foot.",
                        "You died to the snakes venom. Didn't come far for a hero ey?"
                    ], [
                        "You strike one of the snakes on it head. It instantly dies. The other snakes back up.",
                        "You miss the snakes by a hair. The snakes strike back and bite your hand.",
                        "You hit your head against one of the branches. A snake bites you in your hand.",
                        "You died to the snakes venom. Didn't come far for a hero ey?"
                    ], [
                        "You scream at the snakes. They get scared and run away. You win the battle!",
                        "You swing around your sword. A last snakes bites your leg as they slitter away.",
                        "You stumble forward onto one of the snakes. It bites your face before slittering away.",
                        "You were at the end of the battle! Come on, you can do better!"
                    ]
                ])
                theInfoDumper([
                    "After defeating the snakes you walk back to the chest.",
                    "You again grab the top of the chest with both hands and lift up the lid.",
                    "You found....A new sword!"
                ])
                damageMultiplier = 1.50
                choice = decision("As you grab the new sword, \nyou look back at the path. Would you like to go back on the path or go further into the deeper part of the forest? (back or further)\n", ["back", "further"])
                if choice == 0: #level 2: plains
                    continuePathForest()
                else: #level 2: deeper forest
                    continueDeeperForest()
            else:
                choice = decision("You walk away from the chest. Would you like to go back on the path or go further into the deeper part of the forest? (back or further)\n", ["back", "further"])
                if choice == 0: #level 2: plains
                    continuePathForest()
                else: #level 2: deeper forest
                    continueDeeperForest()
    else: #level 1: desert
        theInfoDumper([
            "You chose to go to the desert!",
            "The thought of a desert right next to the plains you lived in didnt pay you any mind. You were excited for this adventure.",
            "As you reached the desert you felt the sun intensify, the air becoming drier and your body screaming for water. But water was a long way away in the middle of nowhere.",
            "You walked, walked, walked, and walked some more. Until...",
            "You found an oasis!"
        ])
        choice = decision("Will you drink from the oasis? (yes or no)\n", ["yes", "no"])
        if choice == 0:
            theInfoDumper([

            ])
        else: #who thought not drinking the water was a good idea?
            while character == "hero":
                healthCheck("You died of thirst! Shouldve thought about that one.")