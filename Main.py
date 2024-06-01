from JsonManager import save_directory_structure_to_json
import configparser
import json

save_directory_structure_to_json(".\\modules", "DirInfo.json")
config_files = {}
jsonFile = open("DirInfo.json")

data = json.load(jsonFile)

for i in data['modules']:
    for x in range(len(data['modules'][i]['__files__'])):
        if ".ini" in data['modules'][i]['__files__'][x]:
            config_files = {data['modules'][i]["id-number"] : data['modules'][i]['__files__'][x]}

print(config_files[0])

jsonFile.close()
