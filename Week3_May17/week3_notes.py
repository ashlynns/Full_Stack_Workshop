"classes produce objects of a given type"

class Vehicle: 
	#type = 'Sedan'
	#def __init__(self, production_year, make):
	#	self.production_year = production_year
	#	self.make = make 
	def __init__(self):
		print('Vehicle is ready')
	def who_is_this(self):
		print('Vehicle') 
	def engine_start(self):
		print('starting engine')

#model_3 = Vehicle('2020', 'Tesla')
#model_e = Vehicle('1990', 'Mercedes')

#print(2022-int(model_e.production_year))

"""
Inheritance -- child class can have attributes of parent class Child(Parent)
Encapsulaation 
Polymorphism

functions in a child class will overwrite functions with the same name in the parent
"""
class Truck(Vehicle):
	def __init__(self):
		super().__init__()
		print('Truck is ready')
	def who_is_this(self):
		print('Truck') 
	def offload(self):
		print('truck is offloading')

big_truck = Truck()
big_truck.who_is_this()
big_truck.engine_start()
big_truck.offload()


# Encapsulation Example 
class Computer: 
	def __init__(self):
		self.__maxprice = 900 # two underscores makes the var private. can only change it externally by creating a new method to access
	def sell(self): 
		print('Selling Price: {}'.format(self.__maxprice))
	def setMaxPrice(self, price): # setter method
		self.__maxprice = price

c = Computer()
c.sell()

c.setMaxPrice(1000)
c.sell()

c.__maxprice = 888 # doesnt actually change anything 
c.sell()


# Polymorphism Example 

class Parrot: 
	def fly(self):
		print('Parrot can fly')
	def swim(self):
		print('Parrot cant swim')

class Penguin: 
	def fly(self):
		print('Penguin cant fly')
	def swim(self):
		print('Penguin can swim')

def flying_test(bird):
	bird.fly() # same code can behave differently depending on object type -- polymorphism! 

blu = Parrot()
peggy = Penguin()

flying_test(blu)
flying_test(peggy)