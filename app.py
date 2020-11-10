import pandas
import numpy

datadir = './datas/'
sdis91_filepath = datadir + 'interventions-hebdo-2010-2017.csv'
gripe_filepath = datadir + 'incidence-RDD-3-syndromes-grippaux.csv'
diarrhee_filepath = datadir + 'incidence-RDD-6-syndrome-diarrhee-aigue.csv'
varicelle_filepath = datadir + 'incidence-RDD-7-varicelle.csv'
days_off_filepath = datadir + 'hollidays_and_days_off.csv'


def load_and_filter_incidence_rdd_file(filepath, row_validator):
    """
    Load data from a csv incidence-RDD-... (could function with other CSV but the function is written for this files)
    Filter the got data using the function row_validator

    :param filepath: string -  The path to the file containing the wanted data.
    :param row_validator: function - Function returning a Boolean. It will be used to filter which rows will be kept

    :return: A pandas.DataFrame containing the data of filepath filtered by row_validator
    """
    data = pandas.read_csv(filepath)
    filtered_data = [row[1] for row in data.iterrows() if row_validator(row)]
    return pandas.DataFrame(numpy.array(filtered_data), columns= data.columns)

filter_ile_de_france = lambda row: row[1]['geo_name'] == 'ILE-DE-FRANCE'
gripe_data = load_and_filter_incidence_rdd_file(gripe_filepath, filter_ile_de_france)
diarrhee_data = load_and_filter_incidence_rdd_file(diarrhee_filepath, filter_ile_de_france)
varicelle_data = load_and_filter_incidence_rdd_file(varicelle_filepath, filter_ile_de_france)

# #Temporary output
print(gripe_data)
print(diarrhee_data)
print(varicelle_data)

sdis91_data = pandas.read_csv(sdis91_filepath)
days_off_data = pandas.read_csv(days_off_filepath)