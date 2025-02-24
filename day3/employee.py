month1=int(input("enter the sales in month1: "))
month2=int(input("enter the sales in month2: "))
month3=int(input("enter the sales in month3: "))
total_sales=month1+month2+month3
if total_sales>=90000:
    print("the person can continue")
elif total_sales>=70000:
    print("person is in average range so he can continue")
else:
    print("the person is not eligible to continue")

