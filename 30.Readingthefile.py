
xyz = open("thefile.txt","r")


""" print("first second method")
print(xyz.read()) """

#this will help to read the fles 
""" print("read method")
abc = xyz.read()
print(abc)  """

#spilt the file 
""" print("split method")
print(abc.split()[2]) """

#readlines function
""" print("readlines method")
print(xyz.readlines())
xyz.close() """
#print in list format then we can use for loop get the value one by one 


#get the values from the list file
""" for y in xyz.readlines():
    print("line by line : ",y , end="")
xyz.close() """

#if i want to read first 2 list 
""" for y in xyz.readlines()[0:2]:
    print(y,end="")
xyz.close() """

#readline funtion
""" line1 = xyz.readline()
print(line1)
line2 = xyz.readline()
print(line2)
line3 = xyz.readline()
print(line3) """


#Iterating a file by reading the content line by line
""" for y in xyz:
    if(y == "server2\n"):
        print("welcom this is servver two")
    else:
        print("1.",y,end="")
xyz.close() """


for y in xyz:
    if(y.replace("\n","") != "server4"):
        print(y,end="")
    else:
        print("Now we are server four")
xyz.close()