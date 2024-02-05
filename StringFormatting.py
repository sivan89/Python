Output = "Running {} out of {} Servers"
print(Output.format(3,10))

Output = "Running {} out of {} Servers"
Output1 = (Output.format(3,10))
print(Output1)

Serverinfo = "Server Name {name} ; IP Address {IP} ; Port Number {port}"
print(Serverinfo.format(name="www.google.com",IP="8.8.8.8",port="80"))