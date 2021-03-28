"""
File: hangman.py
Name: Howard Lee
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game. It will first check if the user's input is valid, and check if the input is
    in the answer. If so, the life count will be unchanged and the dash will be replace to that letter.
    Ot the other hand, the life count will be deducted one if a the input is not in the answer.
    """
    ans = random_word()
    hint = '-' * len(ans)
    print('The word looks like: ' + hint)
    print('You have ' + str(N_TURNS) + ' guesses left')
    start_game(N_TURNS, hint, ans)


def start_game(life, hint, ans):
    """
    This function will check if the user input is valid.
    If so, it will then check whether the input letter is in the answer.
    The function will keep running until a user win or lose the game.
    :param life: int, The life count when starting a game.
    :param hint: str, the string that gives the hint
    :param ans:
    :return:
    """
    while life > 0:
        guess = input('Your guesses: ')
        up = guess.upper()
        if valid(up):
            correct = check(up, ans)
            if correct:
                hint = replace(up, ans, hint)
                print('You are correct!')
                if hint == ans:
                    break
                else:
                    print('The word looks like: ' + hint)
            else:
                print('There is no ' + up + '\'s word')
                print('The word looks like: ' + hint)
                life -= 1
            print('You have ' + str(life) + ' guesses left')
        else:
            print('illegal format')
    if hint == ans:
        print('You win!!')
    else:
        print('You are completely hung : (')
    print('The word was: ' + ans)


def valid(guess):
    """
    This is a predicate function to check whether a user input is a letter and with only one letter.
    :param guess:
    :return: bool
    """
    if guess.isalpha() and len(guess) == 1:
        return True
    return False


def check(s, ans):
    """
    This is a predicate function to check whether a string is in a given answer.
    :param s: str, the one need to be checked.
    :param ans: str, the given answer.
    :return: bool,
    """
    if s in ans:
        return True
    return False


def replace(s, ans, word):
    """
    This function would check whether a letter is in a given answer.
    If so, it will change the string in the word at same index of ans into s.
    :param s:
    :param ans: str,
    :param word: str,
    :return: str,
    """
    revise = ''
    for i in range(len(ans)):
        ch = ans[i]
        if s == ch:
            revise += ch
        else:
            revise += word[i]
    return revise


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
