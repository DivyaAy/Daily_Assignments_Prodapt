import csv,json
myfile = 'diesel.csv'
jsonfile = 'diesel.json'
des_list = []

with open (myfile,'r',encoding='UTF8',newline='') as d:
    dataReader = csv.reader(d)
    for data in dataReader:
        des_list.append(data)

list_json = json.dumps(des_list)
with open (jsonfile,'w',encoding='UTF8') as j:
     j.write(list_json)