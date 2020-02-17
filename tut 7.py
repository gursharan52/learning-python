# if elif else statement
var1 = 72
var2 = 85
var3 = int(input())

if var3 > var2 :
    print("Greater")
elif var3 == var2 :
    print("Equal")
else:
    print("Lesser")


list = [1,4,7,9]
if 4 in list:
    print("Yes its in list")
else:
    print("No its not in List")


print("What is your Age?")
Age = int(input())

if Age > 18:
    print("You can drive")
elif Age == 18:
    print("We can't decide so you have to come in my office")
else:
    print("We don't allow to you for driving")