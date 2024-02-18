#function call
""" def printwhat():
    print("Hello All Good to hear")

printwhat()


def addtwo(a,b):
    sum = a + b
    print(sum)
    
c=5
d=6
addtwo(c,d) """


""" def num2and3(type,num):
    if (type=="S"):
        result = num * num
    elif(type=="C"):
        result = num * num * num
    return result

print(num2and3("C",2))
print(num2and3("S",3)) """



def square(num):
    return num * num

""" for i in [1,2,3]:
    print(square(i)) """
    

n = int(input())
for j in range(1,n+1):
    print(square(j))