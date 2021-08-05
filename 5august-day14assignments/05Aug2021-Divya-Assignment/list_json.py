import json
std_list = [{"name":"Divya","roll_no":9},{"name":"div","roll_no":10}]
#print(json.dumps(std_list))
mydata = json.dumps(std_list)
with open ('test.json','w',encoding='UTF8',newline='') as j:
    j.write(mydata)