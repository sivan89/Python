sample_dic = {1: "Hello", 2: "Welcome" , 3: "to" , 4: "My" , 5: "world"}
print(len(sample_dic))
print("Dic:", sample_dic)

print(sample_dic[1])   #Access Dict. with keys

sample_dic[6] = "NewValue" #Add new key-value pair
print(sample_dic) 

sample_dic[6] = "Number-6" #Changing the value of key
print(sample_dic) 

del sample_dic[6] #Deleting the key-value
print(sample_dic) 

print(sample_dic.items()) #Print All the value Key: value 

for key,value in (sample_dic.items()):
    print(key , ":" , value)
    
print(sample_dic.keys()) #To extract dictionary keys 

print(sample_dic.values()) #To extract dictionary values

for a,b in (sample_dic.items()):
    print(a)
    print(b)