test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
position_place = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [' '] * 10


def display_board(board):
    """ This function is responsible for printing the board"""
    print('\n')
    print('____' * 3)
    print('|   ' * 4)
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    print('|   ' * 4)
    print('____' * 3)
    print('|   ' * 4)
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print('|   ' * 4)
    print('____' * 3)
    print('|   ' * 4)
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
    print('|   ' * 4)
    print('____' * 3)


def players_marker_input():
    """This function will take player input (marker) and assignee it to them """
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('player_1 please select a marker (X or O): ').upper()
    player_1 = marker
    if player_1 == 'X':
        player_2 = 'O'
        print('Player_1 marker is "X" and Player_2 marker is "O"')
    else:
        player_2 = 'X'
        print('Player1 marker is "O" and Player2 marker is "X"')
    return player_1, player_2


def place_marker_on_board(board, marker, position):
    """This function will accept a position and put the marker on the board """
    board[position] = marker


def check_win(board, mark):
    """This function will check is teh current mark win the game"""
    if board[7] == board[8] == board[9] == mark or board[4] == board[5] == board[6] == mark or board[1] == \
            board[2] == board[3] == mark or board[1] == board[4] == board[7] == mark or board[2] == board[5] == \
            board[8] == mark or board[3] == board[6] == board[9] == mark or board[1] == board[5] == board[9] == \
            mark or board[3] == board[5] == board[7] == mark:

        print(f"player with mark '{mark}' won the game! Congratulation : ")
        return True
    else:
        return False


def check_position(free_position):
    """This function will check if there is a free position"""
    if len(free_position):
        return True
    else:
        return False


game_round = 1
game_star = True
"""Game Start Here"""
print('Welcome to Tic Tac Toe by RFM')
while game_star:
    game_on = True
    player1_marker, player2_marker = players_marker_input()

    def who_start_first():
        player_turn = True
        while player_turn:
            turn = input("Who would like to go first ('X' or 'O'): ").upper()
            if turn == 'X' or turn == 'O':
                return turn
            player_turn = False

    turn = who_start_first()

    while game_on:

        if game_round < 5:
            if turn == player1_marker:
                def player_one():
                    player_position = ''
                    display_board(board)
                    while player_position not in position_place:
                        player_position = int(input(f'Player {player1_marker} select a free position between (1-9): '))
                        if player_position in position_place:
                            break
                    place_marker_on_board(board, player1_marker, player_position)
                    position_place.remove(player_position)
                    display_board(board)
                player_one()
                turn = player2_marker
                game_round += 1

            elif turn == player2_marker:
                def player_two():
                    player_position = ''
                    display_board(board)
                    while player_position not in position_place:
                        player_position = int(input(f'Player {player2_marker} select a free position between (1-9): '))
                        if player_position in position_place:
                            break
                    place_marker_on_board(board, player2_marker, player_position)
                    position_place.remove(player_position)
                    display_board(board)
                player_two()
                turn = player1_marker
                game_round += 1

        elif game_round >= 5:
            if turn == player1_marker:
                if check_position(position_place):
                    def player_one():
                        player_position = ''
                        display_board(board)
                        while player_position not in position_place:
                            player_position = int(
                                input(f'Player {player1_marker} select a free position between (1-9): '))
                            if player_position in position_place:
                                break
                        place_marker_on_board(board, player1_marker, player_position)
                        position_place.remove(player_position)
                        display_board(board)
                    player_one()
                    if check_win(board, player1_marker):
                        print('Game Over')
                        game_on = False
                    else:
                        turn = player2_marker
                        game_round += 1
                elif not check_position(position_place):
                    print("Tie Game 🤝")
                    game_on = False
            elif turn == player2_marker:
                if check_position(position_place):
                    def player_two():
                        player_position = ''
                        display_board(board)
                        while player_position not in position_place:
                            player_position = int(
                                input(f'Player {player2_marker} select a free position between (1-9): '))
                            if player_position in position_place:
                                break
                        place_marker_on_board(board, player2_marker, player_position)
                        position_place.remove(player_position)
                        display_board(board)
                    player_two()
                    if check_win(board, player2_marker):
                        print('Game Over')
                        game_on = False
                    else:
                        turn = player1_marker
                        game_round += 1
                elif not check_position(position_place):
                    print("Tie Game 🤝")
                    game_on = False

    def replay_game():
        global game_star, board, position_place, game_round
        play_again = input("Would you like to replay te game ('Y'/'N'): ").upper()
        if play_again == 'Y':
            position_place = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            board = [' '] * 10
            game_round = 1
            game_star = True
        else:
            print('Thank you Good Bye!')
            game_star = False

    replay_game()
