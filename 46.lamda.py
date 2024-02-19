j=11
for i in range(1,j):
    print(i, end=" ")
print()
x = range(1,11)
res = [print(i,end=" ") for i in x]
print()

print("###############################################")

#function
def dube(num):
    num = num * num * num
    return num

print(dube(3))

#Lambda Function 
num2 = lambda num1: num1 * num1 * num1
print(num2(3))

print("###############################################")

#MAX
print(max(12,17))

#Lambda Function 
abc = lambda a,b: a if a > b else b
print(abc(12,17))

print("###############################################")


numbers = [50, 35, 22, 87, 54, 62, 17, 25, 73, 60]
for i in numbers:
    if (i%2 == 0):
        print(i)
""" t = []
t.append(i)
print(t) """
                 
print("###############################################")

xyz = [50, 35, 22, 87, 54, 62, 17, 25, 73, 60]


def numbers(i):
    if (i%2 == 0):
        return i

x = filter(numbers, xyz)
y = list(x)

print(y)


div = list(filter(lambda d: (d % 2 == 0 ), xyz))
print(div)

print("###############################################")


