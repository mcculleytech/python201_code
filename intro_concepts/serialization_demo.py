import pickle

hackers = {"neut": 1, "geohot": 100, "neo": 1000}

for key, value in hackers.items():
	print(key, value)

# Binary serialization
serialized = pickle.dumps(hackers)
print(serialized)

# deserialzation
hackers_2 = pickle.loads(serialized)
print(hackers_2)

for key, value in hackers_2.items():
	print(key, value)

# Write serialized data to file
# with open("hackers.pickle", "wb")as handle:
#	pickle.dump(hackers, handle)

# loaded the serialized data and deserialzed it.
with open("hackers.pickle", "rb") as handle:
	hackers_3 = pickle.load(handle)

print(hackers_3)
