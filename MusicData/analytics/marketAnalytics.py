#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 4 08:36:26 2022
@author: Philipp Ackermann

ANALYTICS OF US MUSIC MARKET
"""
#%% # tag to run as Jupyter notebook

# libraries
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV/JSON file I/O
import matplotlib.pyplot as plt  # only used to set bgcolor of figure
from utils.filefinder import find_file


plt.rcParams.update(
    {
        "figure.facecolor": (1.0, 1.0, 1.0, 1.0),  # white with no transparency
        "savefig.facecolor": (1.0, 1.0, 1.0, 1.0),  # white with no transparency
    }
)

# ---- data prep ----

# load data frame
# Hint: Relative path works when executeed as Jupyter notebook.
#       Where necessary fix the file path to match the current working
#       directory of your IDE by removing '../' or using an absolute path.
df = pd.read_csv(
    find_file("USMusicMarket.csv"), header=0, encoding="utf8"
)  # get dataframe

print("Analyze USMusicMarket.csv")
print("===========================")
df.info()
print(df.describe())

first20 = df.head(20)
print("\nFirst 20 entries:")
print(first20)

# missing data?
print("\nMissing data:")
print(df.isnull().sum())

# missing values?
print("\nMisssing values:")

for i in df.columns:
    null_rate = df[i].isna().sum() / len(df) * 100
    empty_rate = df[i].eq("").sum() / len(df) * 100
    if null_rate > 0:
        print(f"{i} null rate: {null_rate:.2f}%")
    if empty_rate > 0:
        print(f"{i} empty rate: {empty_rate:.2f}%")

# ---- feature engineering ----

# analyse overall market revenue
print("\Analyse overall market revenue:")
revenues = df.groupby("year")["value"].sum()
# print(revenues)
revenues.plot.bar(figsize=(10, 14), title="Revenue of US Recordings in Mio $")

# analyse revenue per format
formats = df.groupby(["format", "year"])["value"].sum().unstack().T
# print(formats.head(10))
formats.plot.bar(
    stacked=True, figsize=(10, 14), title="Revenue of US Recordings per Format in Mio $"
)

# aggregate formats related to music albums
formats["Vinyl"] = formats["LP/EP"] + formats["Vinyl Single"]
formats["Compact Disc"] = formats["CD"] + formats["CD Single"]
formats["Music Casssette"] = formats["Cassette"] + formats["Cassette Single"]
formats["Download"] = (
    formats["Download Album"]
    + formats["Download Single"]
    + formats["SoundExchange Distributions"]
)
formats["Streaming"] = (
    formats["Limited Tier Paid Subscription"]
    + formats["On-Demand Streaming (Ad-Supported)"]
    + formats["Other Ad-Supported Streaming"]
    + formats["Paid Subscription"]
)

filtered = formats[
    ["Vinyl", "8-Track", "Music Casssette", "Compact Disc", "Download", "Streaming"]
]
filtered.plot.area(
    stacked=True,
    figsize=(10, 8),
    title="Revenue of US Music Recordings per Media in Mio $",
)

# Percentage of music market
year_total = filtered.sum(axis="columns")
format_pct = filtered.div(year_total, axis="index")
format_pct.plot.area(
    stacked=True, figsize=(10, 5), title="Media Percentage of US Music Recordings"
)

# %%
