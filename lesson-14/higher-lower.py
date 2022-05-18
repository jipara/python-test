from art import logo
print(logo)
import random

from game_data import data

def choice():
  random_star = random.choice(data)
  print (random_star["name"], random_star["description"], random_star["country"])
choice()  
