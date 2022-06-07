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
userinput = int(input("What do you choose? Type '0' for rock, '1' for paper, and '2' \nfor scissors."))
choices = (rock, paper, scissors)
computerinput = random.randint(0, 2)

if userinput == 0:
  print(choices[0]) # rock
elif userinput == 1:
  print(choices[1]) # paper
elif userinput == 2:
  print(choices[2]) # scissors

print("The computer chose: " + str(choices[computerinput]))  

if userinput == computerinput:
  print("The round was a draw")
elif userinput == 2 and computerinput == 1:
  print("You won this round!")
elif userinput == 0 and computerinput == 2:
  print("You won this round!")
elif userinput == 1 and computerinput == 0:
  print("You won this round!")
else:
  print("You lose this round..")
