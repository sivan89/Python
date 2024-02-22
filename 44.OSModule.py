import os
import glob

#print(os.system("ipconfig"))


def chdir():
    print (os.getcwd())
    print() #extra line 
    return 

print("current working dir")
chdir()

os.chdir("..")

print("current working dir")
chdir()


dirc = ("logs")
current = os.getcwd()
print(os.path.join(current,dirc))
create = os.path.join(current,dirc)
os.mkdir(create) # Note : we can run only first time 
os.chdir(create)
print(os.getcwd())
print("dir '" + dirc + "' Cretated" ) # string concodination method 1
os.chdir("..")
os.rmdir(dirc)
print(os.getcwd())
print("dir " "'%s'" " deleted" %dirc) # string concodination method 1

""" a = os.getcwd()
b = "123\\425"
current1 = os.path.join(a,b)

os.makedirs(current1)

os.chdir(current1)
print(current1)

os.chdir("../..") 

os.rmdir(b) """

import os.path as p #making alias during import command

a = "38.regex.py"
print(p.abspath(a)) # absolute path for the file முழுமையான பாதை
os.chdir("Python")
print(p.exists(a)) # present or not( true - present)
print(p.getsize(a))  # get the size

print(os.listdir())


b= "27*.py"
print(glob.glob(b)) # search a fie using glon module 