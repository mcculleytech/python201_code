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
alice = Hacker("alice", 20, 5)

bob.print_name()
alice.print_name()

print(bob.age)
print(alice.age)

bob.birthday()
alice.birthday()

print(bob.age)
print(alice.age)

print(alice.cves)
# AttributeError
#print(bob.cves)

print(issubclass(Hacker, Person))
print(issubclass(Person, Hacker))

print(isinstance(bob, Person))
print(isinstance(bob, Hacker))

print(isinstance(alice, Person))
print(isinstance(alice, Hacker))