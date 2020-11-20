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

# Here, headers are append one by one to make tests and development easier.
# In the end, all kept headers will be in one big array
csv_headers = ['week']
# csv_headers.extend(['sunrise', 'sunset', 'moonrise', 'moonset', 'moon_phase', 'moon_illumination'])
csv_headers.extend(['temperature_max', 'temperature_min', 'temperature_average'])
csv_headers.append('total_snow_cm')
# csv_headers.append('sun_hour')
# csv_headers.extend(['wind_speed_kmph', 'wind_direction_degree'])
# csv_headers.append('precipitation_mm')
# csv_headers.append('humidity')
# csv_headers.append('visibility_km')
# csv_headers.append('pressure')
# csv_headers.append('cloud_cover')
# csv_headers.append('heat_index_c')
# csv_headers.append('dew_point_c')
# csv_headers.extend(['wind_chill_c', 'wind_gust_kmph'])
# csv_headers.append('feels_like_c')
# csv_headers.append('uv_index')
csv_headers.append('city')
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

    csv_line['total_snow_cm'] = sum([float(daily_data[monday_index + week_index]['totalSnow_cm']) for week_index in range(7)])

    # Get the city name without ', France' at the end (which will introduce de bug in the csv)
    csv_line['city'] = original_data[0]['result']['data']['request'][0]['query'].split(',')[0]

    csv_lines.append(csv_line)

# CSV Generation
with open('./data/wwo_hist.csv', 'w') as file:
    file.write(csv_separator.join(csv_headers) + '\n')
    for line in csv_lines[::-1]:
        file.write(
            ','.join(
                [str(value) for value in line.values()]) + '\n')
