"""
File: quadratic_solver.py
Name: Howard Lee
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Users input the coefficient and constant of a quadratic equation,
	and will get the number of root(s) and its(their) value(s).
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	discriminant = b ** 2 - 4 * a * c
	if discriminant < 0:
		print('No real roots')
	else:
		square_root = math.sqrt(discriminant)
		if discriminant == 0:
			root_zero = -b / 2  # The only root, when discriminant = 0
			print('One root: ' + str(root_zero))
		else:
			root_large = (-b + square_root) / 2  # The larger root, when discriminant > 0
			root_small = (-b - square_root) / 2  # The smaller root, when discriminant > 0
			print('Two roots: ' + str(root_large) + ' , ' + str(root_small))


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
