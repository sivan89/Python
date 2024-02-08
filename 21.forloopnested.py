'''
for i in range(1,6):
    for j in range (i):
        print("*", end=" ")
    print("")
'''

for server in ("server1","server2","server3"):
    for user in ("user1","user2","user3"):
        print("user added : " + user + "for : " + server )