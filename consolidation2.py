# Tuple out Game
import random
end_score = 50

print("Welcome to the 'Tuple Out' dice game! ")

#rolls = 3
#for i in range(0,rolls):
die_1 = random.randint(1,6)
die_2 = random.randint(1,6)
die_3 = random.randint(1,6)

score = die_1 + die_2 + die_3
print(score)