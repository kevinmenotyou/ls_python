import random

MAX_TOTAL = 21

CARDS_AND_VALUES = {
    'ace': [1, 11],
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
    deck = []
    for suit in SUITS:
        for number, value in CARDS_AND_VALUES.items():
            deck.append((f'{number}_of_{suit}', 
                    {
                        'suit': suit,
                        'number': number,
                        'value': value,
                    }
            ))
    return deck

def shuffle(deck):
    random.shuffle(deck)

def prompt(message):
    print(f'==> {message}')

def deal_card(deck, number_of_cards):
    dealt_cards = []
    top_card_index = 1
    for index in range(0, number_of_cards):
        my_card = deck.pop(top_card_index)
        dealt_cards.append(my_card)
    return dealt_cards

def calculate_ace(current_total):
    possible_ace_values = CARDS_AND_VALUES['ace']
    possible_ace_values.sort(reverse=True)
    for possible_ace_value in possible_ace_values:
        if current_total + possible_ace_value <= MAX_TOTAL:
            return possible_ace_value
    return possible_ace_values[len(possible_ace_values)] # return smallest possible

def calculate_hand_total(hand):
    current_hand = hand.copy()

    hand_total = sum([card[1]['value'] for card in current_hand if card[1]['number'] != 'ace'])
    number_of_aces = sum([sum(card) for card in current_hand if card[1]['number'] == 'ace'])
    print(f'hand_total: {hand_total}')
    print(f'number_of_aces: {number_of_aces}')
    for ace in range(0, number_of_aces):
        hand_total += calculate_ace(current_total)
    return hand_total

def busted(hand):
    if calculate_hand_total(hand) > 21:
        return True
    return False

def player_loop(deck, player_hand):
    while True:
        display_hand(player_hand)
        answer = input("hit or stay?")
        if answer == 'stay' or busted(player_hand):
            break
        if answer == 'hit':
            player_hand.extend(deal_card(deck, 1))
    if busted(player_hand):
        prompt("You lose!")
    else:
        prompt("You chose to stay!")  # if player didn't bust,
                                      # must have stayed to get here

def dealer_loop(deck, dealer_hand):
    dealer_total = 0
    while dealer_total <= 17:
        #hit()
        if busted():
            break
    if busted():
        prompt("Dealer Busted")
    else:
        prompt("Hello.")

def display_hand(hand, hidden_card = False):
    display_hand = hand.copy()
    if (hidden_card == True):
        display_hand[1] = "***"
        return
    prompt(f'{display_hand}')

def display_hands(player_hand, dealer_hand):
    print(f'Player: {display_hand(player_hand, False)}')
    print(f'Dealer: {display_hand(dealer_hand, True)}')

def game_loop():
    while True:
        deck = init_deck()
        shuffle(deck)
        player_hand = deal_card(deck, 2)
        dealer_hand = deal_card(deck, 2)
        
        player_loop(deck, player_hand)
        # not implemented: dealer_loop(deck, dealer_hand)

game_loop()
