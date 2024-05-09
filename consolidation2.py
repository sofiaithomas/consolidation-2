# Tuple out Game
# Idea for advanced topic: histogram graph with matplotlib for frequency of numbers rolled
import random
# import pandas as pd
# import matplotlib.pyplot as plt
import plot_results

print("Welcome to the 'Tuple Out' dice game! ")
# Going to need to ask how many players

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
def play_game():
    score = 0
    '''
    While the players score is less than 50 the function uses the roll dice function to generate rolls each time
    It adds the limits of tupling in the game and allows for rerolls
    Adds the rolled dice and adds it to the players score prior to the next roll.
    '''

    while score < 50:
        player_score = 0
        all_dice = []

        while True:
            dice = roll_dice()
            print("These are your rolled die: ", dice)
            # up to here if runs infinitely displaying your rolled dice, now need to update the score so it doesn't run forever
            all_dice.append(dice)
            player_score += sum(dice)

            # if statement for tupling
            if dice[0] == dice[1] == dice[2]:
                print("Uh oh you have tupled! You get 0 points to your score this round")
                player_score = 0
                #print(f"You have a score of: {score}")
                #print("------------------------------")
                break

            elif dice[0] == dice[1] or dice[1] == dice[2] or dice[2] == dice[0]:
                print("The two dice with the same number are fixed")
                reroll_choice = input("Do you want to reroll the unfixed die? y or n: ")
                if reroll_choice == 'y':
                    reroll_die = int(input("Which die in the set is being re-rolled: 1, 2, or 3"))
                    dice[reroll_die - 1] = random.randint(1,6)
                    print("Your dice with the new re-rolled:", dice)
                    all_dice.append(dice)

                    if dice[0] == dice[1] == dice[2]:
                        print("Uh oh you have tupled! You get 0 points to your score this round")
                        player_score + 0
                        break
                else:
                    print(f"Your score is: {score + player_score}")
                    print("----------------------------")
                    break

            
            print(f"Your score is: {score + player_score}")
            print("----------------------------")

        score += player_score
    print(f"Yay! You got over 50 points with a score of {score}")
    return all_dice


dice_rolled = play_game()

plot_results.plot_dice(dice_rolled)