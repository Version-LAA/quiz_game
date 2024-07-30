from art import text2art
from Quiz import QUIZ_CATEGORIES
from Game import Game
def main_menu():
    print(text2art("Quiz",font='block',chr_ignore=True))
    print(text2art("GAME"))
    print("\nWelcome to the ultimate 2 player quiz game!")
    print("\n Select from our options below:\n ")
    print("What would you like to do?")
    try:
        option = input("\n1) Play New Game\n2) See Historical Matchups\n3) Exit\n\nOption: ")
        option = int(option)
    except:
        print("Not a valid value, goodbye! ")

    return option
def main():
    game = Game()
    initial_option = main_menu()


    if initial_option == 1:
        player1 = input("\nEnter a name for player1: ")
        player2 = input("Enter a name for player2: ")
        game.add_players([player1,player2])

        print("\nWhat type of quiz do you want to take?!\n")
        category = [print(f"{i+1} - {QUIZ_CATEGORIES[i]}") for i in range(len(QUIZ_CATEGORIES))]

        # [TODO] - error checking for non numerical inputs
        try:
            type = int(input("\nCategory Choice: "))
        except ValueError:
            print("Not a valid input")
        while type not in range(1,len(category)+1):
            print("Please enter a valid category type")
            type = int(input("\nCategory Choice: "))
        print("\nWhat level would you like to play?\n")
        print("1 - Beginner\n2 - Advanced\n")
        level = int(input("Level Choice: "))
        while level not in [1,2]:
            print("\nNot a valid option - please select from the following\n")
            print("1 - Beginner\n2 - Advanced\n")
            level = int(input("Level Choice: "))
        game.generate_quiz(type,level)
        # print(game.quiz[0])
        game.play_game()
    elif initial_option == 2:
        pass
    elif initial_option == 3:
        print("Come back next time, Goodbye 👋🏾")
        exit()
    else:
        print("Not a valid value, goodbye! 👋🏾👋🏾 ")
        exit()

main()
