filename=open("Book2.txt")
def process_file(filename):
	hist = dict()
	for line in filename:
		most_common(hist)
	return hist
def most_common(hist):
	t = []
	for key, value in hist.items():
		t.append((value, key))
		t.sort(reverse=True)
	return t

hist = process_file('Book2.txt')
