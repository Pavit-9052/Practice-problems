'''
Games

Problem #1
Play the game Rock Papar Scissors with the computer.
Play it three times and best of three wins. 
If you win, print your name in color (look for a python package to do this)
Hint - Use random number generation

Problem #2
Two player dice game.
Each player will roll the die (numbers from 1 to 6)
Points are added to each roll.
1 - 1 pt
2 - 5 pts
3 - 15 pts
4 - (-15) pts
5 - (-5) pts
6 - (-1) pts'''

import random

def dice_roll():
    return random.randint(1, 6)

def calculate_points(roll):
    if roll == 1:
        return 1
    elif roll == 2:
        return 5
    elif roll == 3:
        return 15
    elif roll == 4:
        return -15
    elif roll == 5:
        return -5
    elif roll == 6:
        return -1

def play_game():
    scores = [0, 0]
    rolls = [0, 0]

    while max(scores) <= 100:
        for player in range(2):
            roll = dice_roll()
            points = calculate_points(roll)
            scores[player] += points
            rolls[player] += 1

            print(f"Player {player + 1} rolled a {roll} and earned {points} points. Total points: {scores[player]}")

            if scores[player] >= 100:
                return player + 1, rolls[player]
            
winner, num_rolls = play_game()

print(f"Player {winner} wins! They reached 100 points in {num_rolls} rolls.")

OUTPUT:-
Player 1 rolled a 3 and earned 15 points. Total points: 15
Player 2 rolled a 6 and earned -1 points. Total points: -1
Player 1 rolled a 5 and earned -5 points. Total points: 10
Player 2 rolled a 6 and earned -1 points. Total points: -2
Player 1 rolled a 2 and earned 5 points. Total points: 15
Player 2 rolled a 6 and earned -1 points. Total points: -3
Player 1 rolled a 1 and earned 1 points. Total points: 16
Player 2 rolled a 6 and earned -1 points. Total points: -4
Player 1 rolled a 1 and earned 1 points. Total points: 17
Player 2 rolled a 4 and earned -15 points. Total points: -19
Player 1 rolled a 2 and earned 5 points. Total points: 22
Player 2 rolled a 5 and earned -5 points. Total points: -24
Player 1 rolled a 4 and earned -15 points. Total points: 7
Player 2 rolled a 6 and earned -1 points. Total points: -25
Player 1 rolled a 2 and earned 5 points. Total points: 12
Player 2 rolled a 6 and earned -1 points. Total points: -26
Player 1 rolled a 6 and earned -1 points. Total points: 11
Player 2 rolled a 5 and earned -5 points. Total points: -31
Player 1 rolled a 6 and earned -1 points. Total points: 10
Player 2 rolled a 5 and earned -5 points. Total points: -36
Player 1 rolled a 4 and earned -15 points. Total points: -5
Player 2 rolled a 4 and earned -15 points. Total points: -51
Player 1 rolled a 6 and earned -1 points. Total points: -6
Player 2 rolled a 1 and earned 1 points. Total points: -50
Player 1 rolled a 1 and earned 1 points. Total points: -5
Player 2 rolled a 6 and earned -1 points. Total points: -51
Player 1 rolled a 5 and earned -5 points. Total points: -10
Player 2 rolled a 6 and earned -1 points. Total points: -52
Player 1 rolled a 3 and earned 15 points. Total points: 5
Player 2 rolled a 4 and earned -15 points. Total points: -67
Player 1 rolled a 5 and earned -5 points. Total points: 0
Player 2 rolled a 6 and earned -1 points. Total points: -68
Player 1 rolled a 6 and earned -1 points. Total points: -1
Player 2 rolled a 2 and earned 5 points. Total points: -63
Player 1 rolled a 1 and earned 1 points. Total points: 0
Player 2 rolled a 5 and earned -5 points. Total points: -68
Player 1 rolled a 3 and earned 15 points. Total points: 15
Player 2 rolled a 1 and earned 1 points. Total points: -67
Player 1 rolled a 1 and earned 1 points. Total points: 16
Player 2 rolled a 1 and earned 1 points. Total points: -66
Player 1 rolled a 6 and earned -1 points. Total points: 15
Player 2 rolled a 4 and earned -15 points. Total points: -81
Player 1 rolled a 3 and earned 15 points. Total points: 30
Player 2 rolled a 6 and earned -1 points. Total points: -82
Player 1 rolled a 6 and earned -1 points. Total points: 29
Player 2 rolled a 4 and earned -15 points. Total points: -97
Player 1 rolled a 3 and earned 15 points. Total points: 44
Player 2 rolled a 4 and earned -15 points. Total points: -112
Player 1 rolled a 5 and earned -5 points. Total points: 39
Player 2 rolled a 4 and earned -15 points. Total points: -127
Player 1 rolled a 3 and earned 15 points. Total points: 54
Player 2 rolled a 3 and earned 15 points. Total points: -112
Player 1 rolled a 6 and earned -1 points. Total points: 53
Player 2 rolled a 1 and earned 1 points. Total points: -111
Player 1 rolled a 3 and earned 15 points. Total points: 68
Player 2 rolled a 5 and earned -5 points. Total points: -116
Player 1 rolled a 3 and earned 15 points. Total points: 83
Player 2 rolled a 5 and earned -5 points. Total points: -121
Player 1 rolled a 3 and earned 15 points. Total points: 98
Player 2 rolled a 6 and earned -1 points. Total points: -122
Player 1 rolled a 5 and earned -5 points. Total points: 93
Player 2 rolled a 1 and earned 1 points. Total points: -121
Player 1 rolled a 3 and earned 15 points. Total points: 108
Player 1 wins! They reached 100 points in 32 rolls.


Find which player scores 100 first and how many time they had to roll the die.
Hint - use random numbers to generate the die (no need to get user input)
Use Arrays and while loop.

Problem #3
Write an app for the follwoing two player game. You have a 6 x 6 board. 
Users take turns rolling the dice twice. first roll is row no, second roll is col number. Mark the spot (row, col) as claimed by the user
who rolled the dice.
When the user rolls the dice within 1 col/row of a claimed spot of the other user, the other user gets a point. 
If the spot is same as the claimed spot of the other user, the user that rolled the dice gets a point. 
The player who gets 5 points first wins the game. 
 
'''
