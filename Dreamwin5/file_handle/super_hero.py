import json
#print(dir(json))
with open("super_heros.json", 'r') as sh:
    data = json.load(sh)
    print(data)
