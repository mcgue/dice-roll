# Simulate Dice Roll
# Uses 3.10
# Import module
import random

# Greeting function
def print_hi(player_name):
    # Greet player
    print(f'Hi, {player_name}')

# Roll 1 die function
def roll_dice(max):
    max = int(max)
    return random.randint(1, max)

# Run
if __name__ == '__main__':
    # Get player's name
    name_input = input('Ready to play? Enter your name: ')

    # Say hi and ask how many sides for a die
    print_hi(name_input)
    dice_max = input('How many sides should each die have? ')
    die_1 = roll_dice(dice_max)
    die_2 = roll_dice(dice_max)

print('You rolled a', die_1, 'and', die_2, 'for a', die_1 + die_2)