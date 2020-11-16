from import_and_prepare_wwo_hist_data.script import get_weather_data_in_a_duration
import json

def original_script():
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


def get_missing_februaries():
    # Get all missing months
    februaries = []
    for year in range(2010, 2018):
        februaries.append(get_weather_data_in_a_duration('c8a647919e5f482393481545201311', 'Essonne', year, year, 2, 2))

    with open('./import_and_prepare_wwo_hist_data/results.json', 'r') as file:
        file_json = file.read()
    result_file = json.loads(file_json)

    for index in range(7):
        result_file[12 * index + 1] = februaries[index][0]

    with open("./import_and_prepare_wwo_hist_data/results.json", 'w') as file:
        file.write('[')
        for result in result_file:
            file.write(json.dumps(result))
            if result != result_file[-1]:
                file.write(',')
            print('data for {}-{} printed'.format(result['month'], result['year']))
        file.write(']')
