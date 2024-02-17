# Nicole Thomas
# Lab01AP3.py
# January 10, 2024

# Ask player1 and player2 for their choice

player1_choice = str(input("Player 1:please enter r for rock, p for paper, or s for scissors: "))

player2_choice = str(input("Player2:please enter r for rock, p for paper, or s for scissors: "))


# Determine winner
def determine_winner(player1=str, player2=str):
    if player1 == player2:
        return "Tie!"

    if player1 == 'r' or 'R':
        if player2_choice == 's':
            return "Player1 wins!"
        else:
            return "Player2 wins!"

    elif player1 == 'p' or 'P':
        if player2_choice == 'r':
            return "Player1 wins!"
        else:
            return "Player2 wins!"

    elif player1 == 's' or 'S':
        if player2_choice == 'p':
            return "Player1 wins!"
        else:
            return "Player2 wins!"

    # Validate player1 choice

    if player1 not in ['r', 'R', 'p', 'P', 's', 'S']:
        print("Invalid entry. Game canceled")
        breakpoint()


# Validate player2 choice
if player2_choice not in ['r', 'R', 'p', 'P', 's', 'S']:
    print("Invalid entry. Game canceled")
    breakpoint()


# Determine and display the winner
def main(player1, player2):
    winner = determine_winner(player1, player2)
    print(winner)


main(player1_choice, player2_choice)
