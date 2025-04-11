# addition vs concat
print(1 + 1)
print("1" + "1")

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

	# operator overloading
	def __str__(self):
		return "my name is {} and I am {} years old".format(self.name, self.age)

	def __add__(self, other):
		return self.age + other.age

	def __lt__(self, other):
		return self.age < other.age


bob = Person("bob", 30)
alice = Person("alice", 20)

print(bob)
print(alice)
# without overload it doesn't know how to handle the following addition
print(bob + alice)
print(bob < alice)