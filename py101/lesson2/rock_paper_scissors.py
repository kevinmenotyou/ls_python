import json
import math
import os
import random

# CONSTANTS #

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
LIZARD = 'lizard'
SPOCK = 'spock'

BEST_OF = 5
MAX_VICTORIES = math.ceil(BEST_OF / 2)

# CLASSES #

class Choice:
    def __init__(self, name, wins_against, loses_against, valid_inputs):
        self.name = name
        self.wins_against_list = wins_against
        self.inputs_list = valid_inputs
        #unused but good for debug
        self.loses_against_list = loses_against

    def wins_against(self, choice):
        return choice in self.wins_against_list

    def loses_against(self, choice):
        return choice in self.loses_against_list

    # too used to LINQ:
    @staticmethod
    def get_all_names_from_list(all_choices):
        my_list = []
        for choice in all_choices:
            my_list.append(choice.name)
        return my_list

    @staticmethod
    def get_all_valid_choices_from_list(all_choices):
        my_list = []
        for choice in all_choices:
            for my_input in choice.inputs_list:
                my_list.append(my_input)
        return my_list

class Player:
    score = 0
    choice_list = []

    def wins_round(self, choice):
        self.score += 1
        self.choice_list.append(choice)

    def reset(self):
        self.score = 0
        self.choice_list = []

    def print_winning_choices(self):
        my_winning_choice_names_list = []
        for choice in self.choice_list:
            my_winning_choice_names_list.append(choice.name)
        my_winning_choices = ", ".join(my_winning_choice_names_list)
        print(f"{MESSAGE['winning_choices']} {my_winning_choices}")

# FUNCTIONS #

def get_formatted_string_of_valid_inputs(my_list):
    formatted_string = ""
    formatted_choices = []
    for choice in my_list:
        formatted_inputs = f"{choice.inputs_list[0]} [{choice.inputs_list[1]}]"
        formatted_choices.append(formatted_inputs)
    formatted_string = ", ".join(formatted_choices)
    return formatted_string

def get_choice_by_input(my_list, my_input):
    # next will return the first object from list
    # filter evaluates function in parameter1 for every item in parameter2
    # and returns a new list where parameter1 returned true

    for item in my_list:
        if my_input in item.name or my_input in item.inputs_list:
            return item

    raise NotImplementedError(MESSAGE['bug'])

def display_winner(player_choice, computer_choice, player, computer):
    player_name = player_choice.name
    computer_name = computer_choice.name
    prompt(f"You chose {player_name}, computer chose {computer_name}")

    if player_choice.wins_against(computer_choice.name):
        player.wins_round(player_choice)
        prompt(MESSAGE['player_wins'])
    elif computer_choice.wins_against(player_choice.name):
        computer.wins_round(computer_choice)
        prompt(MESSAGE['computer_wins'])
    else:
        prompt(MESSAGE['tie_result'])

def prompt(message):
    print(f"==> {message}")

def init_data():
    return [
        Choice(ROCK, [SCISSORS, LIZARD], [PAPER, SPOCK], [ROCK, "r"]),
        Choice(PAPER, [ROCK, SPOCK], [SCISSORS, LIZARD], [PAPER, "p"]),
        Choice(SCISSORS, [PAPER, LIZARD], [ROCK, SPOCK], [SCISSORS, "sc"]),
        Choice(LIZARD, [SPOCK, PAPER], [SCISSORS, ROCK], [LIZARD, "l"]),
        Choice(SPOCK, [SCISSORS, ROCK], [LIZARD, PAPER], [SPOCK, "sp"])]

def get_player_selection(choice_list):

    valid_selections = Choice.get_all_valid_choices_from_list(choice_list)

    prompt(f'Choose one: {get_formatted_string_of_valid_inputs(choice_list)}')
    player_selection = input().casefold()

    while player_selection not in valid_selections:
        prompt("That's not a valid choice")
        player_selection = input().casefold()

    return player_selection

def is_game_over(player, computer):
    return computer.score >= MAX_VICTORIES or player.score >= MAX_VICTORIES

def get_play_again():
    while True:
        prompt(MESSAGE['play_again'])
        answer = input().casefold()

        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt(MESSAGE['invalid_choice'])

    if answer[0].casefold() == 'n':
        return False
    return True

def display_best_of_winner(player, computer):
    print (f"Player won {player.score} rounds!")
    print (f"Computer won {computer.score} rounds!")

    if (player.score > computer.score):
        print (MESSAGE['stars'])
        print ("Player wins!")
        player.print_winning_choices()
    else:
        print (MESSAGE['stars'])
        print ("Computer wins!")
        computer.print_winning_choices()
    print(MESSAGE['stars'])

# MAIN LOOP #

def main_loop():

    choices = init_data()
    player = Player()
    computer = Player()

    with open('rock_paper_scissors.json', 'r') as file:
        global MESSAGE
        MESSAGE = json.load(file)

    play_again = True
    while play_again:

        player.reset()
        computer.reset()
        print(MESSAGE['welcome'])

        while not is_game_over(player, computer):
            player_choice = get_player_selection(choices)
            player_choice = get_choice_by_input(choices, player_choice)

            computer_choice = random.choice(
                Choice.get_all_names_from_list(choices))
            computer_choice = get_choice_by_input(choices, computer_choice)

            display_winner(player_choice, computer_choice, player, computer)

        print(MESSAGE['last_round'])
        input()
        os.system('clear')

        display_best_of_winner(player, computer)

        play_again = get_play_again()

    print (MESSAGE['thank_you'])

main_loop()