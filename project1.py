import random

def roll():
    min_val=1
    max_val=6
    roll=random.randint(min_val,max_val)
    return roll 


while True :

  players=input("enter number of players between 2 -4 ")

  if players.isdigit():
     players=int(players)
     if 2 <= players <= 4:
       break
     else: 
       print("the number of player must be between 2 - 4 ")
  else:
    print("invalide number ")   
   

max_score = 50

players_scor = [0 for _ in range(players)]

while max(players_scor) < max_score:
  print("max score ",max(players_scor))
  for player_idx in range(players):
      current_score = 0
      print("Player",player_idx + 1 ,"turn has just started !")
      while True:
        should_roll = input("would you like to roll(y)")
        if should_roll.lower() !="y":
           break

        value = roll()

        if value == 1:
           current_score = 0 
           print("\n you score turn to 0")
           print("you rolled a 1! Turn done !")
           break
        else:
           print("you roled a " ,value) 
           current_score +=value
           print("your current score is",current_score)
       
        players_scor[player_idx] += current_score
        print("Your total score is: ",players_scor[player_idx])

max_score = max(players_scor)
winning_idx = players_scor.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)        
