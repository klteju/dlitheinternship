com1=int(input("enter the sales in com1: "))
com2=int(input("enter the sales in com2: "))
com3=int(input("enter the sales in com3: "))
if com1==com2==com3:
    print("all have same sales")
elif com1>com2 and com1>com3:
    print("com1 sales the highest")
elif com2>com1 and com2>com3:
    print("com2 sales the highest")
else:
    print("com3 sales the highest")