#WORD GUESSER
import random

#intialise global variables
playing = True
guessed = False

currentWord = "testingdefault"
wordList = ["apple", "banana", "coriander", "durian", "eggplant", "fettucine", "garnish", "hamburger", "juice", "orange", "lemon", "pineapple"]
alreadyGuessed = []

guess = ""

guessLimit = 12
guessCount = 0

#get user input to check
def get_guess():
    global guess
    displayGuessed = "Already guessed: "
    if(len(alreadyGuessed) > 0):
        for previousGuess in alreadyGuessed:
            displayGuessed = displayGuessed + previousGuess + ", " 
        print(displayGuessed)
    guess = input("You have " + str(guessLimit - guessCount) + " guesses left.\nGuess a letter or a word: ")
    guess = guess.lower()
    if(guess == "exit"):
        exit()

#checks full word or individual character
def check_guess():
    guessCorrect = False
    if(guess == currentWord):
        print("\nYou Win!  The word was: " + guess + "\n")
        guessCorrect = True
        global guessed
        guessed = True
    elif(len(guess) < 2):
        for char in currentWord:
            if(char == guess):
                if(not guess in alreadyGuessed):
                    alreadyGuessed.append(guess)
                guessCorrect = True
                print("The word does contain the letter: " + guess + "\n")
                break
            elif(not guess in alreadyGuessed):
                alreadyGuessed.append(guess)
    else:
        print("The word is not:  " + guess)

    if(not guessCorrect):
        global guessCount
        guessCount += 1    

#print results to the screen after guessing
def display_results():
    global guessed
    if(not guessed):
        displayString = ""
        for char in currentWord:
                if(char in alreadyGuessed):
                    displayString = displayString + char
                else:
                    displayString = displayString + "*"
        if(not "*" in displayString):
            print("\nYou Win!  The word was: " + displayString + "\n")
            guessed = True
        else:
            print("\nGuess the word:")
            print(displayString)

#GAME LOOP
while(playing):
    alreadyGuessed = []
    guessed = False
    guess = ""
    guessCount = 0
    chosenIndex = random.randint(0, len(wordList) - 1) #get random word index
    currentWord = wordList[chosenIndex] #Choose word from list

    print("\nWord selected.\n")
    display_results()

    #loop to run while the word is not guessed
    while(not guessed):
        get_guess()
        check_guess()
        display_results()
        if(guessCount >= guessLimit and not guessed):
            print("Max guesses reached.  You failed.")
            guessed = True

    #exit/retry
    retry = input("Input [r] to try again\nPress [enter] or input any other key to exit.\n")
    if(retry == "r"):
        print("\nRESTARTING\n")
    else:
        playing = False

exit()