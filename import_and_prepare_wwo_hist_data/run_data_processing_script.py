import calendar
# calendar.weekday() - Will be use to take the day of 2010-01-01
import json
from datetime import date

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

for monday_index in range(3, len(daily_data), 7):
    monday = daily_data[monday_index]
    csv_line = {}

    # Set the week
    current_date = monday['date'].split('-')
    week_number = date(int(current_date[0]), int(current_date[1]), int(current_date[2])).isocalendar()[1]
    csv_line['week'] = '{}{}'.format(current_date[0], week_number if week_number >= 10 else '0{}'.format(week_number))

    # Get temperature min, max and average
    csv_line['temperature_max'] = max([int(daily_data[monday_index + week_index]['maxtempC']) for week_index in range(7)])
    csv_line['temperature_min'] = min([int(daily_data[monday_index + week_index]['mintempC']) for week_index in range(7)])
    csv_line['temperature_average'] = round(sum([int(daily_data[monday_index + week_index]['avgtempC']) for week_index in range(7)]) / 7, 2)

    csv_line['city'] = original_data[0]['result']['data']['request'][0]['query']

    csv_lines.append(csv_line)

for line in csv_lines:
    print(line)