a=int(input("Enter the number1: "))
b=int(input("Enter the number2: "))
c=a
print("assigning a to c",c)
if(a==c):
    print("a and c are equal")
a+=b   
print ("unary operation of a and b with addition", a)
a-=b   
print ("unary operation of a and b with substraction", a)
a*=b   
print ("unary operation of a and b with multiplication", a)
a/=b   
print ("unary operation of a and b with division", a)
print(a==c)