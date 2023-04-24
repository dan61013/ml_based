"""
Will it rain in Australia tomorrow?
Refer: https://www.kaggle.com/code/smriti19/will-it-rain-in-australia-tomorrow/notebook?scriptVersionId=73537100
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import missingno as msno
import warnings

warnings.filterwarnings('ignore')

weather = pd.read_csv(f'{os.getcwd()}/data/weatherAUS.csv')
print(weather.head())
print(f'Shape of DataFrame: {weather.shape}')
print(f'Names of columns of DataFrame: {weather.columns}')

# Get Null values
# msno.matrix(weather)
# print(weather.isnull().sum())
# plt.show()  # 使用plt顯示分佈圖

# Statistical insights into the dataset
print(weather.describe())

# sns.countplot(data=weather, x='RainTomorrow')
# plt.show()

weather['Date'] = pd.to_datetime(weather['Date'])
weather['Day'] = weather['Date'].dt.day
weather['Year'] = weather['Date'].dt.year
# Dropping the Date column since day and month have already been extracted as integer values.
weather.drop('Date', axis=1, inplace=True)

# numerical columns
numerical_columns = weather._get_numeric_data().columns
print(f'Numerical columns: {list(numerical_columns)}')

# category columns
categorical_columns = list(set(weather) - set(numerical_columns))
print(f"Categorical columns: {categorical_columns}")

# plt.figure(figsize=(18, 8))
# mask_1 = np.triu(np.ones_like(weather.corr(), dtype=np.bool))
# heatmap = sns.heatmap(weather.corr(), annot=True, cmap='coolwarm', mask=mask_1)
# heatmap.set_title('Correlation heatmap', fontdict={'fontsize': 16})
# plt.show()

fig, axes = plt.subplots(2, 2, figsize=(30, 20))
sns.set_style('whitegrid')

# Maximum Temperature
plt.subplot(2, 2, 1)
plt.title('Maximum Temperature variation over the years', fontweight='bold', fontsize=20)
plt.xlabel('MaxTemp', fontweight='bold', fontsize=16)
sns.distplot(weather['MaxTemp'], color='indigo', bins=25)

# Minimum Temperature
plt.subplot(2, 2, 2)
plt.title('Minimum Temperature variation over the years', fontweight='bold', fontsize=20)
plt.xlabel('MinTemp', fontweight='bold', fontsize=16)
sns.distplot(weather['MinTemp'], color='blue')

# Sunshine
plt.subplot(2, 2, 3)
plt.title('Sunshine over the years', fontweight='bold', fontsize=20)
plt.xlabel('Sunshine', fontweight='bold', fontsize=16)
sns.distplot(weather['Sunshine'], color='green', bins=50)

# Evaporation 蒸發 
plt.subplot(2, 2, 4)
plt.title('Evaporation over the years', fontweight='bold', fontsize=20)
plt.xlabel('Evaporation', fontweight='bold', fontsize=16)
sns.distplot(weather['Evaporation'], color='red', bins=50)

print('\033[1m' + 'The mean max. temp. is: ', weather['MaxTemp'].mean())
print('\033[1m' + 'The mean min. temp. is: ', weather['MinTemp'].mean())
print('\033[1m' + 'The mean sunshine over the years is: ', weather['Sunshine'].mean())
print('\033[1m' + 'The mean evaporation over the years is: ', weather['Evaporation'].mean())

plt.show()
