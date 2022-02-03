#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 08:36:26 2022
@author: Philipp Ackermann

ANALYTICS OF ALBUMS
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
df = pd.read_json(find_file("recomAlbums.json"))

print("Analyze recomAlbums.json")
print("========================")
df.info()

first20 = df.head(20)
print("\nFirst 20 entries:")
print(first20)

# cleanup of multiple-values
df["genre"] = df["genres"].str.split(", ").str[0]

# missing data?
print("\nMissing data:")
print(df.isnull().sum())

# missing values?
print("\nMissing values:")

for i in df.columns:
    null_rate = df[i].isna().sum() / len(df) * 100
    empty_rate = df[i].eq("").sum() / len(df) * 100
    if null_rate > 0:
        print(f"{i} null rate: {null_rate:.2f}%")
    if empty_rate > 0:
        print(f"{i} empty rate: {empty_rate:.2f}%")

# data cleansing
print(f"\nimported records: {len(df)}")
df["year"].replace("", np.nan, inplace=True)
# drop records
df.dropna(inplace=True)
print(f"cleaned years:    {len(df)}")

# ---- feature engineering ----

# analyse genre
print("\nGenre categories counted and sorted:")
print(df.groupby("genre")["year"].count().sort_values(ascending=False))
genre_over_time = df.groupby("genre")["year"].value_counts().unstack().T
genre_over_time.plot.area(
    stacked=True, figsize=(10, 10), title="Recommended Music Albums"
)

# filter year range
criterion = (df["year"] > "1999") & (df["year"] < "2016")
filtered_genre_over_time = (
    df[criterion].groupby("genre")["year"].value_counts().unstack().T
)
filtered_genre_over_time.plot.area(
    stacked=True, figsize=(10, 10), title="Recommended Music Albums between 2000-2015"
)

# filter year range and top 6 genres
criterion2 = (
    (df["year"] > "1949")
    & (df["year"] < "2016")
    & (df["genre"].isin(["Jazz", "Rock", "Pop", "Electronic", "R&B", "Indie"]))
)
filtered_genre2 = df[criterion2].groupby("genre")["year"].value_counts().unstack().T
filtered_genre2.plot.area(
    stacked=True, figsize=(10, 10), title="Top 6 Genres of Recommended Music Albums"
)


# %%
