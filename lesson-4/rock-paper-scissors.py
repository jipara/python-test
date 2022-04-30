import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]
your_choice = int(input("What is your choice type 0 for rock, type 1 for paper, type 2 for scissors?\n"))
if your_choice >= 3 or your_choice < 0:
  print("your number is out of range")
else:
  print(game_images[your_choice])
  #your_choice = [paper, rock, scissors]
  #print(your_choice)
  computer_choice = random.randint(0, 2)
  print(game_images[computer_choice])

  
  if your_choice == 0 and computer_choice == 2:
    print("you win")
  elif computer_choice == 0 and your_choice ==2:
    print("you lose")
  elif computer_choice > your_choice:
    print("you lose")
  elif your_choice > computer_choice:
    print("you win")
  elif computer_choice == your_choice:
    print("you are even")
  
    
