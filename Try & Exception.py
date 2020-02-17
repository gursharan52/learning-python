# Try & Exception
print('Enter 1st no.')
num1 = input()
print('Enter 2nd no.')
num2 = input()
try:
	print('The sum of your 1st & 2nd no. is ',
		  int(num1) + int(num2))
	print('Good man :)')

except Exception as e:
	print(e)
	print('Good try best of luck for next time :)')
	



