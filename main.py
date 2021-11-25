import random
print ("Let's play a game. Type 1 for rock, 2 for paper or 3 for scissors.")

playerChoice = input ("Are you ready? Rock, scissors, paper... Shoot!  ")
playerChoice = int(playerChoice)
if playerChoice == 1:
  print ("Your choice is rock")
elif playerChoice == 2:
  print ("Your choice is paper")
elif playerChoice == 3:
  print ("Your choice is scissors")
else:
  print ("Hmm...You've chosen wrong symbol")

computerChoice = random.randint(1,3)
if computerChoice == 1:
  print ("My choice is rock")
elif computerChoice == 2:
  print ("My choice is paper")
elif computerChoice == 3:
  print ("My choice is scissors")


if playerChoice == computerChoice:
  print ("DRAW")

if playerChoice == 1:
  if computerChoice == 2:
    print ("You lost!!!")
  if computerChoice == 3:
    print ("You won!!!")

if playerChoice == 2:
  if computerChoice == 1:
    print ("You won!!!")
  if computerChoice == 3:
    print ("You lost!!!")

if playerChoice == 3:
  if computerChoice == 1:
    print ("You'll never beat me!")
  if computerChoice == 2:
    print ("You won this time...")