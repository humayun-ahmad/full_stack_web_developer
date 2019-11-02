class Dog():

	# class object attribute
	species = "mamal"
	def __init__(self, one,two):
		self.one = one
		self.two = two

# below two line are same 
# mydog = Dog("lab","lab2")
mydog = Dog(one = "lab", two = "lab2")

print(mydog.one)
print(mydog.two)
print(mydog.species)

















