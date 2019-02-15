file=open("Book3.txt")
def character_word_count(file):
	d=dict()
	for line in file:
		for word in line:
			if word not in d:
				d[line] = 1
			else:
				d[line] += 1
	return d
print(character_word_count(file))
