import random


def create_1_deck():
    ranks = ['A', '2', '3', '4', '5', '6', '7','8','9','10','J','Q','K']
    suits = ['♦', '♣', '♠', '♥']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    return deck

def combine_decks(number_of_decks):
    stack = []
    for _ in range(number_of_decks):
        stack += create_1_deck()
    random.shuffle(stack)
    return stack

def draw_card():
    while True:
        drawn_card = stack[0]
        try:
            stack.pop(0)
        except ValueError:
            continue
        else:
            drawn_card = ''.join(drawn_card)
            return drawn_card

def game_start():
    print('player hand: ', *player_hand, '    score:', score_display(player_hand))
    print('dealer hand: ', ''.join(dealer_hand[0]), '??', '    score:', score_display([dealer_hand[0]]))
    return

def score(hand): #type list
    score = 0
    score_2 = 0
    aces = 0
    for card in hand:
        try:
            if card[0] == '1':
                score += 10
            else:
                score += int(card[0])
        except ValueError:
            if card[0] == 'A':
                aces += 1
                score += 11
            else:
                score += 10
    for _ in range(aces):
        if score > 21 :
            score -= 10
        elif score < 21 :
            score_2 = score - 10
    return score, score_2

def score_display(hand):
    score_1, score_2 = score(hand)
    if score_2 == 0:
        return f'{score_1}'
    else :
        return f'{score_2}/{score_1}'



def player_hit():
    global lost, betting, money, won
    print('Player hit')
    player_hand.append(draw_card())
    print('player hand: ', *player_hand,  '    score:', score_display(player_hand))
    print('dealer hand: ', ''.join(dealer_hand[0]), '??')
    if check_busted(player_hand):
        print('    Lost, player busted', '\n')
        lost += 1
        print(f'Lost {betting}$')
        print(f'Remaining balance: {money}$')
        return False


    return True

def player_stayed():
    global lost, betting, money, won
    print('Player stayed')
    if 21 >= score(dealer_hand)[0] >= 17:
        print('dealer hand: ', *dealer_hand, '    score:', score_display(dealer_hand))
    while score(dealer_hand)[0] < 17:
        dealer_hand.append(draw_card())
        print('dealer hand: ', *dealer_hand,  '    score:', score_display(dealer_hand))

    if score(dealer_hand)[0] > 21:
        print('    Won, dealer busted', '\n')
        won += 1
        print(f'Won {betting*2}$')
        money += betting*2
        print(f'Remaining balance: {money}$')
        return True
    compare_score(player_hand, dealer_hand)
    return

def check_busted(hand):
    if score(hand)[0] > 21:

        return True
    else :
        return False

def compare_score(hand_1, hand_2):
    global lost, betting, money, won, flag_doubled
    player_score = score(hand_1)[0]
    dealer_score = score(hand_2)[0]
    if dealer_score > player_score :
        print('    Lost, less points', '\n')
        lost += 1
        if flag_doubled:
            print(f'Lost {betting*2}$')
            print(f'Remaining balance: {money}$')
        else :
            print(f'Lost {betting}$')
            print(f'Remaining balance: {money}$')

        return
    elif dealer_score == player_score :
        print('    Draw, same points', '\n')
        if flag_doubled:
            print(f'Regained {betting*2}$')
            money += betting*2
            print(f'Remaining balance: {money}$')
        else:
            print(f'Regained {betting}$')
            money += betting
            print(f'Remaining balance: {money}$')
        return
    else:
        print('    Won, more points', '\n')
        won += 1
        if flag_doubled:
            money += betting * 4
            print(f'Won {betting * 4}$')
            print(f'Remaining balance: {money}$')
        else:
            money += betting*2
            print(f'Won {betting*2}$')
            print(f'Remaining balance: {money}$')
        return

def player_doubled():
    global lost, betting, money, won, flag_doubled
    flag_doubled = True
    print('Player doubled')
    money = money - betting
    print(f'Remaining balance: {money}$')
    player_hand.append(draw_card())
    print('player hand: ', *player_hand, '    score:', score_display(player_hand))
    print('dealer hand: ', ''.join(dealer_hand[0]), '??')
    if check_busted(player_hand):
        print('    Lost, player busted', '\n')
        lost += 1
        print(f'Lost {betting*2}$')
        print(f'Remaining balance: {money}$')
        return False
    else:
        if 21 >= score(dealer_hand)[0] >= 17:
            print('dealer hand: ', *dealer_hand, '    score:', score_display(dealer_hand))
        while score(dealer_hand)[0] < 17:
            dealer_hand.append(draw_card())
            print('dealer hand: ', *dealer_hand, '    score:', score_display(dealer_hand))

        if score(dealer_hand)[0] > 21:
            print('    Won, dealer busted', '\n')
            won += 1
            print(f'Won {betting * 4}$')
            money += betting * 4
            print(f'Remaining balance: {money}$')
            return True
        compare_score(player_hand, dealer_hand)
        return

def is_able_to_split(hand):
    if len(hand) == 2 and hand[0][0] == hand[1][0]
        return True
    return False

def player_split(hand):
    hand1 = [hand[0]]
    hand2 = [hand[1]]
    print('Hand 1: ',*hand1)
    print('Hand 2: ',*hand2)
    print('Playing hand 1:')

def split_hand_play(hand):
    hand.append(stack[0])



#game start
if input('[y] to start: ') == 'y' :
    number_of_decks = int(input('Number of decks: '))
    stack = combine_decks(number_of_decks)
    won = lost = 0
    money = int(input('Starting money?: '))
    print('Shuffling')
    next_round = 'y'
    while next_round == 'y' and money > 0:
        if len(stack) < 15:
            print('Not enough cards, reshuffling the stack', '\n')
            stack = combine_decks(number_of_decks)
        print(f'Balance: {money}$')
        while True:
            betting = int(input('Betting amount: '))
            if betting > money:
                print('Insufficient funds')
                continue
            else :
                break
        money = money - betting
        print(f'Remaining balance: {money}$')
        player_hand = [draw_card(), draw_card()]
        dealer_hand = [draw_card(), draw_card()]
        game_start()



        win = True


    #in game
        while win:
            if score(player_hand)[0] == 21 and len(player_hand)==2:
                print('Blackjack!')
                won += 1
                money += betting*2.5
                print(f'Won {betting*2.5}$')
                print(f'Current balance: {money}$')
                break
            flag_doubled = False
            if len(player_hand) == 2 and betting <= money:
                if input('Double?[y]:' ) == 'y' :
                    player_doubled()
                    break
            response = input('Hit[h] or Stay[s]: ')
            if response == 'h' :
                win = player_hit()
            else:
                player_stayed()
                break
        print(f'W: {won} ; L: {lost}')
        next_round = input("Continue?[y] :")
    else:
        print('Exiting')

#exiting game
else :
    print('Exiting')