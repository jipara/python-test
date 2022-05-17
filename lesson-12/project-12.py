import random
def number():
  choice = random.choice(range(1, 101))
  return choice

def easy_game():
  print("You have 10 attempts remaining to guess the number.")
  attemps = 10
  guess = input("make a guess: ")
  if guess == number:
    return "You win"
  elif guess > number:
    attemps = attepms -1
    print("too high!")
  elif guess < number:
    print("too low")



easy_game()
  
