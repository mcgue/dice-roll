# Simulate Dice Roll
# import modules
import random

def print_hi(player_name):
    # Greet player
    print(f'Hi, {player_name}')  # Press Ctrl+F8 to toggle the breakpoint.

def roll_dice(max):
    max = int(max)
    return random.randint(1, max)

# Run
if __name__ == '__main__':
    # Get player's name
    name_input = input('Ready to play? Enter your name: ')

    print_hi(name_input)
    dice_max = input('How many sides should each die have? ')
    die_1 = roll_dice(dice_max)
    die_2 = roll_dice(dice_max)

print('You rolled a', die_1, 'and', die_2, 'for a', die_1 + die_2)
