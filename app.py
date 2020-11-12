import pandas
import numpy

datadir = './datas/'
sdis91_filepath = datadir + 'interventions-hebdo-2010-2017.csv'
gripe_filepath = datadir + 'incidence-RDD-3-syndromes-grippaux.csv'
diarrhee_filepath = datadir + 'incidence-RDD-6-syndrome-diarrhee-aigue.csv'
varicelle_filepath = datadir + 'incidence-RDD-7-varicelle.csv'
days_off_filepath = datadir + 'hollidays_and_days_off.csv'


def load_and_filter_csv(filepath, row_validator, separator=','):
    """
    Load data from a csv
    Filter the got data using the function row_validator

    :param filepath: string -  The path to the file containing the wanted data.
    :param row_validator: function - Function returning a Boolean. It will be used to filter which rows will be kept
    :param separator: str - The separator between each element

    :return: A pandas.DataFrame containing the data of filepath filtered by row_validator
    """
    data = pandas.read_csv(filepath, sep=separator, skip_blank_lines=True).dropna()
    columns = data.columns

    if row_validator is not None:
        data = [row[1] for row in data.iterrows() if row_validator(row)]
        data = pandas.DataFrame(numpy.array(data), columns=columns)

    return data


sdis91_data = load_and_filter_csv(sdis91_filepath, None, separator=';')

# #Temporary output
print(sdis91_data)

filter_rdd_files = lambda row: row[1]['geo_name'] == 'ILE-DE-FRANCE' and\
                               201001 <= row[1]['week'] <= 201752
gripe_data = load_and_filter_csv(gripe_filepath, filter_rdd_files)
diarrhee_data = load_and_filter_csv(diarrhee_filepath, filter_rdd_files)
varicelle_data = load_and_filter_csv(varicelle_filepath, filter_rdd_files)

# #Temporary output
print(gripe_data)
print(diarrhee_data)
print(varicelle_data)

days_off_data = load_and_filter_csv(days_off_filepath,
                                    lambda row:'2010-01-01' <= row[1]['date'] <= '2017-12-12')

# #Temporary output
print(days_off_data)