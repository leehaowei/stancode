"""
File: hailstone.py
Name: Howard Lee
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    The function will perform the calculation of Hailstone sequence, until the value reaches 1.
    """
    step = 0
    num = int(input('Enter a number: '))

    if num == 1:
        print('It took ' + str(step) + ' steps to reach 1')
    else:
        while True:
            if num == 1:
                break

            step += 1
            old_num = num
            if (num % 2) == 0:  # evaluate whether a number is even
                num = num // 2
                print(str(old_num) + ' is even, so I take half: ' + str(num))
            else:
                num = 3 * num + 1
                print(str(old_num) + ' is odd, so I make 3n+1: ' + str(num))

        print('It took ' + str(step) + ' steps to reach 1')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
