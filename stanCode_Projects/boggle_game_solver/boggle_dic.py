"""
File: boggle.py
Name: Howard
----------------------------------------
TODO: The programme allows users to input 16 words and the boggle function will help find every possible answer
      in the dictionary.txt.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variable
dic = {}
# eight possible coordinates to move.
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]


def main():
    read_dictionary()
    board = []
    # to set up a board
    for i in range(1, 5):
        current = input(f'{i} row of letters: ')
        current = current.lower()
        if len(current) > 7 or current[1] != ' ' or current[3] != ' ' or current[5] != ' ':
            print('Illegal input')
            break
        else:
            current = list(current.replace(' ', ''))
            board.append(current)
    boggle(board)

def boggle(board):
    """
    This function help solve a boggle game.
    :param board: [str], a list of strings that user input.
    """
    # initiate a 4*4 switches for checking if a character has been visited. All set to be False at first.
    passed = [[False for x in range(4)] for y in range(4)]
    # a empty list to store all valid answers
    final = []
    for i in range(4):
        for j in range(4):
            helper(board, final, passed, i, j)
    print(f'There are {len(final)} words in total.')


def helper(board, final, passed, i, j, path=''):
    """
    A helper function of boggle function
    :param board: [str], a list of strings that user input.
    :param final: a list of all valid answers, used to count the total amount.
    :param passed: a switch used to check if a character have been visited.
    :param i: row index of a character
    :param j: column index of a character
    :param path: str, the characters that have been visited on a certain iteration.
    """
    passed[i][j] = True
    path += board[i][j]
    if len(path) >= 4:
        if path in dic and path not in final:
            final.append(path)
            print(f'Found "{path}"')
    # check all 8 neighbors
    for k in range(8):
        if has_prefix(path):
            if valid(i + row[k], j + col[k], passed):
                helper(board, final, passed, i + row[k], j + col[k], path)
    passed[i][j] = False


def valid(x, y, passed):
    """
    This function check if the index is in the valid area.
    :param x: row index of a character
    :param y: column index of a character
    :param passed: a switch used to check if a character have been visited.
    :return: bool
    """
    return (0 <= x < 4) and (0 <= y < 4) and not passed[x][y]


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            if line not in dic:
                dic[line] = 1


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for s in dic:
        if s.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()

