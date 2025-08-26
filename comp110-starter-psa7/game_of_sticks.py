"""
Module: game_of_sticks

Implementation of the Game of Sticks, including an AI that learns the game,
either by playing against a human, or by pre-training against another AI.

Authors:
1) Cavin Nguyen - cavinnguyen@sandiego.edu
2) Jessica Cervantes - jessicacervantes@sandiego.edu
"""

import random


def get_player_selection(player_number, sticks_left):
    """
    This function gets the user's input to choose amount of sticks to take away. Prevents user from choosing anything other than 1-3 respective to sticks left.

    Parameters:
    player_number (type: int) - player 1 or player 2
    sticks_left (type: int) - sticks left in the game
    
    Return:
    choice (type: int) - returns the value of what the player chooses.
    """
    while True:
        if sticks_left >= 3:
            choice = int(input(f"Player {str(player_number)}: How many sticks do you take (1-3)? "))
            if 1 <= choice <= 3:
                break
        elif sticks_left == 2:
            choice = int(input(f"Player {str(player_number)}: How many sticks do you take (1-2)? "))
            if 1 <= choice <= 2:
                break
        elif sticks_left == 1:
            choice = int(input(f"Player {str(player_number)}: How many sticks do you take (1-1)? "))
            if choice == 1:
                break

    return choice
            

def player_vs_player(num_sticks):
    """
    This function runs the sticks game between player vs player.

    Parameters:
    num_sticks (type: int) - number of sticks initialized to start the game

    Return:
    None
    """

    while True:
        if num_sticks >= 1:
            choice = get_player_selection(1, num_sticks)
            num_sticks -= choice
            player = True
            if num_sticks > 1:
                print(f"There are {num_sticks} on the board.")
            else:
                print(f"There is {num_sticks} on the board.")
        if num_sticks >= 1:
            choice = get_player_selection(2, num_sticks)
            num_sticks -= choice
            player = False
            if num_sticks > 1:
                print(f"There are {num_sticks} on the board.")
            else:
                print(f"There is {num_sticks} on the board.")
        else:
            if player == True:
                print("Player 1, you lose.")
            else:
                print("Player 2, you lose.")
            break


def initialize_hats(num_sticks):
    """
    Creates the hat dictionary for the games.

    Parameters:
    num_sticks (type: int) - number of sticks to create number of keys in dict.
    
    Return:
    hats (type: dictionary) - returns a dictionary of lists of possible values that the AI can choose.
    """
    hats = {1:[1], 2:[1, 2]}	
    for num in range(3, num_sticks + 1):
        hats[num] = [1, 2, 3]
    return hats	

def update_hats(hats, besides, ai_won):
    """
    Updates the hats dictionary if the AI won or loss.

    Parameters:
    hats (type: dictionary) - dictionary of lists of possible values that the AI can choose.
    besides (type: dictionary) - dictionary of ints used to update the dict.
    ai_won (type: boolean) - boolean used as a conditional to determine different actions.

    Return:
    None
    """
    if ai_won == True:
        for key in besides:
            hats[key].append(besides[key])
            hats[key].append(besides[key])
    elif ai_won == False:
        for key in besides:
            if besides[key] not in hats[key]:
                hats[key].append(besides[key])

def get_ai_selection(sticks_left, hat, besides):
    """
    Gets AI's selection randomly based sticks left.

    Parameters:
    sticks_left (type: int) - sticks left in the game
    hat (type: dictionary) - dictionary of lists of possible values that the AI can choose.
    besides (type: dictionary) - dictionary of ints used to store values the AI chose.

    Return:
    choice (type: int) - integer value of the random choice.
    """
    choice = random.choice(hat[sticks_left])
    hat[sticks_left].remove(choice)
    besides[sticks_left] = choice

    return choice


