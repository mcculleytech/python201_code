# Using len to get length of string and list. basic polymorphism
print(len("string"))
print(len(['l','i','s','t']))

class Person:
	'Person base class'
	# class attribute
	wants_to_hack = True

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def print_name(self):
		print("my name is {}".format(self.name))

	def print_age(self):
		print("my age is {}".format(self.age))



	def birthday(self):
		self.age += 1

class Hacker(Person):

	def __init__(self, name, age, cves):
		super().__init__(name, age)
		self.cves = cves

	def print_name(self):
		print("My name is {} and I have {} CVEs".format(self.name, self.cves))

	def total_cves(self):
		return self.cves

bob = Person("bob", 30)
alice = Hacker("Alice", 20, 10)
people = [bob , alice]

for person in people:
	person.print_name()
	print(type(person))

def obj_dump(object):
	object.print_name()
	print(object.age)
	object.birthday()
	print(object.age)
	print(object.__class__)
	print(object.__class__.__name__)

obj_dump(bob)
obj_dump(alice)