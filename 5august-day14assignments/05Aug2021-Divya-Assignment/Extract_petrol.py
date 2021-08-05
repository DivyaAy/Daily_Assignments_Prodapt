import json
#pt_list = [ ]
# myfile = 'petrol.csv'
f = open('petrol.json')
data = json.load(f)
for i in data:
    if i["rate"]<='70':
        print(i)

    