class Circle():

	pi = 3.14

	def __init__(self,radius):
		self.radius = radius

	def  area(self):
		return self.radius * self.radius * Circle.pi
	def set_radius(self,new_r):
		self.radius = new_r

# Circle parameter is the radius value
obj = Circle(3)

# set the new value of radius
obj.set_radius(4)

print(obj.area())