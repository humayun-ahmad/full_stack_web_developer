# INHERITANCE

class Animal():

	def __init__(self):
		print("Animal created!")

	def whoAmI(self):
		print("Animal")

	def eat(self):
		print('Eating')


# mya = Animal()
# mya.whoAmI()
# mya.eat()


class Dog(Animal):
	def __init__(self):
		Animal.__init__(self)
		print("Dog Created")


# myd = Dog()
# myd.whoAmI()
# myd.eat()


# SPECIAL METHODS
