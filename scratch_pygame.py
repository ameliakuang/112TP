import json

# some JSON:
x = '{ "name":[1,2]}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["name"])

