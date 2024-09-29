import random

def choose_game():
    while True:
        print("Welcome to Rock, Paper, Scissors!")
        print("What game do you want to play?")
        print("1. Player vs Player")
        print("2. Player vs Computer")
        print("3. Computer vs Computer")
        print("4. Exit the game")
        try:
            game_choice = int(input("Select your game by pressing 1, 2, 3 or 4 to exit :"))
            if game_choice == 1:
                player_vs_player()
                continue

            if game_choice == 2:
                user_vs_computer()
                continue

            if game_choice == 3:
                computer_vs_computer()
                continue

            if game_choice == 4:
                print("Thank you for playing")
                break
            if game_choice != [1, 2, 3, 4]:
                print("Invalid game choice")
                print("Try again")
                continue
        except ValueError:
            print("Invalid game choice")
            print("Try again")
            continue


# Start a game function
def player_vs_player():
# Show a greeting message and explain the rules of the game
    print("Welcome to Rock, Paper, Scissors, Player vs Player!")
    print("First player to win 3 rounds wins the game")
    print("Select your weapon by pressing 1, 2, or 3")
    print("Press 4 to exit the game")
# These variables are created to keep the players' scores before the while loop in order for the
# scores to be updated, instead of being set with the same value if they were within the while loop
    score_player1 = 0
    score_player2 = 0
# Start a while loop, allowing the players to play multiple rounds until the score of 5 is met, or if
# a player decides to exit the game
    while True:
# Print the players options
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")
# Use the try block to handle any errors in the player's input
        try:
# Take the player 1 input as an integers, the use of the integers, 1, 2, 3 and 4, instead of
# Rock, Paper or scissors reduce the errors that may happen during the players input
            player1_choice = int(input("Player 1, select a weapon! Press 4 to exit :"))
# If player 1 chooses to exit the game, the score of player 1 and player 2 will be displayed,
# and a winner will be chosen depending on which player has a greater score, and print a message to
# thank the players for participating
            if player1_choice == 4:
                print(f"Score: Player 1: {score_player1}  Player 2: {score_player2}")
                if score_player1 > score_player2:
                    print("Player 1 is the winner!")
                    print("Thank you for playing Rock, Paper, Scissors")
# If the scores are tied, no winners are announced and print a "It's a draw!" message
                elif score_player1 == score_player2:
                    print("It's a draw!")
                    print("Thank you for playing Rock, Paper, Scissors")
                elif score_player2 > score_player1:
                    print("Player 2 is the winner!")
                    print("Thank you for playing Rock, Paper, Scissors")
# After the winner is chosen, if there is one, print a farewell message and the break statement exit
# the loop and ends the game
                print("Goodbye")
                break
# Repeat the same process for the player 2 input if the input is 4
            player2_choice = int(input("Player 2, select a weapon! Press 4 to exit:"))
            if player2_choice == 4:
                print(f"Score: Player 1: {score_player1}  Player 2: {score_player2}")
                if score_player1 > score_player2:
                    print("Player 1 is the winner!")
                elif score_player1 == score_player2:
                    print("It's a draw!")
                elif score_player2 > score_player1:
                    print("Player 2 is the winner!!")
                    print("Thank you for playing Rock, Paper, Scissors")
                print("Goodbye")
                break
# If any errors happened during any players inputs, the except block would catch it
# and return an invalid choice message and skips the rest of the program through the continue statement
        except ValueError:
            print("Invalid choice! Please select between 1 and 4.")
            continue
# If a player's choice is a number but not between 1, 2, or 3, print an invalid choice message
# and skips the rest of the program through the continue statement
        if player1_choice not in [1, 2, 3] or player2_choice not in [1, 2, 3]:
            print("Invalid choice! Please select between 1 and 4.")
            continue
# The next three elif statement are for winning combinations for player 1, taking the input of the
# two players, increasing the variable score_player1 by 1, declaring player 1 as the winner, and
# print the updated scores
        elif player1_choice == 1 and player2_choice == 3:
            score_player1 += 1
            print("Player 1 wins this round!")
            print(f"Score: Player 1: {score_player1}  Player 2: {score_player2}")

        elif player1_choice == 2 and player2_choice == 1:
            score_player1 += 1
            print("Player 1 wins this round!")
            print(f"Score: Player 1: {score_player1}  Player 2: {score_player2}")

        elif player1_choice == 3 and player2_choice == 2:
            score_player1 += 1
            print("Player 1 wins this round!")
            print(f"Score: Player 1: {score_player1}  Player 2: {score_player2}")
