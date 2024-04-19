import random

def deal_cards():
    return [random.randint(1, 10), random.randint(1, 10)]

def play_another_round():
    choice = input("Do you want to play another round? (Type yes or no): ").lower()
    return choice == "yes"

while True:
    player_hand = deal_cards()
    player_total = sum(player_hand)
    bet = input("How much money do you want to bet? ")
    print("You are now betting", bet, "dollars.")
    while True:
        # show the player's hand and total
        if (player_total == 20) and len(player_hand) == 2:
            print("BLACKJACK", player_hand)
            print("Player Wins! (Black Jack)")
            quit()
            
        if player_total > 21:
            print("Player's Hand:", player_hand)
            print("Your hand, " + str(player_total) + ", is over 21")
            print("You lose!")
            break
        print("Player's Hand:", player_hand)
        print("Player's Total:", player_total)

        # Ask the player to hit or stand
        choice = input("Do you want to 'hit' or 'stand'? ").lower()

        if choice == "hit":
            player_hand.append(random.randint(1, 10))
            player_total = sum(player_hand)
        elif choice == "stand":
            break
    print()
    dealer_hand = [random.randint(1, 10), random.randint(1, 10)]

    while sum(dealer_hand) < 17:
        dealer_hand.append(random.randint(1, 10))

    # show the dealer's hand
    print("Dealer's Hand:", dealer_hand)
    print("Dealer's Total:", sum(dealer_hand))

    # Compare player and dealer hands and print who wins
    if player_total > 21:
        print("Player loses! (Over 21)")
        print("You have lost", bet, "dollars.")
    elif sum(dealer_hand) > 21:
        print("Dealer loses! (Over 21)")
        print("Player wins", str(bet) + "$.")
    elif player_total > sum(dealer_hand):
        print("Player wins!")
        print("you have won", bet, "dollars.")
    elif sum(dealer_hand) > 17 and sum(dealer_hand) > player_total and sum(dealer_hand) < 22:
        print("Dealer wins!")
        print("You have lost", bet, "dollars.")
    elif player_total == sum(dealer_hand):
        print("It's a Push (Tie)!")
        print("you still have", bet, "dollars.")
    else:
        print("Dealer wins!")
        print("You have lost", bet, "dollars.")

    if not play_another_round():
        print("Thank You For Playing!")
        break
    print()
    print()
