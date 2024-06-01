from JsonManager import save_directory_structure_to_json
import configparser
import json

save_directory_structure_to_json(".\\modules", "DirInfo.json")
config_files = {}
main_files = {}
jsonFile = open("DirInfo.json")
config = configparser.ConfigParser()

data = json.load(jsonFile)

for i in data['modules']:
    for x in range(len(data['modules'][i]['__files__'])):
        if ".ini" in data['modules'][i]['__files__'][x]:
            config_files[data['modules'][i]["id-number"]] = data['modules'][i]['__files__'][x]
        if "main.py" in data["modules"][i]["__files__"][x]:
            main_files[data['modules'][i]["id-number"]] = data['modules'][i]['__files__'][x]


for i in range(len(config_files)):
    config.read(config_files[i])
    print(config[])

jsonFile.close()
