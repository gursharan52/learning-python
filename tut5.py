#Dictionry

D1 = {"guri":"Golgappe" , "Gursharan":"Maggie" , "karan":{"B":"prothe" , "L":"rice" , "D":"roti"}}



D1 ['sach deva'] = 'dosa'
D1 ['dev'] = 'Rajma'
del D1['dev']
print(D1)
print(D1["karan"])
print(D1["karan"]['L'])
D2 = D1.copy()
del D2["Gursharan"]
D2.update({"Leena":"toffee"})
print(D2)
print(D2.keys())
print(D2.items())


d1={"love":"pyaar","hate":"gussa","humaity":"insaaniyat",

"colour":"rang","shop":"dukaan"}

print("what you are searching for?")

print(d1[input()])


