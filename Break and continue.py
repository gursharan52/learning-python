'''
var = 0

while(True):
    if var+1<5:
        var = var + 1
        continue

    print(var + 1, end=' ')
    if var == 44:
        break
    var = var + 1
'''




while(True):
	digit = int(input('Enter your digit \n'))
	if  digit > 100:
		print('Congratulations you Entered a digit greater than 100')
		break
	else:
		print('Try again\n')
		continue

