"""
A program that rolls two dice and prints a message if they roll the same value,
otherwise prints the values of each dice
"""

import random

dice_value_1 = random.randint(1, 6)
dice_value_2 = random.randint(1, 6)
if dice_value_1 == dice_value_2:
    print(f'Both dice rolled {dice_value_1}')
else:
    print(f'You rolled {dice_value_1} and {dice_value_2}')

