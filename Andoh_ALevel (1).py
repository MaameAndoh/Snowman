#NEW PART
def instructions():
    print("This is a game of snowman.")
    print("The challenge is to guess all the letters in the secret word.")
    print("Each incorrect guess brings you closer to a complete snowman.")
    print("The game ends when you either guess correctly or have five incorrect guesses.")
    print("Good luck!")
    
#NEW PART
def initializeBlanks(secretWord):
    blanks = ['_']*len(secretWord)
    return(blanks)

#NEW PART
def getGuess():
    instructions()
    #create the loop control variable
    #again = 'y'
    #create the secret word

    #player1 = input("Player 1, Enter your name:")
    #player2 = input("Player 2, Enter your name:")
    secretWord = 'stairs'
    blanks = initializeBlanks(secretWord)
    wrongGuess = []

    wrongCount = 0
    won = False
    while wrongCount < 5 and won != True:
        print()
        user = input("Enter a letter:")
        wrongCount = statusReport(user, secretWord, blanks, wrongGuess, wrongCount)
        won = blanksFilled(secretWord, blanks, wrongCount, wrongGuess)

#NEW PART
def fillInBlanks(user, secretWord, blanks, wrongGuess, wrongCount):

    for x in range(len(secretWord)):
        #ind = secretWord.index(x)
        if secretWord[x] == user:
            blanks[x] = user
    print(blanks)
    
    blanksFilled(secretWord, blanks, wrongGuess, wrongCount)

#NEW PART
def report(secretWord, blanks, wrongCount, wrongGuess):
    
    if wrongCount == 5:
        print()
        print("Game over.")
        print("You have five incorrect guesses. You have a complete snowman.")
        print("The secret word was", secretWord)
        print("Here are the letters you guessed correctly:", blanks)
        print("Here are the incorrect letters:", wrongGuess)
        print()
    
    else:
        print()
        print("Congratulations! You guessed all the letters.")
        print(blanks)
        print("Here are the letters you guessed incorrectly:", wrongGuess)
        print("Number of incorrect letters:", wrongCount)
        print()

#NEW PART
def grid(wrongCount, grid):

    #create snow
    grid[3][0] = '~'
    grid[3][1] = '~'
    grid[3][2] = '~'

    if wrongCount == 1:
        grid[0][1] = 'O'
        print(*grid[0])
        print()
        print()
        print(*grid[3])
    elif wrongCount == 2:
        grid[0][1] = 'O'
        grid[1][1] = 'O'
        print(*grid[0])
        print(*grid[1])
        print()
        print(*grid[3])
    elif wrongCount == 3:
        grid[0][1] = 'O'
        grid[1][1] = 'O'
        grid[2][1] = 'O'
        print(*grid[0])
        print(*grid[1])
        print(*grid[2])
        print(*grid[3])
    elif wrongCount == 4:
        grid[0][1] = 'O'
        grid[1][1] = 'O'
        grid[2][1] = 'O'
        grid[1][0] = '/'
        print(*grid[0])
        print(*grid[1])
        print(*grid[2])
        print(*grid[3])
    elif wrongCount == 5:
        grid[0][1] = 'O'
        grid[1][1] = 'O'
        grid[2][1] = 'O'
        grid[1][0] = '/'
        grid[1][2] = '\\'
        print(*grid[0])
        print(*grid[1])
        print(*grid[2])
        print(*grid[3])
    else:
        print(*grid[0])
        print(*grid[1])
        print(*grid[2])
        print(*grid[3])

#NEW PART
def statusReport(user, secretWord, blanks, wrongGuess, wrongCount):
    #initialize the grid
    createGrid = [[' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']]

    if user.isalpha():
        lowercase = user.lower()
        if len(lowercase) > 1:
            print("No more than one entry allowed. Try again.")
        elif lowercase in secretWord:
            print("Great guess!")
            fillInBlanks(lowercase, secretWord, blanks, wrongGuess, wrongCount)
        else:
            print()
            print("The letter is not in the secret word.")
            #check to see if the letter has already been guessed.
            if lowercase in wrongGuess:
                print("You have already guessed this letter.")
                print("Incorrect letters:",wrongGuess)
            else:
                wrongGuess.append(lowercase)
                print("Incorrect letters:",wrongGuess)
    else:
        if len(user) > 1:
            print("No more than one entry allowed. Try again.")
        else:
            print("Enter only letters. Try again.")

    wrongCount = len(wrongGuess)
    print()
    print("There are", wrongCount, "incorrectly guessed letters.")

    if wrongCount == 5:
        grid(wrongCount,createGrid)
        report(secretWord, blanks, wrongCount, wrongGuess)
        return(wrongCount)
    else:
        grid(wrongCount,createGrid)
        return(wrongCount)

#NEW PART
def blanksFilled(secretWord, blanks, wrongCount, wrongGuess):
    if '_' not in blanks: 
        report(secretWord, blanks, wrongCount, wrongGuess)
        won = True
        return(won)

getGuess()