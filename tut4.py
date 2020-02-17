grocery = ['maggie' , 'oil' , 'shampoo' , ' bhindi' , 'potato']
print(grocery)
num = ['2' , '56' , '27' , '9' , '37']
# ask to ajay for why sort function take 9 as a first digit
num.sort()
# if i comment the reverse function than no.9 show at last digit why?
num.reverse()
print(num)
print(num[3])
print(num[0:3])
num.append('3')
num.insert(2,54)
num.remove('27')
num.pop()
print(num)


#tupple are never change
num2 = ('1','2','3')
print('tupple =', num2)