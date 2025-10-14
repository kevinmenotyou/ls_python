import math
import os
import pdb
import random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
TOTAL_NUMBER_OF_MATCHES = 5
PLAYER = 'Player'
COMPUTER = 'Computer'
TIE = 'Tie'

WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
    [1, 5, 9], [3, 5, 7]              # diagonals
]

def join_or(my_array, my_delimitter = ", ", my_word = "or"):
    if len(my_array) == 0:
        return ""

    if len(my_array) == 1:
        return my_array[0]

    copy_array = [str(integer) for integer in my_array]
    my_last_element = copy_array.pop()
    return f"{my_delimitter.join(copy_array)} {my_word} {my_last_element}"

def prompt(message):
    print(f'==> {message}')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def display_board(board):
    os.system('clear')
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def player_chooses_square(board):

    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        print(valid_choices)
        prompt(f'Choose a square ({join_or(valid_choices)}):')
        square = input().strip()
        if square in valid_choices:
            break
        prompt("Sorry, that's not a valid choice.")
    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return

    offensive_tile = find_at_risk_square(board, COMPUTER_MARKER)
    if offensive_tile != None:
        board[offensive_tile] = COMPUTER_MARKER
        return

    defensive_tile = find_at_risk_square(board, HUMAN_MARKER)
    if defensive_tile != None:
        board[defensive_tile] = COMPUTER_MARKER
        return

    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def find_at_risk_square(board, player_marker):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == player_marker and board[sq2] == player_marker and board[sq3] == INITIAL_MARKER):
            return sq3
        elif (board[sq1] == player_marker and board[sq2] == INITIAL_MARKER and board[sq3] == player_marker):
            return sq2
        elif (board[sq1] == INITIAL_MARKER and board[sq2] ==  player_marker and board[sq3] == player_marker):
            return sq1
    return None

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
               and board[sq2] == HUMAN_MARKER
               and board[sq3] == HUMAN_MARKER):
            return PLAYER
        elif (board[sq1] == COMPUTER_MARKER
                  and board[sq2] == COMPUTER_MARKER
                  and board[sq3] == COMPUTER_MARKER):
            return COMPUTER

    return None

def someone_won(board):
    return bool(detect_winner(board))

def welcome_player():
    prompt('Welcome to Tic-Tac-Toe. Best of 5 Wins!')
    wait_for_input('Press enter to continue...')

def wait_for_input(my_message):
    prompt(f'{my_message}')
    input().lower()

def someone_won_series(num_player_wins, num_computer_wins):
    wins_needed_to_win_series = math.ceil(TOTAL_NUMBER_OF_MATCHES / 2)

    if num_player_wins >= wins_needed_to_win_series:
        return True
        
    if num_computer_wins >= wins_needed_to_win_series:
        return True

    return False

def detect_series_winner(num_player_wins, num_computer_wins):
    if num_player_wins > num_computer_wins:
        return PLAYER

    if num_computer_wins > num_player_wins:
        return COMPUTER

    return TIE

def display_round_number(round):
    prompt(f'Round {round}, fight!')

def display_current_series_score(player_wins, computer_wins, ties, round):
    prompt(f'By round {round}, player has {player_wins} wins, computer has {computer_wins}, and there are {ties} ties.')

def display_computer_wins(num_player_wins, num_computer_wins, num_of_ties):
    prompt(f'Oh no! Computer wins! They won {num_computer_wins} and you won {num_player_wins}. There were {num_of_ties} ties')

def display_player_wins(num_player_wins, num_computer_wins, num_of_ties):
    prompt(f'You win! You won {num_player_wins} matches, and the computer won {num_computer_wins}. There were {num_of_ties} ties')

def display_tie(num_player_wins, num_computer_wins):
    prompt(f"It's a tie! You won {num_player_wins} matches, while the computer won {num_computer_wins}. There were {num_of_ties} ties")

def play_tic_tac_toe():
    
    while True:

        series_score = {
            PLAYER: 0,
            COMPUTER: 0,
            TIE: 0,
        }

        welcome_player()

        for round in range(1, 6):

            display_round_number(round)

            board = initialize_board()

            while True:
                display_board(board)

                player_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break

                computer_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break

            display_board(board)

            if someone_won(board):
                winner = detect_winner(board)
                series_score[winner] += 1
                prompt(f"{winner} won!")
            else:
                series_score[TIE] += 1
                prompt("It's a tie!")

            if someone_won_series(series_score[PLAYER], series_score[COMPUTER]) or round >= 5:
                series_winner = detect_series_winner(series_score[PLAYER], series_score[COMPUTER])

                if series_winner == PLAYER:
                    display_player_wins(series_score[PLAYER], series_score[COMPUTER], series_score[TIE])

                if series_winner == COMPUTER:
                    display_computer_wins(series_score[PLAYER], series_score[COMPUTER], series_score[TIE])

                if series_winner == TIE:
                    display_tie(series_score[PLAYER], series_score[COMPUTER], series_score[TIE])

                break

            display_current_series_score(series_score[PLAYER], series_score[COMPUTER], series_score[TIE], round)

            wait_for_input('Ready for the next round? Press enter to continue...')


        prompt("Play again? (y or n)")
        answer = input().lower()

        if answer[0] != 'y':
            break

play_tic_tac_toe()