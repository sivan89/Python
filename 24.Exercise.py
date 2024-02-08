""" 1. Get a number from user & verify the entered number is a multiple of 3, multiple of 5 and multiple of both 3 & 5.
2. Create a script to get values from user for mathematical calculator based on users input.

Sample Input & Output: 
----------------------
Enter first no: 10
Enter second no: 20
Which operation would you like to perform (1. Addition, 2. Substraction, 3. Multiplication, 4. Division): Addition
The result is : 30 """

""" a = int(input("enter the number:"))
b = a * 3
c = a * 5
print("multi 3 :",b)
print("multi 5 :",c)
d = b * c
print("both 3 and 5 :", d) """


""" e = int(input("enter the first number : "))
f = int(input("enter the second number :"))

print("what action do youwant to perform 1.add and 2.sub and 3.mmul and 4.div ")
g = int(input("type -1- -2- -3- -4- : "))
if(g==1):
    h = e + f
    print(h)
elif(g==2):
    i = e - f
    print(i)
elif(g==3):
    j = e * f
    print(j)
elif(g==4):
    l= e/f
    print(l)
else:
    print("enetr the corrcet number") """
    
    

fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}
basket = frozenset(fruits)

print('Unique elements:', basket)

""" # Add new fruit throws an error!
basket.add("Orange")
print('After adding new element:', basket) """