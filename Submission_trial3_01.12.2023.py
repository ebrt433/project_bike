import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
import numpy as np
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import TimeSeriesSplit
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor




## + Weather data
# Load training and testing datasets & remove unnecessary cols
train_data = pd.read_parquet("../input/mdsb-2023/train.parquet")
test_data = pd.read_parquet("../input/mdsb-2023/test.parquet")
final_test_data =pd.read_parquet("../input/mdsb-2023/final_test.parquet")

#combining test data + train data and reassigning to use our old variables in order to change our code minimally
train_data = combined_train_test = pd.concat([train_data, test_data])
test_data = final_test_data

train_data.drop(columns=['counter_name', 'site_name','counter_id', 'counter_installation_date', 'counter_technical_id', 'site_id'], inplace=True)
test_data.drop(columns=['counter_name', 'site_name','counter_id', 'counter_installation_date', 'counter_technical_id', 'site_id'], inplace=True)

#Load weather dataset and remove irrelevant columns
weather_data = pd.read_csv("hourly-weather-data.csv")
weather_data = weather_data.drop(columns=['name', 'dew', 'precipprob', 'preciptype','uvindex','icon','stations', 'sealevelpressure', 'winddir', 'conditions', 'sealevelpressure', 'severerisk', 'solarradiation', 'solarenergy'])

# convert to datetime to merge them properly
train_data['date'] = pd.to_datetime(train_data['date'])
test_data['date'] = pd.to_datetime(test_data['date'])
weather_data['datetime'] = pd.to_datetime(weather_data['datetime'])

#merge with weather data
merged_train_data = pd.merge(train_data, weather_data, left_on='date', right_on='datetime', how='inner')
merged_test_data = pd.merge(test_data, weather_data, left_on='date', right_on='datetime', how='inner')
merged_train_data = merged_train_data.drop(columns=['datetime'])
merged_test_data = merged_test_data.drop(columns=['datetime'])


## School Holidays + Weather data
# import the holiday dataset
schoolholiday_data = pd.read_csv("../input/external-data/fr-calendrier.csv", delimiter=';')
schoolholiday_data = schoolholiday_data[schoolholiday_data['zones'] == 'Zone C'] # Zone C is Paris
schoolholiday_data = schoolholiday_data.drop(columns=['description','location','annee_scolaire', 'zones'])

# Convert the date strings to datetime objects
schoolholiday_data['start_date'] = pd.to_datetime(schoolholiday_data['start_date'], utc=True).dt.date
schoolholiday_data['end_date'] = pd.to_datetime(schoolholiday_data['end_date'],utc=True).dt.date

# Generate a set of unique dates for each range in a row
unique_dates = set()
for _, row in schoolholiday_data.iterrows():
    unique_dates.update(pd.date_range(start=row['start_date'], end=row['end_date']))

# Convert the set back to a list and create a DataFrame
unique_dates_list = sorted(list(unique_dates)) 
schoolholiday_data = pd.DataFrame({'Date': unique_dates_list})

# merge with rest of the data
merged_train = pd.merge(merged_train_data, schoolholiday_data, left_on='date', right_on='Date', how='left')
merged_train['Date'] = merged_train['Date'].apply(lambda x: 0 if pd.isna(x) else 1)
merged_train.rename(columns={'Date': 'is_school_holiday'}, inplace=True)

merged_test = pd.merge(merged_test_data, schoolholiday_data, left_on='date', right_on='Date', how='left')
merged_test['Date'] = merged_test['Date'].apply(lambda x: 0 if pd.isna(x) else 1)
merged_test.rename(columns={'Date': 'is_school_holiday'}, inplace=True)


## School Holidays + Weather data + strike data
# import the strike dataset
from datetime import datetime  # Import the datetime class from the datetime module

