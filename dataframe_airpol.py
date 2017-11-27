from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt

ap = pd.read_csv(r'Documents\airpol.csv')

ap.fillna(ap.ffill(), inplace=True)

ap[ap['Core Based Statistical Area'].isin(['Wichita, KS'])]  # testing to see if fillna worked

ap['Core Based Statistical Area'] = ap['Core Based Statistical Area'].str.replace(',',' ')
ap.set_index(ap['Core Based Statistical Area'], inplace=True)
ap2 = ap[ap['Pollutant'].isin(['PM25'])]
ap2.index.names = ['City']

del ap2['Core Based Statistical Area']
ap2.drop('CBSA', axis=1, inplace=True)
ap2.drop('Number of Trends Sites', axis=1, inplace=True)

airpol = ap2[ap2['Trend Statistic'].isin(['98th Percentile'])]

airpol.drop('Pollutant', axis=1, inplace=True)
airpol.drop('Trend Statistic', axis=1, inplace=True)

# Pivotting the table for Tableau

appivot = airpol.T  # transpose

appivot.index.names = ['Year']

