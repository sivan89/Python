print("***********************************************")

import psutil

print(psutil.cpu_count())
print(psutil.disk_usage("D:"))

import shutil

#print(shutil.disk_usage("D:"))

total, used, free = shutil.disk_usage("D:")

print("Total: %d GB" % (total // (2**30)))
print("Used: %d GB" % (used // (2**30)))
print("Free: %d GB" % (free // (2**30)))

print("***********************************************")