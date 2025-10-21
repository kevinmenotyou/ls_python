import random

MAX_TOTAL = 21

CARDS_AND_VALUES = {
    'ace': {1, 11}
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'jack': 10,
    'queen': 10,
    'king': 10
}

SUITS = [
    'diamonds',
    'hearts',
    'spades',
    'clubs'
]

def init_deck():
    deck = {}
    for suit in SUITS:
        for number, value in CARDS_AND_VALUES.items():
            deck[f'{number}_of_{suit}']= {
                'suit': suit,
                'number': number,
                'value': value,
                }
    return deck

def shuffle(deck):
    random.shuffle(deck)

def deal_card(deck, number_of_cards):
    dealt_cards = {}
    top_card_index = 1
    for index in range(0, number_of_cards):
        my_card = deck.pop(list(deck.keys())[top_card_index])
        dealt_cards.update(my_card)
    return dealt_cards

def calculate_ace(current_total):
    possible_ace_values = CARDS_AND_VALUES['ace']
    possible_ace_values.sort(reverse=True)
    for possible_ace_value in possible_ace_values:
        if current_total + possible_ace_value <= MAX_TOTAL:
            return possible_ace_value
    return possible_ace_values[len(possible_ace_values)] # return smallest possible

def busted(dealt_cards):
    total = 0
    for card_name, in dealt_cards.index():
        card.
def player_loop(deck, player_hand):
    while True:
        answer = input("hit or stay?")
        if answer == 'stay' or busted(player_hand):
            break
        if answer == 'hit':
            player_hand.update(deal_card(deck, 1))
    if busted():
        # probably end the game? or ask the user to play again?
    else:
        prompt("You chose to stay!")  # if player didn't bust,
                                    # must have stayed to get here

def dealer_loop(cards):
    dealer_total = 0
    while dealer_total <= 17:
        #hit()
        if busted():
            break
    if busted():
        prompt("Dealer Busted")
    else:
        prompt("Hello.")

def display_hand(hand, hidden_card):
    if (hidden_card == True):
        
        return


def display_hands(player_hand, computer_hand):

def game_loop():
    while True:
        deck = init_deck()
        shuffle(deck)
        player_hand = deal_card(deck, 2)
        dealer_hand = deal_card(deck, 2)
        
        player_loop(deck)
        dealer_loop(deck)
