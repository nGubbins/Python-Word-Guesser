
#this is not being used at the moment, left here as an example of how I could move this particular function into another class
#ideally this class would hold the check_guess function
def get_guess():
    guessInput = input("\nGuess a letter or a word: ")
    guessInput.lower()
    if(guessInput == "exit"):
        exit()
    return guessInput

