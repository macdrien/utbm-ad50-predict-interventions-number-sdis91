# 1. UTBM - AD50 - Project - Predict firemen's interventions number in Essonne

Authors:

- *Adrien Bouyssou*
- *Vincent Galinier*

## 1.1. Summary

- [1. UTBM - AD50 - Project - Predict firemen's interventions number in Essonne](#1-utbm---ad50---project---predict-firemens-interventions-number-in-essonne)
  - [1.1. Summary](#11-summary)
  - [1.2. Subject](#12-subject)
  - [1.3. Bias](#13-bias)
  - [1.4. Weather data clearing](#14-weather-data-clearing)
  - [Merging the datasets](#merging-the-datasets)

## 1.2. Subject

The aim of this project is to predict the number of firefighters interventions in a specific french department (Essone).

To do so, we will use six differents data tables in the CSV format:

1. The calendar of French holidays and days off
2. A table of influenza statistics in France
3. A table of diarrhoea statistics in France
4. A table of varicella statictics in France
5. Weather data in Onderville-Sur-Essonne
6. The main one, firemen's interventions statistics from 2010 to 2017 in Essonne


To do the predictions and process the datasets, we will use Python and libraries such as Pandas, Scikit-Learn or Keras.

## 1.3. Bias

Datasets are not always concerning the Essone departement only. In one hand, some are on a city scale and on the other hand, some cover an entire region. It is not a big problem but it introduces a bias in our predictions.

TODO : on n'a aussi pas tellement de données en fin de compte : seulement 7 ans sur un seul département. En comparaison pour faire des prédicitons météo on a à notre disposition des centaines d'années de données qui concernent le monde entier

## 1.4. Weather data clearing

After gathering all the datasets, we have to implement a pre-process to keep only what we want and parse all in the same format to be able to use it.

The big parsing was the weather's CSV one. Firstly, we got data on the best area possible, on Onderville-Sur-Essonne and on the same date interval as the firemen's interventions data (from 2010 to 2017).  
After that, we created 3 files in the folder `import_and_prepare_wwo_hist_data`.

The first one, `util.py`, is a tool file. It contains two functions. The first function return the number of days of the given month (with the year). The second one get and return the weather data. It is a generic function which can call the API for the wanted location and on the given datetime interval. We can specify the returned format and the frequency of the datetime too.  
We needed to this function because the WWO API can not return data on an interval bigger than a month. So we used this function to automize the imports. Otherwise, we had to do sixteen API call manually.  

The second file, `run_importation_script.py`, use the previous file to import all weather data between 2010 and 2017 and transform it into a JSON file called `results.json`. This file will be completed thanks to the second function, `get_missing_februaries`. The reason is because I (Adrien Bouyssou) introduced a bug in the util function that gives the number of days, in the leap year detection.

The consequence of this is that we had missing days in our datasets. The `get_missing_februaries` function solves this problem.

Lastly, we made a last script to run the preprocess and keep the data we want. It was a big part too. The main reason is that the biggest frequency we have is a daily report. But others CSVs are weekly. So, we have to made that the daily reports have to be parsed into weekly reports. And the method will change following the kind of data and the corresponding information. For example, we will take the average of the temperature (min and max too) but we will do the sum of the daily precipitations.  
We exported the result into a new CSV called wwo_hist.csv.

## Merging the datasets

After gathering all the necessary datasets from different data sources, it was necessary to find a way to put them all together in coherent way to form one big dataset / DataFrame. This merging process is done within the `src/merge_datasets.ipynb` notebook.

## Experimenting with diffenrents prediction models (?)

We can now "feed" the merged dataset to some models (...)


