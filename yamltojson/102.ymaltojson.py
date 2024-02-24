import os
import json
import yaml

os.chdir("D:\DevOps\Python\Python\yamltojson")

yamlfile = "Services.yaml"
jsonfile = "Services.json"

with open(yamlfile,'r') as ym:
    readrm = yaml.safe_load(ym)

with open(jsonfile,'w') as js:
    writejs = json.dump(readrm,js,indent=2)