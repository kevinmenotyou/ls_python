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

PLAYER='Player'
DEALER='Dealer'
TIE='Tie'

def init_deck():
    deck = []
    for suit in SUITS:
        for number, value in CARDS_AND_VALUES.items():
            deck.append((f'{number}_of_{suit}',
                    {
                        'suit': suit,
                        'num': number,
                        'val': value,
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
    for _ in range(0, number_of_cards):
        my_card = deck.pop(top_card_index)
        dealt_cards.append(my_card)
    return dealt_cards

def calculate_ace(current_total):
    possible_ace_values = CARDS_AND_VALUES['ace']
    possible_ace_values.sort(reverse=True)
    for possible_ace_value in possible_ace_values:
        if current_total + possible_ace_value <= MAX_TOTAL:
            return possible_ace_value # valid number found
    # we are going to bust, so pick the smallest ace value anyway
    return possible_ace_values[len(possible_ace_values) - 1]

def calculate_hand_total(hand):
    my_hand = hand.copy()
    values = [card[1]['val'] for card in my_hand if card[1]['num'] != 'ace']
    total = sum(values)
    num_aces = len([card for card in my_hand if card[1]['num'] == 'ace'])
    for _ in range(0, num_aces):
        total += calculate_ace(total)
    return total

def busted(hand):
    if calculate_hand_total(hand) > 21:
        return True
    return False

def player_loop(deck, player_hand):
    while True:
        display_player_hand(player_hand)
        if busted(player_hand):
            break
        answer = input("hit or stay? ")
        if answer == 'stay':
            break
        if answer == 'hit':
            player_hand.extend(deal_card(deck, 1))
    if busted(player_hand):
        points = calculate_hand_total(player_hand)
        prompt(f"You went bust with ${points} points!")
    else:
        # if player didn't bust, they must have stayed to get here
        prompt("You chose to stay!")

def dealer_loop(deck, dealer_hand):
    display_dealer_hand(dealer_hand)
    dealer_total = calculate_hand_total(dealer_hand)
    while dealer_total <= 17:
        dealer_hand.extend(deal_card(deck, 1))
        prompt ("Dealer dealt himself another card!")
        display_dealer_hand(dealer_hand)
        if busted(dealer_hand):
            break
    if busted(dealer_hand):
        points = calculate_hand_total(dealer_hand)
        prompt(f"Dealer went bust with ${points} points!")

def display_hand(hand, hidden_card = False):
    my_hand = hand.copy()
    if (hidden_card is True):
        my_hand[1] = "***"
    for card in hand:
        name = card[0]
        my_hand = name.split('_')
        my_hand[0] = my_hand[0].capitalize()
        my_hand[2] = my_hand[2].capitalize()
        prompt(' '.join(my_hand))

def display_player_hand(player_hand):
    print('Player hand:')
    display_hand(player_hand, False)

def display_dealer_hand(dealer_hand):
    print('Dealer hand:')
    display_hand(dealer_hand, True)

def display_hands(player_hand, dealer_hand):
    display_player_hand(player_hand)
    display_dealer_hand(dealer_hand)

def determine_winner(player_hand, dealer_hand):
    player_total = calculate_hand_total(player_hand)
    dealer_total = calculate_hand_total(dealer_hand)
    if busted(dealer_hand) or player_total > dealer_total:
        return PLAYER
    if busted(player_hand) or dealer_total > player_total:
        return DEALER
    return TIE # player_total == dealer_total

def display_result(player_hand, dealer_hand):
    display_hands(player_hand, dealer_hand)
    winner = determine_winner(player_hand, dealer_hand)
    if winner == TIE:
        points = calculate_hand_total(player_hand)
        prompt(f"It's a tie! Both {DEALER} and {PLAYER} had {points} points!")
    else:
        prompt(f'{winner} won!')

def game_loop():

    prompt("Welcome to Black Jack!")
    while True:
        deck = init_deck()
        shuffle(deck)
        player_hand = deal_card(deck, 2)
        dealer_hand = deal_card(deck, 2)

        display_hands(player_hand, dealer_hand)

        player_loop(deck, player_hand)
        if not busted(player_hand):
            dealer_loop(deck, dealer_hand)

        display_result(player_hand, dealer_hand)

        answer = input("Do you want to play again? y/n")
        if not answer == 'y' or not answer == 'Y':
            prompt("Thanks for playing!")
            break

game_loop()
