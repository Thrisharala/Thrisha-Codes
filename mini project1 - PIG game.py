#pig game
import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val,max_val)
    return roll
#roll function

#value = roll()
#print(value)
#the upper comment (code) print a  a random number each time
while True:
    players = input("Enter the number of players(2-4) : ")
    if players.isdigit():
        players = int(players)
        if(1<=players<=4):
            break
        else:
            print(" Number of players must be 2-4. ")
    else:
        print("Invalid, please try again")
#check the condition for players

max_score = 25
player_scores = [0 for _ in range(players)]      #list comprehension

while max(player_scores)<max_score:
    for player_turn in range (players):          # turns for each player
        print("\nPlayer ",player_turn + 1,"turns has just started! ")
        current_score = 0

        while(True):
            want_to_roll = input("want to roll (y): ")
            if want_to_roll!="y":
                break

            value = roll()
            if( value == 1):
                print(" You rolled a 1! Turn done!")
                break
            else:
                current_score += value
                print(" You rolled a ",value)

            print(" The current score is:",current_score)
        
        player_scores[player_turn]+=current_score
        print(" Your final score is : ",player_scores[player_turn])

max_score = max(player_scores)
winner = player_scores.index(max_score)        #gives the max score of each player
print(" The player ", winner+1 ,"is the winner with a score of :",max_score)