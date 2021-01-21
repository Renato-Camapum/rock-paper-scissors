# This is a simple version of the game, using list and if statements. Have fun!




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
import random


player_choice = int(input("Press '0' for rock, '1' for paper and '2' for scissoors\n"))

weapons = [rock, paper, scissors]
print("You choose")
print(weapons[player_choice])

comp_choice = random.randint(0, 2)
print("Computer choose")
print(weapons[comp_choice])

if player_choice == comp_choice:
  print("It's a draw.")
elif player_choice > comp_choice:
  print("You win")
else:
  if player_choice == 0 and comp_choice == 2:
    print("you win!")
  else:
    print("You lose!")