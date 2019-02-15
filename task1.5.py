file=open("Book2.txt")
def starts_with_vow(file):
	t=("a", "e", "i", "o", "u")
	count=0
	for line in file:
		for word in line:
			if word[0] in t:
				count=count+1
	return count
print(starts_with_vow(file))
