import os
import json
import yaml

os.chdir("D:\DevOps\Python\Python\JSontoyml")
         
filejson = "Services.json"
fileymal = "Services.yaml"

with open(filejson,'r') as jo:
    jsondata = json.load(jo)

with open(fileymal,"w") as ym:
        yaml.dump(jsondata,ym)

