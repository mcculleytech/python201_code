class Person:
	'Person base class'
	# class attribute
	wants_to_hack = True

	def __init__(self, name, age):
		self.name = name
		self.__age = age

	def get_age(self):
		return self.__age

	def set_age(self, age):
		self.__age = age

	def print_name(self):
		print("my name is {}".format(self.name))

	def print_age(self):
		print("my age is {}".format(self.age))

	def birthday(self):
		self.__age += 1

bob = Person("age", 30)
# throws an attribute error since the age attribute has been encapsulated.
#print(bob.age)
print(bob.get_age())
bob.set_age(33)
print(bob.get_age())
bob.birthday()
print(bob.get_age())

print(bob.__dict__)
bob._Person__age = 50
print(bob.get_age())