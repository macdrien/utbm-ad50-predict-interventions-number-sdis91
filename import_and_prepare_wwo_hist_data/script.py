import requests
import json

global_api_key = 'YOUR_WWO_KEY'
global_location = 'Essonne'
global_start_year = 2010
global_end_year = 2017
global_start_month = 1
global_end_month = 12


def get_number_of_days(year, month):
    number_of_days = 31
    if month in [4, 6, 9, 11]:
        number_of_days = 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 == 0) or year % 400 == 0:
            number_of_days = 28
        else:
            number_of_days = 29
    return number_of_days

def get_weather_data_in_a_duration(api_key, location, start_year, end_year, start_month=1, end_month=12, frequency=24, format='json'):
    if api_key is None:
        print('[ERROR] The get_weather_data_in_a_duration needs an api_key to get the credentials')
        return None

    if location is None:
        print('[ERROR] The get_weather_data_in_a_duration needs a location to target')
        return None

    url = 'https://api.worldweatheronline.com/premium/v1/past-weather.ashx'
    # ?q=Essonne&date=2010-01-01&enddate=2017-12-31&tp=24&format=json&key=YOUR_WWO_KEY

    results = []

    for year in range(start_year, end_year + 1):
        for month in range(start_month, end_month + 1):

            number_of_days = get_number_of_days(year, month)
            params = {
                'q': location,
                'date': '{}-{}-{}'.format(year, month, '01'),
                'enddate': '{}-{}-{}'.format(year, month, number_of_days),
                'tp' : frequency,
                'format': format,
                'key': api_key
            }

            print('[INF] Request for {}-{}'.format(month, year))

            month_result = requests.get(url, params=params)

            if month_result.status_code == 200:
                print('[INF] Result 200 - OK')
                results.append({'year': year, 'month': month, 'result': month_result.json()})
                print(results[-1])
            else:
                print('[ERR] Request failed for {}-{}'.format(month, year))

    return results


duration_results = get_weather_data_in_a_duration(global_api_key, global_location, global_start_year, global_end_year)

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
