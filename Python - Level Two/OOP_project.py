from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

'''
mycards = []
for r in RANKS:
	for s in SUITE:
		mycards.append((s,r))
'''
# same as like above


# mycards = []

class Deck:



	def __init__(self):
		# allcards = []
		print("Creating new ordered Deck!")
		self.allcards = [(s,r) for s in SUITE for r in RANKS ]
		# self.allcards = [(s,r) for s in SUITE for r in RANKS ]
		# for r in RANKS:
		# 	for s in SUITE:
		# 		allcards.append((s,r))
	def shuffle(self):
		print("SHUFFLEING DECK")
		shuffle(self.allcards)

	def split_in_half(self):
		return (self.allcards[:26], self.allcards[26:])

class Hand:

	def __init__(self,cards):
		self.cards = cards

	def __str__(self):
		return "Contains {} cards".format(len(self.cards))

	def add(self,added_cards):
		self.cards.extend(added_cards)

	def remove_card(self):
		return self.cards.pop()


class player:
	def __init__(self,name,hand):
		self.name = name
		self.hand = hand

	def play_card(self):
		drawn_card = self.hand.remove_card()
		print("{} has placed: {}".format(self.name,drawn_card))
		print("\n")
		return drawn_card

	def remove_war_cards(self):
		war_cards = []

		if len(self.hand.cards) < 3:
			return self.hand.cards

		else:

			for x in range(3):
				war_cards.append(self.hand.cards.pop())

			return war_cards
	def still_has_card(self):
		# return true if player still has card left
		return len(self.hand.cards) != 0


# Create new deck and split it in half:
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

# Create both players:
comp = player("computer", Hand(half1))

name = input("what is your name?")
user = player(name,Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_card() and comp.still_has_card():
	total_rounds += 1
	print("Time for a new round!")
	print("here are the current standing")
	print(user.name + "has the count: " + str(len(user.hand.cards)))
	print(comp.name + "has the count: " + str(len(comp.hand.cards)))
	print("play a card!")
	print('\n')

	table_cards = []

	c_card = comp.play_card()
	p_card = user.play_card()

	if c_card[1] == p_card[1]:
		war_count += 1

		print("war!")

		table_cards.extend(user.remove_war_cards())
		table_cards.extend(comp.remove_war_cards())

		if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
			user.hand.add(table_cards)
		else:
			comp.hand.add(table_cards)
	else:
		if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
			user.hand.add(table_cards)
		else:
			comp.hand.add(table_cards)

print("game over, number of rounds: " + str(total_rounds))
print("a war happened " + str(war_count) + " times")











