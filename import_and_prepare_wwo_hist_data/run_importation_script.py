from import_and_prepare_wwo_hist_data.script import get_weather_data_in_a_duration
import json

# Get all the data
duration_results = get_weather_data_in_a_duration('Your WWO API key', 'Essonne', 2010, 2017)

# Write all results into the results.json file
file = open("results.json", 'a')
print('file opened')

file.write('[')
for result in duration_results:
    file.write(json.dumps(result))
    if result != duration_results[-1]:
        file.write(',')
    print('data for {}-{} printed'.format(result['month'], result['year']))
file.write(']')

file.close()
print('file closed')
