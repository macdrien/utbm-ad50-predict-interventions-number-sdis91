# Script to download and prepare data from World Weather Online

This package contains functions to get data from the World Weather Online API and prepare them for future processes.  
The API only allows GET methods on a month, not more. From that fact, we automatised a process to get data on a larger duration and print the result into a JSON file called result.json

The script.py contains multiple functions:

- get_number_of_days: take two number in argument, a year and a month. Return the number of days of the given month
- get_weather_data_in_a_duration: Return an array containing objects. One object describe, for a month, all weather data recieved.
