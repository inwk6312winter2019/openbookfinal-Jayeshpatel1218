file1=open("Book1.txt")
file2=open("Book2.txt")
file3=open("Book3.txt")
def unique_words(file):
	l=[]
	for line in file:
		line=line.split()
		if line not in l:
			l.append(line)
	return l
print(unique_words(file1))
