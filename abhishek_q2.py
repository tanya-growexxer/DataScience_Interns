import json

logs_file_loc = './logs'

with open(logs_file_loc, 'r') as fp:
    logs_data = fp.readlines()

log_dict = {}
for entry in logs_data:
    entry = entry[:-1]
    entry = (entry.split(','))
    id_ = int(entry[0].split(' ')[-1])
    timestamp = ' '.join(entry[0].split(' ')[:-1])
    status = entry[1]
    message = entry[-1]
    log_dict[id_] = {'timestamp':timestamp,
                    'status':status,
                    'message':message}

with open('logs.json', 'w') as fp:
    json.dump(log_dict, fp)