print("going to compare three numbers which is biggest number")
a = int(input("enter the first number :"))
b = int(input("enter the second number :"))
c = int(input("enter the third numbre :"))

if(a>b):
    if(a>c):
        print("first numbr is biggerst number :",a)
    else:
        print("third number is biggest number :",c)
elif(b>c):
    print("second nnumber is bigget number :",b)
else:
    print("third number is biggest number:",c)
        