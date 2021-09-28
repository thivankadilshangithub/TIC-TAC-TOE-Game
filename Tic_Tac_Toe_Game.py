# The TIC TAC TOE Game.

# This is player board
Player_Board = {'1': ' ', '2': ' ', '3': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '7': ' ', '8': ' ', '9': ' '}

Keys = []

for key in Player_Board:
    Keys.append(key)

# This is the printing board
def printing_Board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


# Now we should write the main function
def main(player1,player2):

    print("Hey " + player1 + ". You are 'X'")
    print("Hey " + player2 + ". You are 'O'")
    Player = 'X'
    count = 0

    for i in range(10):
        printing_Board(Player_Board)

        place = input("It is player " + Player + ".Enter the place please?")
        if Player_Board[place] == ' ':
            Player_Board[place] = Player
            count += 1

        else:

            print("Your place is already filled.\nNow, Move to which place?")
            continue

        # After five moves, There will be a result.
        if count >= 5:
            if Player_Board['7'] == Player_Board['8'] == Player_Board['9'] != ' ':
                printing_Board(Player_Board)
                print("\nGame Over.\n")
                print(" Congratulations Player " + Player + ". You won the Game !!! ")
                break
            elif Player_Board['4'] == Player_Board['5'] == Player_Board['6'] != ' ':
                printing_Board(Player_Board)
                print("\nGame Over.\n")
                print(" Congratulations Player " + Player + ". You won the Game !!! ")
                break
            elif Player_Board['1'] == Player_Board['2'] == Player_Board['3'] != ' ':
                printing_Board(Player_Board)
                print("\nGame Over.\n")
                print(" Congratulations Player " + Player + ". You won the Game !!! ")
                break
            elif Player_Board['1'] == Player_Board['4'] == Player_Board['7'] != ' ':
                printing_Board(Player_Board)
                print("\nGame Over.\n")
                print(" Congratulations Player " + Player + ". You won the Game !!! ")
                break
            elif Player_Board['2'] == Player_Board['5'] == Player_Board['8'] != ' ':
                printing_Board(Player_Board)
                print("\nGame Over.\n")
                print(" Congratulations Player " + Player + ". You won the Game !!! ")
                break
            elif Player_Board['3'] == Player_Board['6'] == Player_Board['9'] != ' ':
                printing_Board(Player_Board)
                print("\nGame Over.\n")
                print(" Congratulations Player " + Player + ". You won the Game !!! ")
                break
            elif Player_Board['7'] == Player_Board['5'] == Player_Board['3'] != ' ':
                printing_Board(Player_Board)
                print("\nGame Over.\n")
                print(" Congratulations Player " + Player + ". You won the Game !!! ")
                break
            elif Player_Board['1'] == Player_Board['5'] == Player_Board['9'] != ' ':  # diagonal
                printing_Board(Player_Board)
                print("\nGame Over.\n")
                print(" Congratulations Player " + Player + ". You won the Game !!! ")
                break

            # If no one wins then it is a tie.
        if count == 9:
            printing_Board(Player_Board)
            print("\nGame Over.\n")
            print("It's a Tie!!")
            break

        # Now we have to switch the players.
        if Player == 'X':
            Player = 'O'
        else:
            Player = 'X'

        # To ask start again the game.
    Start_again = input("Do want to play Again?(y/n)")

    if Start_again == "y" or Start_again == "Y":

        for key in Keys:
            Player_Board[key] = " "
            main(player1, player2)
    else:
        print("Come again !!!")

if __name__ == "__main__":
    print("Tic-Tac-Toe Game")
    print("Two players need to this game. Please enter your names")
    Player_1 = input("Enter the player 1: ")
    Player_2 = input("Enter the player 2:")
    main(Player_1, Player_2)



