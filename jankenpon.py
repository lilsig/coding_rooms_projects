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

rps = [rock, paper, scissors] #list rock=0 paper=1 scissors=2

import random
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("You chose:\n" + rps[userChoice]) #the number you choose indicates the index of the list so the index is going to be 'choice'

cpuChoice = random.randint(0, 2)
print("Computer chose:\n" + rps[cpuChoice])

win = (userChoice == 0 and cpuChoice == 2) or (userChoice == 1 and cpuChoice == 0) or (userChoice == 2 and cpuChoice == 1)
lose = (userChoice == 2 and cpuChoice == 0) or (userChoice == 0 and cpuChoice == 1) or (userChoice == 1 and cpuChoice == 2)
draw = (userChoice == cpuChoice)

if win:
    print("You win!")
elif lose:
    print("You lose!")
elif draw:
    print("It's a draw!")