def player_vs_ai(num_sticks, training_rounds):
    """
    Runs the player vs ai game which trains the ai and prompts the user.

    Parameters:
    num_sticks (type: int) - number of sticks to create number of keys in dict.
    training_rounds (type: int) - number of rounds to train the AI

    Return:
    None
    """
    hats = pretrain_ai(num_sticks, training_rounds)
    sticks_left = num_sticks
    besides = {}
    write_hat_contents(hats,"hat-contents.txt")
    while True:
        if sticks_left >= 1:
            choice = get_player_selection(1, sticks_left)
            sticks_left -= choice
            ai_won = True

            if sticks_left > 1:
                print(f"There are {sticks_left} on the board.")
            else:
                print(f"There is {sticks_left} on the board.")

        if sticks_left >= 1:
            choice = get_ai_selection(sticks_left, hats, besides)
            print(f"AI selects {choice}")
            sticks_left -= choice
            ai_won = False

            if sticks_left > 1:
                print(f"There are {sticks_left} on the board.")
            else:
                print(f"There is {sticks_left} on the board.")
        else:
            
            if ai_won == True:
                print("You lose.")
            else:
                print("AI loses.")
            update_hats(hats, besides, ai_won)
            
            while True:
                again = int(input("Play again (1 = yes, 0 = no)? "))
                if again == 0:
                    break
                elif again == 1:
                    sticks_left = num_sticks
                    besides = {}
                    break
            if again == 0:
                break 
    
def pretrain_ai(num_sticks, training_rounds):
    """
    Trains AI simulating to play a certain number of rounds with another AI.

    Parameters:
    num_sticks (type: int) - number of sticks to create number of keys in dict.
    training_rounds (type: int) - number of rounds to train the AI
    
    Return:
    hats_2 (type: dictionary) - returns a dictionary of lists of possible choices that was trained based on the number of training rounds.
    """

    hats_1 = initialize_hats(num_sticks)
    hats_2 = initialize_hats(num_sticks)
    sticks_left = num_sticks

    for i in range(training_rounds):
        besides_1 = {}
        besides_2 = {}
        while True:
            if sticks_left >= 1:
                choice_1 = get_ai_selection(sticks_left, hats_1, besides_1)
                sticks_left -= choice_1
                ai_one_won = False

            if sticks_left >= 1:
                choice_2 = get_ai_selection(sticks_left, hats_2, besides_2)
                sticks_left -= choice_2
                ai_one_won = True

            else:
                update_hats(hats_1, besides_1, ai_one_won)
                
                update_hats(hats_2, besides_2, not(ai_one_won))
                besides_1 = {}
                besides_2 = {}
                sticks_left = num_sticks
                break
    return hats_2


def write_hat_contents(hats, filename):
    """
    Replace this fake docstring comment with a real one with the proper
    formatting.

    Parameters:
    hats (type: dictionary) - dictionary of lists of possible values that the AI can choose
    filename (type: string) - name of file to write into or create.

    Return:
    None
    """
    
    f = open(filename, "w")
    f.write("Hat Number: (1's, 2's, 3's)\n")
    
    for keys,values in hats.items():
        f.write(f"{keys}: ({values.count(1)}, {values.count(2)}, {values.count(3)})\n")
    
    f.close()

def main():
    """
    Asks the user how many sticks and whether they want to play with a friend, a untrained computer, or a trained computer.
    """
    print("Welcome to the Game of Sticks!")


    while True:
        num_sticks = int(input("How many sticks are there on the table initially (10-100)? "))
        if 10 <= num_sticks <= 100:
            while True:
                print("Options:\n", "Play against a friend (1)\n", "Play against the computer (2)\n", "Play against the trained computer (3)\n")
                mode = int(input("Which option do you take (1-3)? "))
                if mode == 1:
                    player_vs_player(num_sticks)
                    break
                elif mode == 2:
                    player_vs_ai(num_sticks, 0)
                    break
                elif mode == 3:
                    print("Training AI, please wait...")
                    player_vs_ai(num_sticks, 1000)
                    break
            break



if __name__ == "__main__":
    main()

