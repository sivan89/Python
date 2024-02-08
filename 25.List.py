
name = []
print(type(name))

name1 = ["smart","stat","BeHappy"]
print(name1)
print(name1[1])
print(len(name1))

#print none 
name2 = [None]   # N should caps
print(name2)

name3 = [None]*5
print(name3)

name1[1] = "star"
print(name1)

name1.append("MakeHappy") #No square bracket 
print("latest :", name1)

new = ["I","LOVE","YOU"]

new1 = new + name1
print("New LISt ",new1)

new += name1
print("concatenates :" ,new)

list_of_network =["net1","net2","net2"]
net = "net2"
if net in list_of_network:
    print("we found the network")
else:
    print("not found")
    
print("first")
for index in range(0,len(list_of_network)):
    print(list_of_network[index])
    
print("Second")
for why in list_of_network:
    print(why)


