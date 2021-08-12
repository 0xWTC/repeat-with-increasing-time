import random
import time

def repeater(function, *args, retries = 10, initial_timeout = 1, double_exponential = False, debug = False):
	"""This is an exponential time repeater"""
	count = 0
	if double_exponential == True:
		exponential = 2
	else:
		exponential = 1 
	while True:
		try:
			return function(*args)
		except:
			sleep = (initial_timeout * 2 ** count ** exponential)
			if debug == True:
				print(f"Function raised an exception. Sleeping for {sleep} seconds...")
			if count + 1 == retries:
				raise Exception(f"Hit retry limit of {retries} retries on a repeater for: {function}")
			time.sleep(sleep)
			count += 1

if __name__ == "__main__":
	def function_that_usually_fails():
		result = random.randrange(0, 10)
		if result > 8:
			print(f"Result: {result}. Result is satisfying, no need to repeat.")
			return result
		else:
			print(f"Result: {result}. Result isn't satisfying. Repeating...")
			raise Exception 
	repeater(function_that_usually_fails, retries = 10, initial_timeout = 1, double_exponential = False, debug = True)