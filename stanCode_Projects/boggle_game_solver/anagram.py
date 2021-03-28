"""
File: anagram.py
Name: Howard
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variables
dic = {}   # a list to store all strings in a FILE
z


def main():
    global ans
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        ans = []
        word = input('Find anagrams for: ')
        if word == EXIT:
            break
        else:
            find_anagrams(word)
            print(f'{len(ans)} anagrams:  {ans}')


def find_anagrams(s):
    """
    A function to find all possible anagram and add them to the global variable ans.
    :param s: str, a word user input to find the anagrams.
    :return: list, a list containing of the anagrams found in the dictionary.
    """
    print('Searching...')
    return helper(s)


def helper(s, current=''):
    """
    A helper function to implement recursions.
    :param s: str, a word user input to find the anagrams.
    :param current: the current word created in the recursion. Starts with empty string.
    """
    # Base Case: when character option left is zero
    if len(s) == 0:
        if current in dic and current not in ans:
            ans.append(current)
            print('Found:  ' + current)
            print('Searching...')
    for i in range(len(s)):
        # Choose
        new_current = current + s[i]
        new_s = s[0:i] + s[i+1:]  # a word without the character just being chosen.
        # to skip the words that start with prefix that are not founded in the dictionary.
        if has_prefix(new_current):
            # Explore
            helper(new_s, new_current)


def read_dictionary():
    """
    This function reads the dictionary.txt file, parse the stings and append them into a global variable list.
    """
    with open(FILE, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            if line not in dic:
                dic[line] = 1


def has_prefix(sub_s):
    """
    This function will check every word in a file ot see whether any of them has the prefix substring.
    :param sub_s: str, the prefix of a word
    :return: bool
    """
    for s in dic:
        if s.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
