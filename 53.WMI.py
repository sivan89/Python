import wmi

# For Local Connection
c = wmi.WMI()

""" For Remote Connection
c = wmi.WMI("12.18.128.123", user = "admin", password = "pass@123") """

""" print(c.classes)
print(c.Win32_Service())
print(wmi.WMI().Win32_Service.methods.keys())
print(c.Win32_Service.methods.keys())
print(c.Win32_Service.properties.keys())  

for s in c.Win32_Service():
    print(s.Name,"-",s.State,"-",s.Status) #Name/state- propertiy  """
    
print(c.Win32_LogicalDisk.properties.keys())

for disk in c.Win32_LogicalDisk():
    print("Disk details",disk.DeviceID)
    print("-" * 25)
    print(f"FileSystem Type: {disk.FileSystem}")
    print(f"Size : %d GB" % (int(disk.Size) / (2**30)))
    print(f"FreeSpace : %d GB" % (int(disk.FreeSpace) / (2**30)))
    print("-" * 25)