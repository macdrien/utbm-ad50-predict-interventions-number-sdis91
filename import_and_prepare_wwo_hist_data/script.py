import requests


def get_number_of_days(year, month):
    """
    :param year: int: The year of the month to take.
    :param month: int: The month to take
    :return: The number of days in the given month
    """
    number_of_days = 31
    if month in [4, 6, 9, 11]:
        number_of_days = 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 == 0) or year % 400 == 0:
            number_of_days = 28
        else:
            number_of_days = 29
    return number_of_days

def get_weather_data_in_a_duration(api_key, location, start_year, end_year, start_month=1, end_month=12, frequency=24, return_format='json'):
    """
    Get all the weather data from World Weather Online between two years and return the data in a table containing objects which describe a month.
    It is possible to not take all months from the first and the last year by setting up start_month and end_month.

    World Weather Online allows us to get data in different intervals of hours. By default, the method take one report for each day (24h). But WWO accepts 1, 3, 6 or 12 hours.
    WWO can return the data in two different formats: JSON and XML. By default, the asked format is JSON, but return_format accepts 'XML' too.

    Finally, this method does not provide an API key. You have to give yours in the first argument 'api_key'.

    :param api_key: str: The WWO API key to use for the requests.
    :param location: str: The place from which the weather data will be asked.
    :param start_year: int: The starting year of the interval of date to take.
    :param end_year: int: The ending year of the interval of date to take.
    :param start_month: int <Optional - default 1>: The starting month of the first year to take the weather information. It has to be in the interval [1, 12].
    :param end_month: int <Optional - default 12>: The ending month of the last year to take the weather information. It has to be in the interval [1, 12].
    :param frequency: int <Optional - default 24>: The interval, in hour, between two reports. It has to be in the set of intervals {1, 3, 6, 12, 24} .
    :param return_format: str <Optional - default 'json'>: The wanted data format for the result. It can be only 'json' or 'xml'.

    :return: A list of reports (dictionary). Each report is structured as following: {'year': year_of_report, 'month': month_of_report, 'result': 'The report in the asked format'}
    """
    if api_key is None:
        print('[ERROR] The get_weather_data_in_a_duration needs an api_key to get the credentials')
        return None

    if location is None:
        print('[ERROR] The get_weather_data_in_a_duration needs a location to target')
        return None

    url = 'https://api.worldweatheronline.com/premium/v1/past-weather.ashx'

    results = []

    for year in range(start_year, end_year + 1):
        for month in range(start_month, end_month + 1):

            number_of_days = get_number_of_days(year, month)
            params = {
                'q': location,
                'date': '{}-{}-{}'.format(year, month, '01'),
                'enddate': '{}-{}-{}'.format(year, month, number_of_days),
                'tp' : frequency,
                'format': return_format,
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
