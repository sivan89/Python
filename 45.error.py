""" #Syntax Error
if(a==10) """

#Exceptions
#5 * (1/0)
#(total * 3)
#print(120 - input("Enter the utilized size:"))

""" while True:
    try:
        x =  int(input("enter the value"))
        break
    except Exception:
        print("ERROR : enter the number", Exception.args )
print("the number is ", x) """

""" import sys
for x in sys.argv[1:]:
    try:
        fo = open(x,"r")
    except OSError:
        print("file is no present")
    else:
        print(len(fo.readlines())) #we are open the file eachline comming under string
        fo.close()
    finally:
        print("File Operation Completed!") """
        
""" try:
    raise Exception("Server1","Server2")
except Exception:
    print(type(Exception))
    print(Exception.args)
    i,j = Exception.args
    print(i) """

""" try:
    raise Exception("Server1","Server2")
except Exception as Ex:
    print(type(Ex))
    
try:
    raise NameError("Server5","Server6")
except NameError as NE:  #if we want to use the list of variable in Exception/NameError need to "as" keyword for calling that variable
    print(type(NE))      #the exception type
    print(NE.args)       #arguments stored in .args
    x,y = NE.args
    print(x)
    print(NE.args[0])
    print(y)
    print(NE.args[1]) """
    
""" def div(x,y):
    try:
        result = x // y
        return result
    except ZeroDivisionError:
        print("type correct number")
        return None

print(div(7,2))
print(div(5,0))
print(div(8,2)) """


""" v=""
def div(x,y):
    try:
        if (y != 0 ):
            result = x // y
            return result
        else:
            print("ERROR MESSAGE: type correct number")
    except TypeError:
        print("ERROR MESSAGE:type ONLY number")

print(div(7,2))
print(div(5,0))
print(div(8,v))
print(div(8,2)) """

""" a = [1, 2, 3]
try:
	print ("Second element = %d" %(a[1]))
	print ("Fourth element = %d" %(a[3]))
except:
	print ("An error occurred") """
 

def divide(x, y):
	try:
		result = x // y
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero")
	else:
		print("The division value is :", result)
	finally:
		print('This is always executed!')

divide(5, 2)
divide(5, 0)
divide(8,2)