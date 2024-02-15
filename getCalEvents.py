import os
import json

rootdir = os.getcwd()

class Calendar:
    def __init__(self, name, description, location, start, end, timezone):
        self.name = name
        self.description = description
        self.location = location
        self.start = start
        self.end = end
        self.timezone = timezone

events = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files: 
        filepath = subdir + os.sep + file
        if filepath.endswith("r.json"):
            splitFile = filepath.split("\\")
            localFilePath = f".\\{(splitFile[len(splitFile)-2])}\\{(splitFile[len(splitFile)-1])}"

            with open(localFilePath) as file:
                cjdata = json.load(file)
                for item in cjdata:
                    name = item['name']
                    description = item['description']
                    location = item['location']
                    start = item['start_at']
                    end = ['end_at']
                    timezone = ['timezone']
                    events.append(Calendar(name, description, location, start, end, timezone))
            
count = 1
for event in events:
    print(f"Event {count}:")
    count += 1
    print(event.name)
    print(event.description)
    print(event.location)
    print(event.start)
    print(event.end)
    print(event.timezone)
