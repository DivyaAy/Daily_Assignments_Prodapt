import csv,json
myfile = 'C:/Users/divya.km/Desktop/preparation_coding/DAY13_TASK/Students.csv'
jsonfile = 'students.json'
list = []

with open (myfile,'r',encoding='UTF8',newline='') as f:
    dataReader = csv.reader(f)
    for data in dataReader:
        list.append(data)

list_json = json.dumps(list)
with open (jsonfile,'w',encoding='UTF8') as j:
     j.write(list_json)