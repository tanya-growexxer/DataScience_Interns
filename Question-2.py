import csv 
import json 
#Defining a function for conversion
def csv_to_json(csvF, jsonF):
    #Taking a list jsonArray
    jsonArray = []
      
    #Opening csv file 
    with open(csvF, encoding='utf-8') as csvf: 
        #Reading the csv file using DictReader to read csv file as dictionary
        csvReader = csv.DictReader(csvf) 

        for row in csvReader: 
     
            jsonArray.append(row)
  
    #Dumping all of the data in jsonArray list to jsonfile
    with open(jsonF, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvF = 'logs.csv'
jsonF= 'output.json'
csv_to_json(csvF, jsonF)