print("Welcome to Rock, Paper, Scissors!")
print("First player at 5 points wins the game")
print("Select your weapon by pressing 1, 2, or 3")
print("Press 4 to exit the game")
count_player1 = 0
count_player2 = 0


def game():
    while True:
        global count_player1, count_player2
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")
        try:
            player1_choice = int(input("Player 1, select a weapon! Press 4 to exit :"))
            if player1_choice == 4:
                print(f"Score: Player 1: {count_player1}  Player 2: {count_player2}")
                if count_player1 > count_player2:
                    print("Player 1 is the winner!")
                    print("Thank you for playing Rock, Paper, Scissors")
                elif count_player1 == count_player2:
                    print("It's a draw!")
                    print("Thank you for playing Rock, Paper, Scissors")
                elif count_player2 > count_player1:
                    print("Player 2 is the winner!")
                    print("Thank you for playing Rock, Paper, Scissors")
                print("Goodbye")
                break

            player2_choice = int(input("Player 2, select a weapon! Press 4 to exit:"))
            if player2_choice == 4:
                print(f"Score: Player 1: {count_player1}  Player 2: {count_player2}")
                if count_player1 > count_player2:
                    print("Player 1 is the winner!")
                elif count_player1 == count_player2:
                    print("It's a draw!")
                elif count_player2 > count_player1:
                    print("Player 2 is the winner!!")
                    print("Thank you for playing Rock, Paper, Scissors")
                print("Goodbye")
                break
        except ValueError:
            print("Invalid choice! Please select between 1 and 4.")
            continue

        if player1_choice not in [1, 2, 3] or player2_choice not in [1, 2, 3]:
            print("Invalid choice! Please select between 1 and 4.")
            continue

        elif player1_choice == 1 and player2_choice == 3:
            count_player1 += 1
            print("Player 1 wins!")
            print(f"Score: Player 1: {count_player1}  Player 2: {count_player2}")

        elif player1_choice == 2 and player2_choice == 1:
            count_player1 += 1
            print("Player 1 wins!")
            print(f"Score: Player 1: {count_player1}  Player 2: {count_player2}")

        elif player1_choice == 3 and player2_choice == 2:
            count_player1 += 1
            print("Player 1 wins!")
            print(f"Score: Player 1: {count_player1}  Player 2: {count_player2}")

        elif player1_choice == player2_choice:
            print("It's a draw!")
            print(f"Score: Player 1: {count_player1}  Player 2: {count_player2}")

        else:
            count_player2 += 1
            print("Player 2 wins2!")
            print(f"Score: Player 1: {count_player1}  Player 2: {count_player2}")

        if count_player1 == 5:
            print("Player 1 is the winner!")
            print("Thank you for playing Rock, Paper, Scissors")
            print("Goodbye")
            break

        if count_player2 == 5:
            print("Player 2 is the winner!")
            print("Thank you for playing Rock, Paper, Scissors")
            print("Goodbye")
            break


game()


