empty_set = set()
print(len(empty_set))

network_list = {123,124,125,126,127,128,129}
print(network_list)

dub_networklist = {111,222,333,444,333,222,111}
print(dub_networklist)
print(len(dub_networklist))

officemixed = {"vim","samba",999,8865}
workfrommixed = {"Smart","kind",-3,56,92}
print("mixed",workfrommixed)
workfrommixed.add(123) #to add new into the set 
workfrommixed.remove(-3) #to remove the string from set
print(len(workfrommixed))
print("after updated :", workfrommixed)
workfrommixed.update(officemixed) #to add new set into old set
print(len(workfrommixed))
print(workfrommixed)

a = {"vim","samba",999,8865}
b = {"samba","kind",-3,56,999}

x = a & b
print(x)

y = a - b
print(y)

z = a | b
print(z)
