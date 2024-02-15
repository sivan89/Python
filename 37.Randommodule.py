#random module: 
import random
import math

print(random.randrange(5,10))

# dir() function used to get a list containing all attributes of a module
#print(dir(random))
xyz = dir(random)
for y in xyz:
    print(y)
    
""" a = 20.85
b = 3
c = -28.44
print(math.ceil(a)) #high number
print(math.floor(a)) #low number 
print(math.sqrt(a)) #sq root 2
print(math.factorial(b)) #factorial 3*2*1
print(math.fabs(c)) #if we are getting any negative value changed to positive 
print(math.trunc(c))
print(math.trunc(a)) #eqalient to ceil
print(round(a)) """