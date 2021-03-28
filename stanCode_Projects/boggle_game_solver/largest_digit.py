"""
File: largest_digit.py
Name: Howard
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	The function will find the largest digit of a number.
	:param n: int, a number
	:return: int, the final largest digit
	"""
	return helper(n, 0)


def helper(n, big):
	"""
	:param n: int, an integer number
	:param big: the current largest digit
	:return: int, the final largest digit
	"""
	n = abs(n)
	if n == 0:
		return big
	else:
		# check the last digit of a number
		if big < int(n % 10):
			big = int(n % 10)
		# check the rest of the digits
		return helper(n/10, big)


if __name__ == '__main__':
	main()
