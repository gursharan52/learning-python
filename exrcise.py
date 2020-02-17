# Exercise
N1 = int(input("Enter your First digit"))
N2 = int(input("Enter your Second digit"))
Opr = (input("Choose your operater{+,-,*,/}"))

if Opr == "+" :
    if N1 == 56 or N2 == 9:
        print(" Your answer is 77")
    else:
        print("Your answer is " , N1 + N2 )

elif Opr == "*":
    if N1 == 45 or N2 == 3:
        print("your answer is 555")
    else:
        print("Ypur answer is " , N1 * N2 )

elif Opr == "/" :
    if N1 == 56 or N2 == 4 :
        print("your answer is 4")
    else:
        print("Your answer is " , N1 / N2 )

elif Opr == "-" :
    print("your answer is " , N1 - N2 )