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


bob = Person("bob", 30)
alice = Person("alice", 20)
mallory = Person("mallory", 50)

print(bob)
print(alice)
print(mallory)

bob.print_name()
alice.print_name()
mallory.print_name()

bob.print_age()
alice.print_age()
mallory.print_age()


bob.birthday()
bob.print_age()

print(bob.name)
print(bob.age)

print(hasattr(bob, "age"))
print(hasattr(bob, "asd"))

print(getattr(bob, "age"))
setattr(bob, "asd", 100)
print(getattr(bob, "asd"))

delattr(bob, "asd")

print(bob.wants_to_hack)
print(alice.wants_to_hack)
print(mallory.wants_to_hack)

Person.wants_to_hack = "No Way!"
print(bob.wants_to_hack)

# can delete classes and still access instaniated classes
#del Person
print(bob.name)

# default attributes that are avialable to every class
print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)

