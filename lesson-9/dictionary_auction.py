from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")

# key_name = input("What is your name?")
# bid_price = input(int("Bid price?"))

auction_dictionary = {}
# key_name = auction_dictionary[key_name]
# auction_dictionary[key_name] = bid_price
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
print(f"The winner is {winner} with bid of ${highest_bid}")    

other_bidders = True
while other_bidders:    
  key_name = input("What is your name?: \n")
  bid_price = int(input("Bid price?: $\n"))
  auction_dictionary[key_name] = bid_price
  should_continue = input("there are other users? 'yes' or 'no'\n")
  if should_continue == 'no':
    other_bidders = False
    find_highest_bidder(bid_price)
  elif should_continue == 'yes':
    clear()
