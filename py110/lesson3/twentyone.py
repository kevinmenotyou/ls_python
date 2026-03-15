import random

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

NEW_LINE='=========================='

PLAYER='Player'
DEALER='Dealer'
TIE='Tie'
DEALER_THRESHOLD=17
MAX_TOTAL=21
NUM_OF_ROUNDS=5



def init_score():
    return {
        PLAYER: 0,
        DEALER: 0
    }

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

def busted(total):
    if total > MAX_TOTAL:
        return True
    return False

def player_loop(deck, player_hand):
    HIT_ANSWERS=['h', 'H', 'hit', 'Hit']
    STAY_ANSWERS=['s', 'S', 'stay', 'Stay']
    while True:
        total = calculate_hand_total(player_hand)
        if busted(total):
            break
        answer = input("hit or stay? ")
        if answer in STAY_ANSWERS:
            break
        if answer in HIT_ANSWERS:
            player_hand.extend(deal_card(deck, 1))
            display_player_hand(player_hand)
        else:
            prompt(f'Only {' '.join(HIT_ANSWERS)} {' '.join(STAY_ANSWERS)} are valid answers!')
    if busted(total):
        prompt(f"You went bust with {total} points!")
    else:
        # if player didn't bust, they must have stayed to get here
        prompt("You chose to stay!")

def dealer_loop(deck, dealer_hand):
    display_dealer_hand(dealer_hand)
    total = calculate_hand_total(dealer_hand)
    while total <= DEALER_THRESHOLD:
        dealer_hand.extend(deal_card(deck, 1))
        total = calculate_hand_total(dealer_hand)
        prompt (f"Dealer dealt himself another card, his total is now {total}!")
        display_dealer_hand(dealer_hand)
        if busted(total):
            break
    if busted(total):
        prompt(f"Dealer went bust with {total} points!")

def display_hand(hand, hidden_card = False):
    my_hand = hand.copy()
    for index, card in enumerate(my_hand):
        name = card[0]
        if hidden_card and index == 1: # second card
            prompt('unknown card')
            continue
        name_list = name.split('_')
        name_list[0] = name_list[0].capitalize()
        name_list[2] = name_list[2].capitalize()
        prompt(' '.join(name_list))

def display_player_hand(player_hand):
    print('Player hand:')
    display_hand(player_hand, False)

def display_dealer_hand(dealer_hand, hidden_card = True):
    print('Dealer hand:')
    display_hand(dealer_hand, hidden_card)

def display_hands(player_hand, dealer_hand, hidden_card = True):
    display_player_hand(player_hand)
    display_dealer_hand(dealer_hand, hidden_card)

def determine_winner(player_total, dealer_total):
    if busted(dealer_total) or (not busted(player_total) and player_total > dealer_total):
        return PLAYER
    if busted(player_total) or (not busted(dealer_total) and dealer_total > player_total):
        return DEALER
    return TIE # player_total == dealer_total

def determine_best_of_winner(score):
    if score[PLAYER] > score[DEALER]:
        return PLAYER
    if score[DEALER] > score[PLAYER]:
        return DEALER
    return TIE # player_total == dealer_total

def increment_score(score, winner):
    if winner == PLAYER:
        score[PLAYER] = score[PLAYER] + 1
    if winner == DEALER:
        score[DEALER] = score[DEALER] + 1

def display_score(score):
    prompt(f'Current Round Score - {PLAYER} won {score[PLAYER]} and {DEALER} won {score[DEALER]}')

def display_final_score(score):
    prompt(f'Final Score - {PLAYER} won {score[PLAYER]} and {DEALER} won {score[DEALER]}')

def display_result(player_hand, dealer_hand, score):
    display_hands(player_hand, dealer_hand, False) # reveal cards
    player_total = calculate_hand_total(player_hand)
    dealer_total = calculate_hand_total(dealer_hand)
    winner = determine_winner(player_total, dealer_total)
    if winner == TIE:
        prompt(f"It's a tie! Both {DEALER} and {PLAYER} had {player_total} points!")
    else:
        prompt(f'{winner} won!')
    increment_score(score, winner)
    display_score(score)

def play_again():
    answer = ""
    while True:
        answer = input("Do you want to play again? y/n")
        if not (answer == 'y' or answer == 'Y'):
            prompt("Thanks for playing!")
            return False
        if not (answer == 'n' or answer == 'N'):
            prompt("Ok, let's go!")
            return True
        prompt('Only y/Y n/N are valid answers!')

def game_loop():


    print(NEW_LINE)
    prompt(f"Welcome to Black Jack! Best of {NUM_OF_ROUNDS} wins!")
    while True:
        score = init_score()
        for i in range(1, NUM_OF_ROUNDS + 1):
            print(NEW_LINE)
            prompt(f'Round {i}!')

            deck = init_deck()
            shuffle(deck)
            player_hand = deal_card(deck, 2)
            dealer_hand = deal_card(deck, 2)

            display_hands(player_hand, dealer_hand)

            player_loop(deck, player_hand)
            player_total = calculate_hand_total(player_hand)
            print(NEW_LINE)

            if not busted(player_total):
                dealer_loop(deck, dealer_hand)
            print(NEW_LINE)

            display_result(player_hand, dealer_hand, score)
            print(NEW_LINE)

        prompt(f'Best of {NUM_OF_ROUNDS} completed!')
        display_score(score)
        round_winner = determine_best_of_winner(score)
        if round_winner == TIE:
            prompt("It's a tie!")
        else:
            prompt(f'{round_winner} won!')

        if not play_again():
            break

game_loop()
