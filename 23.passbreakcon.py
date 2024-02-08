'''
#Pass
number = 10
count = 0
while (count <= number):
    if(count%2 == 0):
        pass
    else:
        print(count)
    count += 1



for server in "server01","server02","server03":
    for user in "user01","user02":
        if(server == "server02"):
            pass
            print("Add User "+ user + " for " + server)
          

#Break
for i in range(3):
    for j in range(5):
        if j == 2:
            break
            print(j)  # when j==2 this won't run becaues we are using break condition
        else:
            print(j)
        print("print i and j",i,j)



for server in "server01","server02","server03":
    for user in "user01","user02":
        if(server == "server02"):
            break
        print("Add User "+ user + " for " + server)
        


for server in "server01","server02","server03":
    for user in "user01","user02":
        if(server == "server02"):
            continue
        print("Add User "+ user + " for " + server)
        
'''

#Break
for i in range(3):
    for j in range(5):
        if j == 2:
            continue
            print(j)  # when j==2 this will skip the statement becaues we are using continue condition
        else:
            print(j)
        print("print i and j",i,j)