import calendar
# calendar.weekday() - Will be use to take the day of 2010-01-01
import json

# Read the JSON from the file and convert it into a python list of dictionaries
with open('./import_and_prepare_wwo_hist_data/results.json', 'r') as file:
    file_json = file.read()
original_data = json.loads(file_json)
