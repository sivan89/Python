import datetime

a = datetime.datetime.now()
print(a)

b = datetime.date.today()
c = datetime.time()
print(b)
print(c)

#Date object to represent a date
d = datetime.date(2023,12,1)
print(d)

#print(dir(datetime))

#we are getting datetime module and import to submodule called date module 
from datetime import date 

e = date(2023,12,1)
print(e)

#we are getting datetime module and import to submodule called time module 
from datetime import time 

f = time(15,59,30)
print(f)