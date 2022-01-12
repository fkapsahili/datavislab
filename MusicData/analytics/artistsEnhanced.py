#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 5 08:46:26 2022
@author: Philipp Ackermann

ENHANCED ANALYTICS OF ARTISTS
"""
#%% # tag to run as Jupyter notebook 

# libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV/JSON file I/O
import datetime as dt
import gender
import matplotlib.pyplot as plt # only used to set bgcolor of figure

plt.rcParams.update({
    "figure.facecolor": (1.0, 1.0, 1.0, 1.0),  # white with no transparency
    "savefig.facecolor": (1.0, 1.0, 1.0, 1.0)  # white with no transparency
})

# Calculate year when career start
# For individual artists, we add assumed 20 years to their birthdate
def startYear(lifespan, isGroup):
    if isGroup == 1:
        if lifespan[0] == '*':
            return dt.datetime.strptime(lifespan[1:5], '%Y').year
        else:
            return dt.datetime.strptime(lifespan[0:4], '%Y').year
    else:
        if lifespan[0] == '*':
            return dt.datetime.strptime(str(int(lifespan[1:5]) + 20), '%Y').year
        else:
            return dt.datetime.strptime(str(int(lifespan[0:4]) + 20), '%Y').year

def endYear(lifespan, defaultYear=np.nan):
    if lifespan[0] == '*':
        if np.isnan(defaultYear):
            return np.nan
        if defaultYear.length() != 4:
            return np.nan
        return dt.datetime.strptime(defaultYear, '%Y').year
    else:
        return dt.datetime.strptime(lifespan[5:], '%Y').year
    

def getGender(fullname, isGroup):
    if isGroup == 1:
        return np.nan
    name = fullname.replace('Dr. ', '').replace('Mr. ', '').replace('Mrs. ', '').replace('Ms. ', '').replace('DJ ', '').replace('MC ', '').replace('Little ', '').replace('Slim ', '').replace('Big ', '').replace('Blind ', '').replace('Doc ', '').replace('Reverend ', '').replace('The ', '')
    list = name.split(' ')
    prename = list[0].upper()
    if fullname in ['R. Kelly','LL Cool J','Mos Def','Busta Rhymes','DMX','50 Cent','Red Garland']:
        return 'male'
    if fullname in ['Leni Stern']:
        return 'female'
    result = np.nan
    if prename in gender.gender.keys():
        result = gender.gender[prename]
        if (result == 'female' or result == 'male'):
            return result
    #print(prename + ' - ' + fullname)
    return np.nan

# ---- data prep ----

# load data frame
# Hint: Relative path works when executeed as Jupyter notebook.
#       Where necessary fix the file path to match the current working 
#       direectory of your IDE by removing '../' or using an absolute path.
df = pd.read_json('../data/famousArtists.json') # get dataframe

print("Enhance famousArtists.json")
print("==========================")
df.info()
# Cleanup of multiple-values 
df['genre'] = df['genres'].str.split(", ").str[0]
df['instr'] = df['instrs'].str.split(", ").str[0]

# missing values?
print("\nMisssing values:")

for i in df.columns:
    null_rate = df[i].isna().sum() / len(df) * 100 
    empty_rate = df[i].eq('').sum() / len(df) * 100
    if null_rate > 0 :
        print("{} null rate: {}%".format(i,round(null_rate,2)))
    if empty_rate > 0 :
        print("{} empty rate: {}%".format(i,round(empty_rate,2)))

# data cleansing
print("\nimported records: " + str(len(df)))
df['country'].replace('', np.nan, inplace=True)
df['lifespan'].replace('', np.nan, inplace=True)

# drop records
df.dropna(inplace=True)
print("cleaned records:  " + str(len(df)))

# data enhancing: year when career started
df['start'] = df.apply(lambda row: startYear(row.lifespan, row.isGroup), axis = 1)
df['end'] = df.apply(lambda row: endYear(row.lifespan), axis = 1)
df['gender'] = df.apply(lambda row: getGender(row.artist, row.isGroup), axis = 1)

df.info()
first20 = df.head(20)
print("\nFirst 20 entries:")
print(first20)

# ---- feature engineering ----

# analyse career start of musicians vs bands
careers = df.groupby('start')['isGroup'].value_counts().unstack()
careers.fillna(0)
careers.plot.bar(figsize=(20, 10), title='Career Start of Musicians vs Bands')

# analyse gender
gender = df.groupby('gender')['gender'].value_counts().unstack()
gender.plot.bar(title='Gender of Musicians')

# analyse gender over time (when career started)
gender = df.groupby('start')['gender'].value_counts().unstack()
gender.plot.bar(figsize=(20, 10), title='Gender of Musicians over Time')

# %%