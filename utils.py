import pandas
import numpy


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