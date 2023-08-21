from random import randint

result = 0
games_played = 0
correct_answers = 0
wrong_answers = 0

def play_game():
    global result, games_played, correct_answers, wrong_answers

    result = 0
    print("Add the following numbers:")
    for _ in range(randint(2, 7)):
        random_number = randint(0, 101)
        print("\t", random_number)
        result += random_number
    print("-------------------------\n")

    def enter_input():
        global games_played, correct_answers, wrong_answers
        try:
            user_input = int(input("Enter the sum of all the digits: "))

            if user_input == result:
                print("Yes, you are absolutely right! The result is {}\n".format(result))
                games_played += 1
                correct_answers += 1
                print("Games Played: {} | Correct Answers: {} | Wrong Answers: {}".format(games_played, correct_answers, wrong_answers))
                restart_game()
            else:
                print("Oops! That's not correct. The correct answer is {}\n".format(result))
                games_played += 1
                wrong_answers += 1
                print("Games Played: {} | Correct Answers: {} | Wrong Answers: {}".format(games_played, correct_answers, wrong_answers))
                restart_game()

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            enter_input()

    def restart_game():
        restart_condition = input("Do you want to restart the game? (y/n): ")

        if restart_condition.lower() == 'y' or restart_condition == '':
            play_game()
        else:
            print("Thanks for playing! <3")

    enter_input()

play_game()
