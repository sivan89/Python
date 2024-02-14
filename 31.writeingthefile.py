variable1 = open("writefile.txt","r")
#print(variable1.read())
variable2 = variable1.read()
print("before")
print(variable2)
variable1.close()

variable3 = open("writefile.txt","w")
variable4 = variable3.write("server1\n")
variable5 = variable3.write("server5\n")
variable3.close()

variable6 = open("writefile.txt","r")
variable7 = variable6.read()
print("after")
print(variable7)
variable6.close()

variable3 = open("writefile1.txt","a")