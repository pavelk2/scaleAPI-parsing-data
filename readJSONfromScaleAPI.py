import json
import csv
from collections import namedtuple

SETTINGS = {
    "input_file" : 'IMAGE_MODERATION_POC_SCALE.json',
    "output_file": 'IMAGE_MODERATION_POC_SCALE.csv',
    "fields": ["TASK_ID","IMAGE_ID","STATUS"]
}

print

with open(SETTINGS['input_file'], 'r') as f:
    tasks_dict = json.load(f)
i = 0

# It would be great to have executor ID

data = []
for task in tasks_dict:
    units_all = task['params']['categories'];
    units_approved = task['response']['category'];

    for unit in units_all:
        i+=1

        status = ""
        if unit in units_approved:
            status = "APPROVED"
        else:
            status = "NOT APPROVED"

        data_unit = {
            SETTINGS["fields"][0] : task["task_id"],
            SETTINGS["fields"][1] : unit[14:-1],
            SETTINGS["fields"][2]: status
        }
        data.append(data_unit)
        print(data_unit)
f.close()

f = open(SETTINGS['output_file'], "w")
writer = csv.DictWriter(f, fieldnames=SETTINGS["fields"])
writer.writeheader()
writer.writerows(data)
f.close()
