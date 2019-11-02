import random

# GET GUESS
def get_guess():
	return list(input("What is your guess"))


# GENERATE COMPUTER CODE 124
def generate_code():
	digits = [str(num) for num in range(10)]
	# print(digits)
	# shuffle the digits
	'''
	The shuffle() method takes a sequence (list, string, or tuple) and reorganize the order of the items. Note: This method changes the original list/tuple/string, it does not return a new list/tuple/string.
	'''
	random.shuffle(digits)
	return digits[:3]

def generate_clues(code,user_guess):
	if user_guess == code:
		return "CODE CRACKED!"


	clues = []
	# ind = 0
	for ind, num in enumerate(user_guess):
		if num == code[ind]:
			clues.append("match")
		elif num in code:
			clues.append("Close")

	if clues == []:
		return ["Nope"]
	else:
		return clues
	# ind = ind + 1

# RUN GAME
print("Welcome Code Breaker!")

secret_code = generate_code()

clue_report = []
while clue_report != "CODE CRACKED!":
	guess = get_guess()

	clue_report = generate_clues(guess,secret_code)
	print("here is the result of your guess: ")
	for clue in clue_report:
		print(clue)





