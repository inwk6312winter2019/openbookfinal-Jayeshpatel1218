file=open("Book1.txt")
def sorted_words(file):
	for line in file:
		line=line.split()
		line.sort()
		print(line)
print(sorted_words(file))
