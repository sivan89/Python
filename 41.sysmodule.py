import sys

""" print(sys.version) #Version of python
print(sys.platform) #platform
print(sys.path) #path for all python lib
print(sys.modules) #list all the module """

""" for x in sys.stdin:
    if (x.strip() == 'q'):
        break
    else:
        print(f"input from u : {x}")
print("Exit") """

name = sys.stdin.readline()
sys.stdout.write(name)
sys.stderr.write("Error Occured!")

""" servername = sys.stdin.readline()
if servername == "Server01":
	sys.exit("Invalid Server!")
	print("The entered value is:", servername)
else:
	print("The entered value is:",servername)
	print("To Be Continued..") """
