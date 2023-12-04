{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2a23590b",
   "metadata": {},
   "source": [
    "# MAP 536 - Python for Data Science - Predicting Cyclist Traffic in Paris"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bd3b93a3",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: '../input/mdsb-2023/train.parquet'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m/Users/elisebarattini/Documents/1_UNIVERSITY/1.3_Masters/DSB/Courses/1_Semester/Python_DS/Project/project_bike/Barattini_Zidi_submission_01 copy.ipynb Cell 3\u001b[0m line \u001b[0;36m2\n\u001b[1;32m     <a href='vscode-notebook-cell:/Users/elisebarattini/Documents/1_UNIVERSITY/1.3_Masters/DSB/Courses/1_Semester/Python_DS/Project/project_bike/Barattini_Zidi_submission_01%20copy.ipynb#W2sZmlsZQ%3D%3D?line=16'>17</a>\u001b[0m \u001b[39mfrom\u001b[39;00m \u001b[39msklearn\u001b[39;00m\u001b[39m.\u001b[39;00m\u001b[39mmodel_selection\u001b[39;00m \u001b[39mimport\u001b[39;00m TimeSeriesSplit\n\u001b[1;32m     <a href='vscode-notebook-cell:/Users/elisebarattini/Documents/1_UNIVERSITY/1.3_Masters/DSB/Courses/1_Semester/Python_DS/Project/project_bike/Barattini_Zidi_submission_01%20copy.ipynb#W2sZmlsZQ%3D%3D?line=18'>19</a>\u001b[0m \u001b[39m# %% [code]\u001b[39;00m\n\u001b[1;32m     <a href='vscode-notebook-cell:/Users/elisebarattini/Documents/1_UNIVERSITY/1.3_Masters/DSB/Courses/1_Semester/Python_DS/Project/project_bike/Barattini_Zidi_submission_01%20copy.ipynb#W2sZmlsZQ%3D%3D?line=19'>20</a>\u001b[0m \u001b[39m## + Weather data\u001b[39;00m\n\u001b[1;32m     <a href='vscode-notebook-cell:/Users/elisebarattini/Documents/1_UNIVERSITY/1.3_Masters/DSB/Courses/1_Semester/Python_DS/Project/project_bike/Barattini_Zidi_submission_01%20copy.ipynb#W2sZmlsZQ%3D%3D?line=20'>21</a>\u001b[0m \u001b[39m# Load training and testing datasets & remove unnecessary cols\u001b[39;00m\n\u001b[0;32m---> <a href='vscode-notebook-cell:/Users/elisebarattini/Documents/1_UNIVERSITY/1.3_Masters/DSB/Courses/1_Semester/Python_DS/Project/project_bike/Barattini_Zidi_submission_01%20copy.ipynb#W2sZmlsZQ%3D%3D?line=21'>22</a>\u001b[0m train_data \u001b[39m=\u001b[39m pd\u001b[39m.\u001b[39;49mread_parquet(\u001b[39m\"\u001b[39;49m\u001b[39m../input/mdsb-2023/train.parquet\u001b[39;49m\u001b[39m\"\u001b[39;49m)\n\u001b[1;32m     <a href='vscode-notebook-cell:/Users/elisebarattini/Documents/1_UNIVERSITY/1.3_Masters/DSB/Courses/1_Semester/Python_DS/Project/project_bike/Barattini_Zidi_submission_01%20copy.ipynb#W2sZmlsZQ%3D%3D?line=22'>23</a>\u001b[0m test_data \u001b[39m=\u001b[39m pd\u001b[39m.\u001b[39mread_parquet(\u001b[39m\"\u001b[39m\u001b[39m../input/mdsb-2023/final_test.parquet\u001b[39m\u001b[39m\"\u001b[39m)\n\u001b[1;32m     <a href='vscode-notebook-cell:/Users/elisebarattini/Documents/1_UNIVERSITY/1.3_Masters/DSB/Courses/1_Semester/Python_DS/Project/project_bike/Barattini_Zidi_submission_01%20copy.ipynb#W2sZmlsZQ%3D%3D?line=23'>24</a>\u001b[0m train_data\u001b[39m.\u001b[39mdrop(columns\u001b[39m=\u001b[39m[\u001b[39m'\u001b[39m\u001b[39mcounter_name\u001b[39m\u001b[39m'\u001b[39m, \u001b[39m'\u001b[39m\u001b[39msite_name\u001b[39m\u001b[39m'\u001b[39m,\u001b[39m'\u001b[39m\u001b[39mcounter_id\u001b[39m\u001b[39m'\u001b[39m, \u001b[39m'\u001b[39m\u001b[39mcounter_installation_date\u001b[39m\u001b[39m'\u001b[39m, \u001b[39m'\u001b[39m\u001b[39mcounter_technical_id\u001b[39m\u001b[39m'\u001b[39m, \u001b[39m'\u001b[39m\u001b[39msite_id\u001b[39m\u001b[39m'\u001b[39m], inplace\u001b[39m=\u001b[39m\u001b[39mTrue\u001b[39;00m)\n",
      "File \u001b[0;32m/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pandas/io/parquet.py:670\u001b[0m, in \u001b[0;36mread_parquet\u001b[0;34m(path, engine, columns, storage_options, use_nullable_dtypes, dtype_backend, filesystem, filters, **kwargs)\u001b[0m\n\u001b[1;32m    667\u001b[0m     use_nullable_dtypes \u001b[39m=\u001b[39m \u001b[39mFalse\u001b[39;00m\n\u001b[1;32m    668\u001b[0m check_dtype_backend(dtype_backend)\n\u001b[0;32m--> 670\u001b[0m \u001b[39mreturn\u001b[39;00m impl\u001b[39m.\u001b[39;49mread(\n\u001b[1;32m    671\u001b[0m     path,\n\u001b[1;32m    672\u001b[0m     columns\u001b[39m=\u001b[39;49mcolumns,\n\u001b[1;32m    673\u001b[0m     filters\u001b[39m=\u001b[39;49mfilters,\n\u001b[1;32m    674\u001b[0m     storage_options\u001b[39m=\u001b[39;49mstorage_options,\n\u001b[1;32m    675\u001b[0m     use_nullable_dtypes\u001b[39m=\u001b[39;49muse_nullable_dtypes,\n\u001b[1;32m    676\u001b[0m     dtype_backend\u001b[39m=\u001b[39;49mdtype_backend,\n\u001b[1;32m    677\u001b[0m     filesystem\u001b[39m=\u001b[39;49mfilesystem,\n\u001b[1;32m    678\u001b[0m     \u001b[39m*\u001b[39;49m\u001b[39m*\u001b[39;49mkwargs,\n\u001b[1;32m    679\u001b[0m )\n",
      "File \u001b[0;32m/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pandas/io/parquet.py:265\u001b[0m, in \u001b[0;36mPyArrowImpl.read\u001b[0;34m(self, path, columns, filters, use_nullable_dtypes, dtype_backend, storage_options, filesystem, **kwargs)\u001b[0m\n\u001b[1;32m    262\u001b[0m \u001b[39mif\u001b[39;00m manager \u001b[39m==\u001b[39m \u001b[39m\"\u001b[39m\u001b[39marray\u001b[39m\u001b[39m\"\u001b[39m:\n\u001b[1;32m    263\u001b[0m     to_pandas_kwargs[\u001b[39m\"\u001b[39m\u001b[39msplit_blocks\u001b[39m\u001b[39m\"\u001b[39m] \u001b[39m=\u001b[39m \u001b[39mTrue\u001b[39;00m  \u001b[39m# type: ignore[assignment]\u001b[39;00m\n\u001b[0;32m--> 265\u001b[0m path_or_handle, handles, filesystem \u001b[39m=\u001b[39m _get_path_or_handle(\n\u001b[1;32m    266\u001b[0m     path,\n\u001b[1;32m    267\u001b[0m     filesystem,\n\u001b[1;32m    268\u001b[0m     storage_options\u001b[39m=\u001b[39;49mstorage_options,\n\u001b[1;32m    269\u001b[0m     mode\u001b[39m=\u001b[39;49m\u001b[39m\"\u001b[39;49m\u001b[39mrb\u001b[39;49m\u001b[39m\"\u001b[39;49m,\n\u001b[1;32m    270\u001b[0m )\n\u001b[1;32m    271\u001b[0m \u001b[39mtry\u001b[39;00m:\n\u001b[1;32m    272\u001b[0m     pa_table \u001b[39m=\u001b[39m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mapi\u001b[39m.\u001b[39mparquet\u001b[39m.\u001b[39mread_table(\n\u001b[1;32m    273\u001b[0m         path_or_handle,\n\u001b[1;32m    274\u001b[0m         columns\u001b[39m=\u001b[39mcolumns,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    277\u001b[0m         \u001b[39m*\u001b[39m\u001b[39m*\u001b[39mkwargs,\n\u001b[1;32m    278\u001b[0m     )\n",
      "File \u001b[0;32m/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pandas/io/parquet.py:139\u001b[0m, in \u001b[0;36m_get_path_or_handle\u001b[0;34m(path, fs, storage_options, mode, is_dir)\u001b[0m\n\u001b[1;32m    129\u001b[0m handles \u001b[39m=\u001b[39m \u001b[39mNone\u001b[39;00m\n\u001b[1;32m    130\u001b[0m \u001b[39mif\u001b[39;00m (\n\u001b[1;32m    131\u001b[0m     \u001b[39mnot\u001b[39;00m fs\n\u001b[1;32m    132\u001b[0m     \u001b[39mand\u001b[39;00m \u001b[39mnot\u001b[39;00m is_dir\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    137\u001b[0m     \u001b[39m# fsspec resources can also point to directories\u001b[39;00m\n\u001b[1;32m    138\u001b[0m     \u001b[39m# this branch is used for example when reading from non-fsspec URLs\u001b[39;00m\n\u001b[0;32m--> 139\u001b[0m     handles \u001b[39m=\u001b[39m get_handle(\n\u001b[1;32m    140\u001b[0m         path_or_handle, mode, is_text\u001b[39m=\u001b[39;49m\u001b[39mFalse\u001b[39;49;00m, storage_options\u001b[39m=\u001b[39;49mstorage_options\n\u001b[1;32m    141\u001b[0m     )\n\u001b[1;32m    142\u001b[0m     fs \u001b[39m=\u001b[39m \u001b[39mNone\u001b[39;00m\n\u001b[1;32m    143\u001b[0m     path_or_handle \u001b[39m=\u001b[39m handles\u001b[39m.\u001b[39mhandle\n",
      "File \u001b[0;32m/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pandas/io/common.py:872\u001b[0m, in \u001b[0;36mget_handle\u001b[0;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[1;32m    863\u001b[0m         handle \u001b[39m=\u001b[39m \u001b[39mopen\u001b[39m(\n\u001b[1;32m    864\u001b[0m             handle,\n\u001b[1;32m    865\u001b[0m             ioargs\u001b[39m.\u001b[39mmode,\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    868\u001b[0m             newline\u001b[39m=\u001b[39m\u001b[39m\"\u001b[39m\u001b[39m\"\u001b[39m,\n\u001b[1;32m    869\u001b[0m         )\n\u001b[1;32m    870\u001b[0m     \u001b[39melse\u001b[39;00m:\n\u001b[1;32m    871\u001b[0m         \u001b[39m# Binary mode\u001b[39;00m\n\u001b[0;32m--> 872\u001b[0m         handle \u001b[39m=\u001b[39m \u001b[39mopen\u001b[39;49m(handle, ioargs\u001b[39m.\u001b[39;49mmode)\n\u001b[1;32m    873\u001b[0m     handles\u001b[39m.\u001b[39mappend(handle)\n\u001b[1;32m    875\u001b[0m \u001b[39m# Convert BytesIO or file objects passed with an encoding\u001b[39;00m\n",
      "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: '../input/mdsb-2023/train.parquet'"
     ]
    }
   ],
   "source": [
    "# %% [markdown]\n",
    "# # MAP 536 - Python for Data Science - Predicting Cyclist Traffic in Paris\n",
    "\n",
    "# %% [code]\n",
    "import os\n",
    "import pandas as pd\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import mean_squared_error\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.svm import SVC\n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.model_selection import cross_val_score\n",
    "import numpy as np\n",
    "from pathlib import Path\n",
    "from sklearn.compose import ColumnTransformer\n",
    "from sklearn.model_selection import TimeSeriesSplit\n",
    "\n",
    "# %% [code]\n",
    "## + Weather data\n",
    "# Load training and testing datasets & remove unnecessary cols\n",
    "train_data = pd.read_parquet(\"../input/mdsb-2023/train.parquet\")\n",
    "test_data = pd.read_parquet(\"../input/mdsb-2023/final_test.parquet\")\n",
    "train_data.drop(columns=['counter_name', 'site_name','counter_id', 'counter_installation_date', 'counter_technical_id', 'site_id'], inplace=True)\n",
    "test_data.drop(columns=['counter_name', 'site_name','counter_id', 'counter_installation_date', 'counter_technical_id', 'site_id'], inplace=True)\n",
    "\n",
    "#Load weather dataset and remove irrelevant columns\n",
    "weather_data = pd.read_csv(\"../input/external-data/hourly-weather-data.csv\")\n",
    "weather_data = weather_data.drop(columns=['name', 'dew', 'preciptype','uvindex','icon','stations', 'sealevelpressure', 'winddir', 'sealevelpressure', 'solarradiation', 'solarenergy', 'severerisk'])\n",
    "\n",
    "# convert to datetime to merge them properly\n",
    "train_data['date'] = pd.to_datetime(train_data['date'])\n",
    "test_data['date'] = pd.to_datetime(test_data['date'])\n",
    "weather_data['datetime'] = pd.to_datetime(weather_data['datetime'])\n",
    "\n",
    "#merge with weather data\n",
    "merged_train_data = pd.merge(train_data, weather_data, left_on='date', right_on='datetime', how='inner')\n",
    "merged_test_data = pd.merge(test_data, weather_data, left_on='date', right_on='datetime', how='inner')\n",
    "merged_train_data = merged_train_data.drop(columns=['datetime'])\n",
    "merged_test_data = merged_test_data.drop(columns=['datetime'])\n",
    "\n",
    "\n",
    "## School Holidays + Weather data\n",
    "# import the holiday dataset\n",
    "schoolholiday_data = pd.read_csv(\"../input/external-data/fr-calendrier.csv\", delimiter=';')\n",
    "schoolholiday_data = schoolholiday_data[schoolholiday_data['zones'] == 'Zone C'] # Zone C is Paris\n",
    "schoolholiday_data = schoolholiday_data.drop(columns=['description','location','annee_scolaire', 'zones'])\n",
    "\n",
    "# Convert the date strings to datetime objects\n",
    "schoolholiday_data['start_date'] = pd.to_datetime(schoolholiday_data['start_date'], utc=True).dt.date\n",
    "schoolholiday_data['end_date'] = pd.to_datetime(schoolholiday_data['end_date'],utc=True).dt.date\n",
    "\n",
    "# Generate a set of unique dates for each range in a row\n",
    "unique_dates = set()\n",
    "for _, row in schoolholiday_data.iterrows():\n",
    "    unique_dates.update(pd.date_range(start=row['start_date'], end=row['end_date']))\n",
    "\n",
    "# Convert the set back to a list and create a DataFrame\n",
    "unique_dates_list = sorted(list(unique_dates)) \n",
    "schoolholiday_data = pd.DataFrame({'Date': unique_dates_list})\n",
    "\n",
    "# merge with rest of the data\n",
    "merged_train = pd.merge(merged_train_data, schoolholiday_data, left_on='date', right_on='Date', how='left')\n",
    "merged_train['Date'] = merged_train['Date'].apply(lambda x: 0 if pd.isna(x) else 1)\n",
    "merged_train.rename(columns={'Date': 'is_holiday'}, inplace=True)\n",
    "\n",
    "merged_test = pd.merge(merged_test_data, schoolholiday_data, left_on='date', right_on='Date', how='left')\n",
    "merged_test['Date'] = merged_test['Date'].apply(lambda x: 0 if pd.isna(x) else 1)\n",
    "merged_test.rename(columns={'Date': 'is_holiday'}, inplace=True)\n",
    "\n",
    "\n",
    "## School Holidays + Weather data + strike data\n",
    "# import the strike dataset\n",
    "from datetime import datetime  # Import the datetime class from the datetime module\n",
    "\n",
    "# strike dates for public transport in Paris, retrieved from: https://www.cestlagreve.fr/calendrier/?lieu=74&secteur=14&mois=1&annee=2022\n",
    "strike_dates = {'Date': [datetime(2020, 9, 17), datetime(2020, 12, 14), datetime(2020, 12, 16),\n",
    "                        datetime(2021, 1, 21), datetime(2021, 2, 4), datetime(2021, 2, 15),\n",
    "                        datetime(2021, 5, 21), datetime(2021, 6, 1), datetime(2021, 10, 5),\n",
    "                        datetime(2021, 11, 17)]}\n",
    "\n",
    "strike_data = pd.DataFrame(strike_dates)\n",
    "strike_data\n",
    "\n",
    "# Convert the date strings to datetime objects\n",
    "strike_data['Date'] = pd.to_datetime(strike_data['Date'])\n",
    "\n",
    "\n",
    "# merge with rest of the data\n",
    "merged_train = pd.merge(merged_train, strike_data, left_on='date', right_on='Date', how='left')\n",
    "merged_train['Date'] = merged_train['Date'].apply(lambda x: 0 if pd.isna(x) else 1)\n",
    "merged_train.rename(columns={'Date': 'is_strike'}, inplace=True)\n",
    "\n",
    "merged_test = pd.merge(merged_test, strike_data, left_on='date', right_on='Date', how='left')\n",
    "merged_test['Date'] = merged_test['Date'].apply(lambda x: 0 if pd.isna(x) else 1)\n",
    "merged_test.rename(columns={'Date': 'is_strike'}, inplace=True)\n",
    "merged_test.head()\n",
    "\n",
    "\n",
    "## School Holidays + Weather data + Strike data + Lockdown data\n",
    "lockdown_data = pd.read_csv(\"../input/external-data/lockdown-data.csv\")\n",
    "lockdown_data['datetime'] = pd.to_datetime(lockdown_data['datetime'])\n",
    "merged_train['date'] = pd.to_datetime(merged_train['date'])\n",
    "merged_test['date'] = pd.to_datetime(merged_test['date'])\n",
    "\n",
    "merged_train = pd.merge(merged_train, lockdown_data, left_on='date', right_on='datetime', how='left')\n",
    "merged_train = merged_train.drop(columns=['datetime'])\n",
    "merged_test = pd.merge(merged_test, lockdown_data, left_on='date', right_on='datetime', how='left')\n",
    "merged_test = merged_test.drop(columns=['datetime'])\n",
    "\n",
    "\n",
    "## Encode the dates\n",
    "def _encode_dates(X):\n",
    "    X = X.copy()  # modify a copy of X\n",
    "    X['date'] = pd.to_datetime(X['date'])\n",
    "    X.loc[:, \"year\"] = X[\"date\"].dt.year\n",
    "    X.loc[:, \"month\"] = X[\"date\"].dt.month\n",
    "    X.loc[:, \"day\"] = X[\"date\"].dt.day\n",
    "    X.loc[:, \"weekday\"] = X[\"date\"].dt.weekday\n",
    "    X.loc[:, \"hour\"] = X[\"date\"].dt.hour\n",
    "    return X\n",
    "\n",
    "merged_train = _encode_dates(merged_train)\n",
    "merged_test = _encode_dates(merged_test)\n",
    "\n",
    "# drop the date column\n",
    "X_merged_train = merged_train.drop(columns=['bike_count', 'log_bike_count', 'date', 'conditions'])\n",
    "Y_merged_train = merged_train['log_bike_count']\n",
    "\n",
    "X_merged_test = merged_test.drop(columns=['bike_count', 'log_bike_count', 'date', 'conditions'])\n",
    "Y_merged_test = merged_test['log_bike_count']\n",
    "\n",
    "X_merged_test.head()\n",
    "\n",
    "# %% [code]\n",
    "merged_train=merged_train.dropna()\n",
    "merged_train.info()\n",
    "\n",
    "# %% [code]\n",
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "\n",
    "# Define your features sets for XGBoost and LSTM\n",
    "features_xgb = ['latitude', 'longitude', 'temp', 'feelslike', 'humidity', \n",
    "                'precip', 'snow', 'snowdepth', 'windgust', 'windspeed', 'cloudcover', \n",
    "                'visibility', 'is_holiday', 'is_strike', 'full_lockdown', \n",
    "                'partial_lockdown', 'school_closures', 'business_closures', \n",
    "                'hour', 'year', 'month', 'day', 'weekday']\n",
    "\n",
    "# Target variable\n",
    "target = 'log_bike_count'\n",
    "\n",
    "# Splitting the data for XGBoost\n",
    "X_xgb = merged_train[features_xgb]\n",
    "y_xgb = merged_train[target]\n",
    "\n",
    "#splitting the data for test XGBoost\n",
    "X_xgb_test = merged_test[features_xgb]\n",
    "y_xgb_test = merged_test[target]\n",
    "\n",
    "# %% [code]\n",
    "from sklearn.pipeline import Pipeline\n",
    "from xgboost import XGBRegressor\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# Step 1: Creating the Pipeline\n",
    "pipeline = Pipeline([\n",
    "    ('scaler', StandardScaler()), \n",
    "    ('xgb', XGBRegressor(objective='reg:squarederror'))\n",
    "])\n",
    "\n",
    "# Step 2: Fitting the Model\n",
    "pipeline.fit(X_xgb, y_xgb)\n",
    "\n",
    "# Step 3: Making Predictions\n",
    "y_pred_xgb = pipeline.predict(X_xgb_test)\n",
    "\n",
    "# Calculate the RMSE for the XGBoost model\n",
    "rmse_xgb = np.sqrt(mean_squared_error(y_xgb_test, y_pred_xgb))\n",
    "print(f\"Root Mean Squared Error (RMSE) for XGBoost on Cross-Validation Set: {rmse_xgb:.2f}\")\n",
    "\n",
    "# Step 4: Preparing the Submission File\n",
    "results = pd.DataFrame({\n",
    "    'Id': np.arange(y_pred_xgb.shape[0]),\n",
    "    'log_bike_count': y_pred_xgb\n",
    "})\n",
    "results.to_csv(\"submission.csv\", index=False)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}