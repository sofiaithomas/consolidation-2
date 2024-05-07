# Tuple out Game
# Idea for advanced topic: histogram graph with matplotlib for frequency of numbers rolled
import random
end_score = 50

print("Welcome to the 'Tuple Out' dice game! ")

# a function for rolling the die would be more efficient than 3 different variables
def roll_dice():
    # empty list for dice
    dice = []
    #needs to run 3 times
    while count < 3:
        dice.append(random.randint(1,6))
        count += 1
    return dice

# function to run the actual game
def play_game():
    