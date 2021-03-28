"""
File: weather_master.py
Name: Howard Lee
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample?/
run in the Assignment 2 Handout.

"""
# This constant controls when to stop: SENTINEL
QUIT = -100


def main():
	"""
	Users can input unlimited data and get the highest, lowest, the average temperature, and
	the number of days of cold days (temperature lower than 16 degree celsius), until entering the QUIT constant.
	"""
	print('stanCode "Weather Master 4.0"!')
	data = int(input('Next Temperature: (or ' + str(QUIT) + ' to quit)?'))

	if data == QUIT:
		print('No temperatures were entered.')
	else:
		num_data = 1   # number of data
		total = data   # sum of every temperature data
		high = data    # highest temperature
		low = data     # lowest temperature

		if data < 16:  # evaluate whether the first data input is cold temperature
			cold = 1
		else:
			cold = 0

		while True:
			data = int(input('Next Temperature: (or ' + str(QUIT) + ' to quit)?'))
			if data == QUIT:
				break
			num_data += 1
			total += data
			if data > high:
				high = data
			elif data < low:
				low = data
			if data < 16:
				cold += 1

		avg = total / num_data  # average temperature

		print('Highest temperature = ' + str(high))
		print('Lowest temperature = ' + str(low))
		print('Average = ' + str(avg))
		print(str(cold) + ' cold day(s)')






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
