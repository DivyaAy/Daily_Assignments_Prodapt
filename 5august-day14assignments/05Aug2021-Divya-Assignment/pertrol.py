import csv,json
myfile = 'petrol.csv'
jsonfile = 'petrol.json'
pet_list = []
# list = [ ]
with open (myfile,'r',encoding='UTF8',newline='') as p:
    dataReader = csv.DictReader(p)
    for data in dataReader:
        pet_list.append(data)

list_json = json.dumps(pet_list)
with open (jsonfile,'w',encoding='UTF8') as j:
     j.write(list_json)

f = open('petrol.json')
data = json.load(f)
for i in data:
    if i["rate"]<='70':
        print(i)

