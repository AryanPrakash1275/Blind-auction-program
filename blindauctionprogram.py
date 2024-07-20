import os
from art import logo

def clear():  
    if os.name == 'nt': 
        os.system('cls')
    else:  
        os.system('clear')

print(logo)

bids={}
bidding_done = False

def highest_bidder(bids):
  highest_bid = 0
  winner = ""
  for bidder in bids:
    user_bid = bids[bidder]
    if user_bid > highest_bid:
      highest_bid = user_bid
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_done:
  user_name = input("What is your name?")
  user_bid = int(input("What is your bid?"))
  bids[user_name] = user_bid
  proceed = input("Anymore more bidders?")
  if proceed == "no":
    highest_bidder(bids)
    bidding_done = True
  elif proceed == "yes":
    clear()
   