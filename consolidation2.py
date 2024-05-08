# Tuple out Game
# Idea for advanced topic: histogram graph with matplotlib for frequency of numbers rolled
import random
end_score = 50

print("Welcome to the 'Tuple Out' dice game! ")
# Going to need to ask how many players
num_players = int(input("This is a single player game - Type 1: "))

# a function for rolling the die would be more efficient than 3 different variables
def roll_dice():
    count = 0
    # empty list for dice
    dice = []
    #needs to run 3 times
    while count < 3:
        dice.append(random.randint(1,6))
        count += 1
    return dice

# function to run the actual game
def play_game(num_players):
    '''
    While the players score is less than 50 the function uses the roll dice function to generate rolls each time
    It adds the limits of tupling in the game and allows for rerolls
    Adds the rolled dice and adds it to the players score prior to the next roll.
    '''
    # score for players
    # basically will make a score list of scores = [0] or [0,0] if there is 2 players
    scores = [0] * num_players
    while max(scores) < 50:
        player_score = 0
        while True:
            dice = roll_dice()
            print("These are your rolled die: ", dice)
            # up to here if runs infinitely displaying your rolled dice, now need to update the score so it doesn't run forever

            # if statement for tupling
            if dice[0] == dice[1] == dice[2]:
                print("Uh oh you have tupled! You get 0 points to your score this round")
                player_score = 0
                break
            
            choice = input("Do you want to reroll any dice? (y or n): ").lower()
            if choice != 'y':
                player_score += sum(dice)
                break
    print("You finally hit 50 points!")
    