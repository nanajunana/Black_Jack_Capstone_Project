import  random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = None
will_play = input("Do you want to play Blackjack? press y")

if will_play == 'y':
    play = True

player_cards = []
computer_cards = []

def shuffle(hand):
    hand.append(random.choice(cards))

while play:
    shuffle(player_cards)
    shuffle(player_cards)
    shuffle(computer_cards)
    shuffle(computer_cards)

    print(f"Your cards: {player_cards}")
    print(f"Dealer cards: {computer_cards[0]}")

    add_more = input("Would you like to draw another card? 'y' or 'n'")

    if add_more == 'y':
        shuffle(player_cards)

    sum_player = sum(player_cards)
    sum_computer = sum(computer_cards)

    if sum_computer <= 11:
        shuffle(computer_cards)
    elif sum_computer < 15:
        decision = random.randint(0,1)
        if decision == 0:
            shuffle(computer_cards)

    if 11 in player_cards and sum_player > 21:
        index = player_cards.index(11)
        player_cards[11] = 1

    if 11 in computer_cards and sum_player > 21:
        index = computer_cards.index(11)
        computer_cards[11] = 1

    print(f"Your cards: {player_cards} = {sum_player}")
    print(f"Dealer cards: {computer_cards} = {sum_computer}")

    if sum_player > 21:
        print(f"You lose! you are over 21")
    elif sum_computer > 21:
        print(f"You win! his cards are over 21")
    elif sum_player == sum_computer:
        print(f"Draw! Try again")
    elif sum_player > sum_computer:
        print(f"You win! your total is {sum_player}")
    else:
        print(f"You lose! dealer total is {sum_computer}")

    play_again = input("Do you want to play again? y or n")

    if play_again == 'n':
        play = False
    else:
        player_cards = []
        computer_cards = []