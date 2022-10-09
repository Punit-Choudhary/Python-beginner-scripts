# Project Name- Tic Tac toe

# global variables
# the contents of game board
game_con = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# player no. 1
player1 = 0
# player no. 2
player2 = 0
# to keep count of player's turn
counter = 1
# to take the player's position
insert_pos = -1
# end of game flag
end_game = 0
# current player's turn
current = ''

# function to start the game


def start_game():
    game_board()
    player_char()
    player_input()

# Function to display the game board


def game_board():
    global game_con, end_game
    print('\n')
    print(' '+game_con[1]+' | '+game_con[2]+' | '+game_con[3]+' ')
    print('---|---|---')
    print(' '+game_con[4]+' | '+game_con[5]+' | '+game_con[6]+' ')
    print('---|---|---')
    print(' '+game_con[7]+' | '+game_con[8]+' | '+game_con[9]+' ')

# to decide the step after the display of game_board()


def the_judge():
    global end_game
    if end_game == 1:
        print('\n' + '************ '+current+'won the game ************')
        answer = input(
            "\n" +
            'To restart the game press 1 key' +
            '\nTo exit the game press any other key : ')
        if answer == '1':
            reboot_the_game_data()
            start_game()
        else:
            exit()
    else:
        player_input()

# function to choose the player's character either X or O


def player_char():
    global player1, player2
    while player1 not in ['x', 'X', 'o', 'O']:
        player1 = input("\n" + 'player1 choose your sign ( X or O ) : ')
        if player1 not in ['x', 'X', 'o', 'O']:
            print("\n" + 'Please insert a valid character.')
        elif player1 in ['x', 'X']:
            player1 = 'X'
            print("\n" + "Player 2's sign is O")
            player2 = 'O'
        else:
            player1 = 'O'
            print("\n" + "Player 2's sign is X")
            player2 = 'X'

# hard file
# function to accept position of player and increment the counter


def player_input():
    global player1, player2, game_con, counter, insert_pos, current
    insert_pos = ' '
    num = 1
    while insert_pos not in range(1, 10):
        if counter % 2 == 1:
            current = 'player 1 '
        else:
            current = 'player 2 '
        insert_pos = int(input(
            "\n" + current +
            'insert the position you want to mark (1 to 9) : '))
        if insert_pos not in range(1, 10):
            print("\n" + 'Invalid number. Please insert a valid position. \n')
        elif game_con[insert_pos] != ' ':
            num = 0
            print("\n" +
                  'This position is already aquired. ' +
                  'please choose a free position.\n')
        elif counter % 2 == 1:
            game_con[insert_pos] = player1
        else:
            game_con[insert_pos] = player2
    if num != 0:
        counter += 1
    # to check the game's end
    game_check()
    # Showing the updated game board
    game_board()
    # to end game if required    the_judge()
    the_judge()

# to check if the game ended or not


def game_check():
    global game_con, end_game, current
    if (game_con[1] == game_con[2] == game_con[3] and game_con[1] != ' '):
        end_game = 1
    elif (game_con[4] == game_con[5] == game_con[6] and game_con[4] != ' '):
        end_game = 1
    elif (game_con[7] == game_con[8] == game_con[9] and game_con[7] != ' '):
        end_game = 1
    elif (game_con[1] == game_con[5] == game_con[9] and game_con[5] != ' '):
        end_game = 1
    elif (game_con[3] == game_con[5] == game_con[7] and game_con[5] != ' '):
        end_game = 1
    elif (game_con[1] == game_con[4] == game_con[7] and game_con[1] != ' '):
        end_game = 1
    elif (game_con[2] == game_con[5] == game_con[8] and game_con[2] != ' '):
        end_game = 1
    elif (game_con[3] == game_con[6] == game_con[9] and game_con[3] != ' '):
        end_game = 1
    else:
        end_game = 0

# clear the data to initial stage of game


def reboot_the_game_data():
    global game_con, player1, player2, counter, insert_pos, end_game, current
    game_con = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1 = 0
    player2 = 0
    counter = 1
    insert_pos = -1
    end_game = 0
    current = ''

# Starts the game


start_game()
