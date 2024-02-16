import datetime

a = datetime.datetime.now()
print(a)

b = datetime.date.today()
print(b)


#Date object to represent a date
d = datetime.date(2023,12,1)
print(d)

#print(dir(datetime))

#we are getting datetime module and import the class called date module means we are going use only data
#Import Only date Class
from datetime import date 
# Date object to represent a date
e = date(2023,12,1)
print(e)



#today - method "cube symbol"---> we have call with `()``
#year - properties "setting symbol"  --> just name
#first we have call the method then called today then we have to use properties after that like below 

g = date.today()

h = g.year
i = g.month
j = g.day
print (g,h,j,i)

#display the class from the module 
print(dir(datetime))

#print the method and properties from the module.class 
print(dir(datetime.time))

#help(datetime)


#we are getting datetime module and import to submodule called time module 
from datetime import time 

f = time(15,59,30)
print(f)

c = datetime.time()
print(c)



from datetime import datetime 

xyz = datetime.now()

print(xyz.strftime("%H:%M:%S"))
print(xyz.strftime("%Y:%m:%d"))
print(xyz.strftime("%d:%m:%Y"))