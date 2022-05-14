from art import logo
print(logo)
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  return random.choice(cards)

deal_card() 

def test():
  user_cards = []
 
  user_cards1 = deal_card() 
  user_cards2 = deal_card()
  user_cards = user_cards1, user_cards2
  total_score= user_cards1 + user_cards2
  return(f"Your cards are {user_cards}, your curent score: {total_score}")
print(test())

def computer():
  computer_card = deal_card()
  computer_second_card = deal_card()
  #print(f"Computer's fist card: {computer_card}")
  total_comp = computer_card + computer_second_card
  return total_comp
  if total_comp < 12:
    computer_third_card = deal_card()
    total_comp = total_comp + computer_third_card
    return total_comp
  elif  total_comp < 22:
    print("you lose")
computer()
print(computer())

#@#########import random
from art import logo
print(logo)
def add(cart1, cart2):
  return cart1 + cart2
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
  play = input("do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if play == 'y':
    def user_cards1(first_card,second_card1):
      cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
      user_cards = random.choices(cards, k = 2)
      print(user_cards)
      for cards in user_cards:
        total_amount_cards = {}
        first_card = user_cards[0]
        second_card1 = user_cards[1]
        total_function = first_card + second_card1
        total_amount_cards[cards] = total_function
        user_cards(first_card,second_card1)
      return (first_card + second_card1)
    user_cards1(first_card,second_card1)
    if user_cards1 > 22:
      print("you lose")
      blackjack()
    else:  
      second_card = input("type 'y' for another card, type 'no' to pass: ")
      total_function = total_function + second_card
  computer_choice = random.choices(cards, k = 2)
  firstcard = computer_choice[0]
  secondcard = computer_choice[1]
  total_computer_choice = firstcard + secondcard
  print(total_computer_choice)
  if total_computer_choice < 12:
    thirdcard = random.choice(cards)
    total_computer_choice = thirdcard + total_computer_choice
    print(total_computer_choice)
  elif total_computer_choice > 22:
    return "Bang"
  print(firstcard)
  print(secondcard)
blackjack()
# total_amount_cards = {
#   custumer: "total_function"
# }
# def game():
#   play = input("do you want to play a game of Blackjack? Type 'y' or 'n': ")
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#   if play == 'y':
#   #print(play)
#     new_game = True
#     user_cards = []
#     while new_game == True:
#       player_cards = {}
#       user_cards = random.choices(cards, k = 2)
#       print(user_cards)
#       for cards in user_cards:
#         first_card = user_cards[0]
#         second_card1 = user_cards[1] 
#         total_function = first_card + second_card1
#         print(f"{first_card} + {second_card1} = {total_function}")
#       second_card = input("type 'y' for another card, type 'no' to pass: ")
#       if second_card == 'y':
#         second_card_loop = True
#         while second_card_loop == True:
#           user_cards_2 = random.choices(cards, 1)
#           # total_cards = user_cards + user_cards_2
#           # return total_cards
#           print(user_cards_2)
#       else:
#         second_card = False
# game()   
