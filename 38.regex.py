import re

""" a = input("enter th ename : ")
if (re.search(a,"love") != None ): #a-variable love-we we want to search 
    print ("we found")
else:
    print("not found") """
    
# r in front of the search pattern indicates 'raw string' where the special characters are treated as normal characters.
""" b = "Manikandan\nRajendran"
c = r"Manikanadn\nRajendran"
print(b)
print(c)

d = "\\shared\\date\\file.txt"
e = r"\\shared\\date\\file.txt"
print(d)
print(e) """

#sub is used for find and replace 
""" f = "my contant for edit my name : MAnikandan"
g = re.sub(r"MAnikandan",r"Rajendran",f)
print(f)
print(g) """

#patten match in search fuction and uinng `.`
""" h = "SmartStar"
if(re.search(r"tS.ar",h) != None):
    print("patten found")
    print(h)
else:
    print("not found")
    print(h) """

#patten match in search fuction and uinng `\d` - digit for finding intgerer 
#if(re.search(r"N\d0","N20") != None):
"""     print("Pattern found")
else:
    print("Pattern not found")  """ 


""" i = "192.168.198.3" """
#if(re.search(r"19\d.",i) != None):
"""     print("patten found")
else:
    print("NOt found") """
    
#"*" Used to match zero or more occurrences of previous character
#if(re.search(r"N\d0*","N2qwe34") != None): 
"""     print("Pattern found")
else:
    print("Pattern not found")  """
    

#if(re.search(r"N\d0+","N2000") != None): 
"""     print("Pattern found")
else:
    print("Pattern not found")  """
    

#if(re.search(r"N{3}0?+","4525NNN02as") != None): 
"""     print("Pattern found")
else:
    print("Pattern not found")  """
    
    
#if(re.search(r"Y[2-5]N0?+","452Y5N0NN14502as") != None): 
"""     print("Pattern found")
else:
    print("Pattern not found")  """
    
#if(re.search(r"^Y\d0.4$","Y10t4") != None): 
"""     print("Pattern found")
else:
    print("Pattern not found")  """
    

#if(re.search(r"\w","$OKay") != None): 
"""     print("Pattern found")
else:
    print("Pattern not found") """ 
    


#if(re.search(r"..Neo\s","!$Neo polean") != None): 
"""     print("Pattern found")
else:
    print("Pattern not found")  """
    

#if(re.search(r"Neo|polean\s","polean ") != None): 
"""     print("Pattern found")
else:
    print("Pattern not found")  """
    
print(re.search(r"N\d","['N1','N3','Neo']").group())
print(re.search(r"N\d","['N1','N3','Neo']"))
print(re.findall(r"N\d","['N1','N3','Neo']"))
pattern = re.compile(r"N\d")
print(re.findall(pattern,"['N1','N3','Neo']"))