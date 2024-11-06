import random

want_to_quit = '' #empty string is false, any string is true
while not want_to_quit:
    dice_value = random.randint(1,6)
    print(f'You rolled a {dice_value}')
    want_to_quit = input('Roll again? Press enter to roll again, any other key to quit. ')
