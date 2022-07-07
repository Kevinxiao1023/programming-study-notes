filenames = ['a_tale_of_two_cities.txt', 'pride_and_prejudice.txt', 'learning_python.txt']

for filename in filenames:
	try:
		with open(filename) as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
		print("\nReading file: "+filename)
		print("The number of'the'appears in the file:")
		print(contents.lower().count('the'))