# If the players' choices are the same, print a "It's a draw!" message a print the current scores
        elif player1_choice == player2_choice:
            print("It's a draw!")
            print(f"Score: Player 1: {score_player1}  Player 2: {score_player2}")
# If player 1 is not the winner, and the choices are not similar, player 2 is declared winner, the
# score of player 2 is increased by 1 and print the updated scores
        else:
            score_player2 += 1
            print("Player 2 wins this round!")
            print(f"Score: Player 1: {score_player1}  Player 2: {score_player2}")
# When player 1 score or player 2 score reaches 5, this player is declared winner of the game, print
# a message to thank the players for participating and print another farewell message. The break statement
# exit the loop and ends the game
        if score_player1 == 3:
            print("Player 1 is the winner!")
            print("Thank you for playing Rock, Paper, Scissors")
            print("Goodbye")
            break

        if score_player2 == 3:
            print("Player 2 is the winner!")
            print("Thank you for playing Rock, Paper, Scissors")
            print("Goodbye")
            break



def user_vs_computer():
    print("Welcome to Rock, Paper, Scissors, Player vs Computer(Kilroy)!")
    playing = True
    user_score = 0
    computer_score = 0
    while playing:
        user_action = input("Choose your weapon (rock, paper, scissors)or q to quit:").lower()
        if user_action == "q":
            print(f"Score: Player: {user_score} Kilroy: {computer_score}")
            if user_score > computer_score:
                print("You win")

            if user_score == computer_score:
                print("It's a draw")

            if user_score < computer_score:
                print("K.O. You lose the game")
            print("Don't be afraid to come back for more")
            break

        possible_actions = ["rock", "paper", "scissors", "q"]
        computer_possible_actions = ["rock", "paper", "scissors"]
        if user_action not in possible_actions:
            print("Invalid choice")
            continue
        computer_action = random.choice(computer_possible_actions)
        print(f"Your weapon {user_action}")
        print(f"Kilroy's weapon {computer_action}")
        if user_action == computer_action:
            print("it's Draw!")
        elif user_action == "rock" and computer_action == "scissors":
            print("You Win!")
            user_score += 1
        elif user_action == "paper" and computer_action == "rock":
            print("You Win!")
            user_score += 1
        elif user_action == "scissors" and computer_action == "paper":
            print("You Win!")
            user_score += 1
        else:
            print("K.O. You Lose")
        computer_score += 1

        print(f"Score: User: {user_score}  Computer: {computer_score}")
        if user_score == 3:
            print("You are the winner!")
            playing = False
            print("Don't be afraid to come back for more")
        if computer_score == 3:
            print("Kilroy is the winner!")
            playing = False
            print("Don't be afraid to come back for more")




def computer_vs_computer():
    print("Welcome to Rock, Paper, Scissors, Computer 1 vs Computer 2!")
    print("First to win 10 rounds wins the game")
    computer1_score = 0
    computer2_score = 0
    while True:
        possible_choices = ["Rock", "Paper", "Scissors"]
        computer1_choice = random.choice(possible_choices)
        computer2_choice = random.choice(possible_choices)
        print(f"Computer 1 chose {computer1_choice} and Computer 2 chose {computer2_choice}")
        if computer1_choice == "Rock" and computer2_choice == "Scissors":
            computer1_score += 1
            print("Computer 1 wins")
        if computer1_choice == "Paper" and computer2_choice == "Rock":
            computer1_score += 1
            print("Computer 1 wins")
        if computer1_choice == "Scissors" and computer2_choice == "Paper":
            computer1_score += 1
            print("Computer 1 wins")
        else:
            computer2_score += 1
            print("computer 2 wins")
        print(f"Score: Computer 1: {computer1_score}  Computer 2: {computer2_score}")
        if computer1_score == 10:
            print("Computer 1 is the winner")
            break
        if computer2_score == 10:
            print("Computer 2 is the winner")
            break



choose_game()
