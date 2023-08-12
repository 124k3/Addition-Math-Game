from random import randint

def Game():
    result = 0
    print("Add the following numbers:")
    for _ in range(3):
        randomNumber = randint(0, 101)
        print(randomNumber)
        result = result + randomNumber
    print("-------------------------\n")
    
    def EnterInput():
        try:
            userInput = int(input("Enter the sum of all the digits: "))
            
            if userInput == result:
                print("Yes, you are absolutely right! The result is {}\n".format(result))
                RestartGame()  # Call the restart function
            else:
                print("Oops! That's not correct. The correct answer is {}\n".format(result))
                RestartGame()  # Call the restart function
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            EnterInput()
    
    def RestartGame():
        restartCondition = input("Do you want to restart the game? (y/n): ")
        
        if restartCondition.lower() == 'y':
            Game()
        else:
            print("Thanks for playing! <3")
    
    EnterInput()

Game()
