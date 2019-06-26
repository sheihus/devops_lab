#!/usr/bin/env python

import json
import yaml
import sys
import os
import subprocess

print(sys.version)

print()
print("The Python version is %s.%s.%s" % sys.version_info[:3])

myCmd = 'which python'
os.system(myCmd)

myCmd = 'which pip'
os.system(myCmd)

print()
subprocess.run(["which", "python"])

# 7
print()
# result = subprocess.run(['pip', 'list'], stdout=subprocess.PIPE)
# result.stdout.decode('utf-8')


# result=subprocess.run(['ls', '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8')
res = subprocess.run(['pip', 'list'], stdout=subprocess.PIPE).stdout.decode('utf-8')
res = res.split("\n")
result = {}
for i in res:
    j = i.split()
    if len(j) > 1:
        result[j[0]] = j[1]
#        result.append((j[0], j[1]))
print(result)

# json
with open("data_file.json", "w") as write_file:
    write_file.write(json.dumps(result))
#    json.dump(result, write_file)


# yaml
with open('sw_templates.yaml', 'w') as f:
    yaml.dump(res, f, default_flow_style=False)
