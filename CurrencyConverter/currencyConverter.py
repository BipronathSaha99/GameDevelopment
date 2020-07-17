# >>-----------CurrencyConverter-------------------<<


#To open currency list from text file .
with open("currency.txt") as file:
    lines=file.readlines()
    
#to collect all information create a dictionary
currencyDic={}
for line in lines:
    bipro=line.split("\t")
    currencyDic[bipro[0]]=bipro[1]
    

amount=int(input("Enter your amouunt="))
print("Enter your currency name that you want. Available optiions are:")
[print(i) for i in currencyDic.keys()]
currency=input("Enter the currency name =")
print(f"{amount} BDT = {amount*float(currencyDic[bipro[0]]):0.5f} {currency}")
