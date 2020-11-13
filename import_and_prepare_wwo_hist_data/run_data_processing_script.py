import calendar
# calendar.weekday() - Will be use to take the day of 2010-01-01
import json

# Read the JSON from the file and convert it into a python list of dictionaries
with open('./import_and_prepare_wwo_hist_data/results.json', 'r') as file:
    file_json = file.read()
original_data = json.loads(file_json)

csv_separator = ','
csv_headers = ['week', 'sunrise', 'sunset', 'moonrise', 'moonset', 'moon_phase', 'moon_illumination', 'temperature_max', 'temperature_min', 'temperature_average', 'total_snow_cm', 'sun_hour', 'wind_speed_kmph', 'wind_direction_degree', 'precipitation_mm', 'humidity', 'visibility_km', 'pressure', 'cloudcover', 'heat_index_c', 'dew_point_c', 'wind_chill_c', 'wind_gust_kmph', 'feels_like_c', 'uv_index' 'city']
csv_lines = []
