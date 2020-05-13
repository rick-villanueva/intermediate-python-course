#Random dice roller 

import random
game_on = True

while True:
  while game_on:
    dice_rolls = int(input('How many dice would you like to roll? '))
    dice_size = int(input('How many sides are the dice? '))
    dice_sum = 0
    for i in range(0,dice_rolls):
      roll = random.randint(1,dice_size)
      dice_sum += roll
      if roll == 1:
        print(f'You rolled a {roll}! Critical Fail')
      elif roll == dice_size:
        print(f'You rolled a {roll}! Critical Success!')
      else:
        print(f'You rolled a {roll}')
    print(f'You have rolled a total of {dice_sum}')
    
  play_again: input("Would you like to go again? Enter 'y' or 'n' ")
  
  if play_again[0].lower() == 'y':
    game_on = True
    continue
  else:
    print('Thanks')
    break
    
    


