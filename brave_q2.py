import csv
import json

with open ("/home/growlt195/Desktop/brave.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    data = {"datalist" : []}
    
    for row in reader:
        data["datalist"].append({"timestap":row[0],"status":row[1],"message":row[2]})
        
with open("brave.json","w") as f:
    json.dump(data,f,indent=4)