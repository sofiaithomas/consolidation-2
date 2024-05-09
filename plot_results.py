import matplotlib.pyplot as plt
import pandas as pd

def plot_dice(dice_rolled):
    """
    """
    dice_dictionary = {"1" : dice_rolled.count(1),
                        "2" : dice_rolled.count(2),
                        "3" : dice_rolled.count(3),
                        "4" : dice_rolled.count(4),
                        "5" : dice_rolled.count(5),
                        "6" : dice_rolled.count(6)}

    dice_numbers = list(dice_dictionary.keys())
    dice_counts = list(dice_dictionary.values())

    dice_data = {"dice number" : dice_numbers,
                    "count of number" : dice_counts}

    dice_dataframe = pd.DataFrame(data = dice_data)
    # graph histogram
    plt.bar(x = "dice number", height = "count of number", data = dice_dataframe)
    plt.show()
    return None
# test 
plot_dice([1, 5, 2, 3, 4, 5, 1, 1, 1, 3, 4])