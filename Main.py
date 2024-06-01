from JsonManager import save_directory_structure_to_json
import configparser
import json

save_directory_structure_to_json(".\\modules" "DirInfo.json")

jsonFile = open("DirInfo.json")

data = json.load(jsonFile)
