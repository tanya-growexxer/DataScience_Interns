import csv
import json
jsonArray = []
with open(r'/home/growlt198/Desktop/logs.csv', encoding ='utf-8') as csvf:
  csvreader = csv.DictReader(csvf, fieldnames=['Timestamp','status', 'message'])
  for row in csvreader:
    jsonArray.append(row)
with open(r'/home/growlt198/Desktop/json_logs.json', 'w', encoding = 'utf-8') as jsonf:
  js = json.dumps(jsonArray, indent = 4)
  jsonf.write(js)