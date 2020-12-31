# 1. UTBM - AD50 - Project - Predict firemen's interventions number in Essonne

Authors:

- *Adrien Bouyssou*
- *Vincent Galinier*

N. B. : This document complements the notebooks files and their existing comments and markdown cells.

## 1.1. Summary

- [1. UTBM - AD50 - Project - Predict firemen's interventions number in Essonne](#1-utbm---ad50---project---predict-firemens-interventions-number-in-essonne)
  - [1.1. Summary](#11-summary)
  - [1.2. Subject](#12-subject)
  - [1.3. Weather data clearing](#13-weather-data-clearing)
  - [1.4. Merging the datasets](#14-merging-the-datasets)
  - [1.5. Experimenting with diffenrents prediction models](#15-experimenting-with-differents-prediction-models-)
  - [1.6. Bias and comments about the results](#16-bias-and-comments-about-the-results)

## 1.2. Subject

The goal of this project is to predict the number of firefighters interventions in a specific french department (Essone).

To do so, we will use six differents data tables in the CSV format:

1. The calendar of French holidays and days off
2. A table of influenza statistics in France
3. A table of diarrhoea statistics in France
4. A table of varicella statictics in France
5. Weather data in Onderville-Sur-Essonne
6. The main one, firemen's interventions statistics from 2010 to 2017 in Essonne

To do the predictions and process the datasets, we will use Python and libraries such as Pandas, Scikit-Learn or Keras.

## 1.3. Weather data clearing

After gathering all the datasets, we parsed and filtered them to only keep what we wanted.

The biggest job concerned the weather dataset. Firstly, we fetched/gathered data on the best area possible, on Onderville-Sur-Essonne and on the same date interval as the firemen's interventions data (from 2010 to 2017).  
After that, we created 3 helper scripts in the folder `import_and_prepare_wwo_hist_data`.

The first one, `util.py`, is a tool file containing two functions. The first function returns the number of days of a given month (with the year). The second one gets and returns the weather data, it is a generic function that can call the API for the wanted location and on the given datetime interval. We can specify the returned format and the frequency of the datetime too.  
We needed to this function because the WWO API can not return data on an interval bigger than a month. So we used this function to automate the imports. Otherwise, we would had to do sixteen API call manually.  

The second file, `run_importation_script.py`, use the previous file to import all weather data between 2010 and 2017 and transform it into a JSON file called `results.json`. This file will be completed thanks to the second function, `get_missing_februaries`. The reason is because I (Adrien Bouyssou) introduced a bug in the util function that gives the number of days, in the leap year detection.

The consequence of this is that we had missing days in our datasets. The `get_missing_februaries` function solves this problem.

Finally, we made a last script to filter the data. It was a big part too. The main reason is that the biggest frequency we have is a daily report. But others CSVs are weekly. So, we have to made that the daily reports have to be parsed into weekly reports. And the method will change following the kind of data and the corresponding information. For example, we will take the average of the temperature (min and max too) but we will do the sum of the daily precipitations.  
We exported the result into a new CSV called wwo_hist.csv.

## 1.4. Merging the datasets

After gathering all the necessary datasets from different data sources, it was necessary to find a way to put them all together in a coherent way to form one big dataset / DataFrame. This merging process is done within the `src/merge_datasets.ipynb` notebook.

What we basically do in this notebook is the following :
  - we go through the datasets, and for each of them:
    - we get rid of the non-useful attributes/columns
    - we find a way to get a yearweek (complying with ISO8601's definition of yearweek) value for each row using existing date-related attributes
  - we merge all all the datasets using the `yearweek` attribute.
  - we drop duplicates
  - we save the merged dataset as a .CSV file (`merged_data.csv`) in the src directory.

For further details about how each dataset is handled, you can refer to the notebook,its comments and its markdown notes.

## 1.5. Experimenting with differents prediction models

Now that the datasets are merged together, we can "feed" it to some models that could be able to predict one of the following features :
- ACCI
- AUTR
- INCN
- INCU
- SUAP
- **ope_total** (the sum of all the previous attributes)

This is a **regression problem** as we want to predict a discrete value that usually ranges from 1160 to 3763 (for `ope_total`).

We experimented with different models and techniques:
### - RandomForestRegressor
For earch target features (the different operation counts listed before), we preprocessed the data using a Stardard Scaler and fed it to sklearn's RandomForestRegressor.

This model is quite fast and gives relatively good results.

On the ope_total feature prediciton, the Mean Absolute Error is usually around 100.

### - Manually tuned MLP with Keras' Sequential Model

For earch target features, we preprocessed the data using a Standard Scaler and a Normalizer and fed it to a sequential model composed of 4 Dense layers using ReLU activation.

The predictions weren't better than with the RandomForestRegressor.

### - Building multiple models and sum their predictions

We trained models to predict ACCI, AUTR, INCN, INCU and SUAP, then summed up their predictions to obtain a prediciton of ope_total.

This approach didn't gave really good results compared to the others.

### - Automatically tuned MLP with AutoKeras

Finally, we returned to the "Keras + MLP" approach but while using AutoKeras this time. When using a MLP, fiding the good amount of layers and fine tuning their parameters can be hard. AutoKeras is a Python library performing Automated Machine Learning. It provides a way to automatically find top performing models and some of the best hyper-parameters that pairs with these models.

After running a model search with AutoKeras, it returns a keras model we can use for predictions.

The predictions of this model were really good on the training data, sometimes reaching a Mean Absolute Error of 80 when predicting ope_total. On the other hand, the predicitons on the validation data weren't that accurate (MAE=130).
The model outputed by AutoKeras gives better predicitons than the model we manually tuned ourselves.

## 1.6. Bias and comments about the results

Datasets are not always concerning the Essone departement only. In one hand, some are on a city scale and on the other hand, some cover an entire region. It is not a big problem but it introduces a bias in our predictions.

We could also argue about the fact that the predictions would be more accurate with more data and more attributes.

**More data :**  
We used data from 2010 to 2017 and, at the rate of one line for each week passed, our merged dataset only contains 416 rows. For some simple predictions problems, this amount of rows would be enough, but when the problem is a harder one, a model sometimes need multiple thousand of rows to be able to do good predictions. In our case, there is not any obvious and useful correlation between attributes, and more rows could help the precision of the predicitons.

**More attributes :**  
Does weather, the incidence rate of three medical conditions and vacation periods are enough to predict firefighters interventions ? It is a good start, but there is probably more than that. Elements unrelated to these attributes could also influence greatly the intervention count ... not to mention the part of randomness.


**Using days instead of weeks:**
Specific days can have an impact 
suicides 
flooding rivers
particular days (new year, national day)


shouldn't have dropped weeknumber, but how to encode it ?