# strike dates for public transport in Paris, retrieved from: https://www.cestlagreve.fr/calendrier/?lieu=74&secteur=14&mois=1&annee=2022
strike_dates = {'Date': [datetime(2020, 9, 17), datetime(2020, 12, 14), datetime(2020, 12, 16),
                        datetime(2021, 1, 21), datetime(2021, 2, 4), datetime(2021, 2, 15),
                        datetime(2021, 5, 21), datetime(2021, 6, 1), datetime(2021, 10, 5),
                        datetime(2021, 11, 17)]}

strike_data = pd.DataFrame(strike_dates)
strike_data

# Convert the date strings to datetime objects
strike_data['Date'] = pd.to_datetime(strike_data['Date'])


# merge with rest of the data
merged_train = pd.merge(merged_train, strike_data, left_on='date', right_on='Date', how='left')
merged_train['Date'] = merged_train['Date'].apply(lambda x: 0 if pd.isna(x) else 1)
merged_train.rename(columns={'Date': 'is_strike'}, inplace=True)

merged_test = pd.merge(merged_test, strike_data, left_on='date', right_on='Date', how='left')
merged_test['Date'] = merged_test['Date'].apply(lambda x: 0 if pd.isna(x) else 1)
merged_test.rename(columns={'Date': 'is_strike'}, inplace=True)
merged_test.head()


## School Holidays + Weather data + Strike data + Lockdown data
lockdown_data = pd.read_csv("../input/external-data/lockdown-data.csv")
lockdown_data['datetime'] = pd.to_datetime(lockdown_data['datetime'])
merged_train['date'] = pd.to_datetime(merged_train['date'])
merged_test['date'] = pd.to_datetime(merged_test['date'])

merged_train = pd.merge(merged_train, lockdown_data, left_on='date', right_on='datetime', how='left')
merged_train = merged_train.drop(columns=['datetime'])
merged_test = pd.merge(merged_test, lockdown_data, left_on='date', right_on='datetime', how='left')
merged_test = merged_test.drop(columns=['datetime'])

# Extract the hour features from the datetime column
merged_train['hour'] = merged_train['date'].dt.hour
merged_test['hour'] = merged_test['date'].dt.hour

## Encode the dates
def _encode_dates(X):
    X = X.copy()  # modify a copy of X
    X['date'] = pd.to_datetime(X['date'])
    X.loc[:, "year"] = X["date"].dt.year
    X.loc[:, "month"] = X["date"].dt.month
    X.loc[:, "day"] = X["date"].dt.day
    X.loc[:, "weekday"] = X["date"].dt.weekday
    return X.drop(columns=["date"])

merged_train = _encode_dates(merged_train)
merged_test = _encode_dates(merged_test)

# define x and y
X_merged_train = merged_train.drop(columns=['bike_count', 'log_bike_count'])
Y_merged_train = merged_train['log_bike_count']

# dropping any remaining Nan Values
merged_train=merged_train.dropna()


# Define your features sets for XGBoost and LSTM
features_xgb = ['latitude', 'longitude', 'temp', 'feelslike', 'humidity', 
                'precip', 'snow', 'snowdepth', 'windgust', 'windspeed', 'cloudcover', 
                'visibility', 'is_school_holiday', 'is_strike', 'full_lockdown', 
                'partial_lockdown', 'school_closures', 'business_closures', 
                'hour', 'year', 'month', 'day', 'weekday']

# Target variable
target = 'log_bike_count'

# Splitting the data for XGBoost
X_xgb = merged_train[features_xgb]
y_xgb = merged_train[target]

#splitting the data for test XGBoost
X_xgb_test = merged_test[features_xgb]


# Step 1: Creating the Pipeline
# Include any necessary preprocessing steps here
pipeline = Pipeline([ 
    ('xgb', XGBRegressor(objective='reg:squarederror'))
])

# Step 2: Fitting the Model
pipeline.fit(X_xgb, y_xgb)

# Step 3: Making Predictions
y_pred_xgb = pipeline.predict(X_xgb_test)

# Step 4: Preparing the Submission File
results = pd.DataFrame({
    'Id': np.arange(y_pred_xgb.shape[0]),
    'log_bike_count': y_pred_xgb
})

results.to_csv("submission.csv", index=False)