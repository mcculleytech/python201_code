# recap of nested functions.
def print_out(a):
	print("Outer: {}".format(a))

	def print_in():
		print("\tInner: {}".format(a))

	return print_in

test2 = print_out("test")

del print_out

test2()

# spits error since print_out was deleted.
print(print_out("test2"))