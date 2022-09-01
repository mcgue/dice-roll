# Simulate Dice Roll
# import modules
import random


def print_hi(player_name):
    # Greet player
    print(f'Hi, {player_name}')  # Press Ctrl+F8 to toggle the breakpoint.


def roll_dice(max):
    max = int(max)
    return random.randint(1, max)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name_input = input('Ready to play? Enter your name: ')
    print_hi(name_input)
    dice_max = input('How many sides should the dice have?')

print('You rolled a', roll_dice(dice_max), 'and', roll_dice(dice_max))
