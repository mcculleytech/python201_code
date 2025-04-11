def gen_demo():
	n = 1 
	yield n

	n += 1
	yield n

	n += 1
	yield n

test = gen_demo()
print(test)
print(next(test))
print(next(test))
print(next(test))
# This will throw StopIterationError
# print(next(test))

# use loop to iterate over generator
test2 = gen_demo()
for a in test2:
	print(a)

# Can create generator functions with loops
# ie perform xor operation on static key

def xor_static_key(a):
	key = 0x5
	for i in a:
		yield chr(ord(i) ^ key) # returning integer rep of char

for i in xor_static_key("test"):
	print(i)

# Can create anonymous generator expressions in similar way to anonymous lambda functions.
xor_static_key2 = (chr(ord(i) ^ 0x5) for i in "test")

print(xor_static_key2)
print(next(xor_static_key2))
print(next(xor_static_key2))

for i in xor_static_key2:
	print(i)
