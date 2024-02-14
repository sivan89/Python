
""" var = open("thefile.txt","r")
var1 = var.read()
print(var1)
var.close() """

with open("thefile.txt") as var:
    var1 = var.read()
    print(var1)
var.close()