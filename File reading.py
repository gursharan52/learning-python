# File Writting

i = open('Guri.txt','rt')
content = i.read()
print(content)


i.close()


f = open('Guri.txt','rt')

for line in f :
	print(line, end= ' ')

f.close()

