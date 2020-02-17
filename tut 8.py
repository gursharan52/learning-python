# Loops


# FOR Loops
List = ['Harry','marie','carry','jerry','larry']

for item in List:
    print(item)

List2 = ('Harry','marie','carry','jerry','larry')

for item in List2:
    print(item)

List3 = [['Harry','2'],['marry','5'],['larry','10'],['jerry','15']]

for item in List3:
    print(item)


List3 = [['Harry','2'],['marry','5'],['larry','10'],['jerry','15']]

for item, Lollypop in List3:
    print(item ,'eat ',Lollypop,' Lollypop daily .'  )

Dict = {'Harrry':1, 'Larry':3, 'Marry':5, 'Jerry':7 }

for item, Lollypop in Dict.items():
    print(item, 'eat ', Lollypop, ' Lollypop daily .')

List3 = [['Harry',2],['marry',5],['larry',10],['jerry',15]]

for item, Lollypop in List3:
    if Lollypop and str(Lollypop).isnumeric() > 6:
        print(item ,'eat ' ,Lollypop ,'Lollypop Daily')

    elif Lollypop < 6:
        print(item ,'sorry you eat Lollypop but less than 6 ',
              item, ' = ', Lollypop)
