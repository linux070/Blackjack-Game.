import random
import os
from blackjack_image import logo
# print("Welcome to the Blackjack Capstone game project.\n")
# print(Do you want to play a game of Blackjack? Type 'y' or 'n':").lower())
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # introduces the deck of cards.
def deal_card():
    random_cards = random.choice(cards) # randomly select a card .
    return random_cards

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# compares the user and computer score so i can decide who wins/loses.
def compare(u_score, c_score):
    if c_score == u_score :
        return "It is a draw🤝."
    elif u_score == 0:
        return "Lose, opponent has Blackjack😬."
    elif u_score == 0:
        return "Win with a Blackjack😅."
    elif u_score > 21:
        return "You went over, you lose🥲."
    elif c_score > 21:
        return "Opponent went over, you win😂."
    elif u_score > c_score:
        return "You, you win😎."
    else:
        return "You lose🥹."
    
def play_game():   
    print(logo) # prints the logo output. 
# demo'ed the user and computer cards. 
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2): # generates a range of 2 numbers : for the user and the computer.
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
    # to calculate the actual score.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
    # prints the cards and the current scores of both players at hand
        print(f"Your cards {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score and computer_score == 0 or user_score > 21:
            is_game_over = True
        else :
            should_continue = input("Type 'y' to draw another card, type 'n' to pass? type :").lower() # wants the user to continue playinggggggg.
            if should_continue == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True  
    # ```` this contains the while for the player : Computer ````
    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    # this is just a demo to show the final hands of both players.
    print(f"User's final score: {user_score}")
    print(f"Computer's final score: {user_score}")

    # the final print statement
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
    os.system('cls') #this is to clear the screen
    play_game()


#linuxmode
