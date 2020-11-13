import calendar
# calendar.weekday() - Will be use to take the day of 2010-01-01
import json

# Read the JSON from the file and convert it into a python list of dictionaries
with open('./import_and_prepare_wwo_hist_data/results.json', 'r') as file:
    file_json = file.read()
original_data = json.loads(file_json)

# Transform original_data into a list all daily reports
daily_data = []
for monthly_report in original_data:
    daily_data.extend(monthly_report['result']['data']['weather'])

csv_separator = ','
csv_headers = ['week', 'sunrise', 'sunset', 'moonrise', 'moonset', 'moon_phase', 'moon_illumination', 'temperature_max', 'temperature_min', 'temperature_average', 'total_snow_cm', 'sun_hour', 'wind_speed_kmph', 'wind_direction_degree', 'precipitation_mm', 'humidity', 'visibility_km', 'pressure', 'cloud_cover', 'heat_index_c', 'dew_point_c', 'wind_chill_c', 'wind_gust_kmph', 'feels_like_c', 'uv_index', 'city']
csv_lines = []

for day in daily_data:
    print(day['date'])
"""
for index in range(3, len(daily_data), 7):
    day = daily_data[index]['date'].split('-')
    print('{} - {}'.format(daily_data[index]['date'], calendar.weekday(int(day[0]), int(day[1]), int(day[2]))))
"""