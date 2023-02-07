import csv
import json

def read_logs_file(file_path):
    logs = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.split(',')
            logs.append({"timestamp": data[0], "status": data[1], "message": " ".join(data[2:])})
    return logs

def save_logs_to_json(logs, file_path):
  	with open(file_path, 'w') as file:
   		json.dump(logs, file)

logs = read_logs_file('data_file.csv')
save_logs_to_json(logs, 'data_file.json')

