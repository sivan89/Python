import sys

xyz = sys.argv
abc = len(sys.argv)

print("total number of augument passed :", xyz)
print("total number of length :", abc)

print("file name is :", sys.argv[0])

for v in range(1,abc):
    print("Argument",v,sys.argv[v])
    

Sum = 0
for i in range(1,abc):
    Sum += int(sys.argv[i])
print(Sum)