#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 4 08:36:26 2022
@author: Philipp Ackermann

ANALYTICS OF ARTISTS
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
df = pd.read_json(find_file("famousArtists.json"))  # get dataframe

print("Analyze famousArtists.json")
print("==========================")
df.info()

first20 = df.head(20)
print("\nFirst 20 entries:")
print(first20)

# Cleanup of multiple-values
df["genre"] = df["genres"].str.split(", ").str[0]
df["instr"] = df["instrs"].str.split(", ").str[0]

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

# data cleansing
print(f"\nimported records: {len(df)}")
df["country"].replace("", np.nan, inplace=True)
df["lifespan"].replace("", np.nan, inplace=True)

# drop records
df.dropna(inplace=True)
print(f"cleaned records:  {len(df)}")

first20 = df.head(20)
print("\nFirst 20 entries:")
print(first20)

# ---- feature engineering ----

# analyse musicians vs bands
print("\nIndividual musicians vs music groups counted:")
print(df.groupby("isGroup")["isGroup"].count().sort_values(ascending=False))
genres = df.groupby("isGroup")["isGroup"].value_counts().unstack()
genres.plot.bar(title="Individual Artists vs. Music Bands")

# analyse countries
print("\nCountries counted and sorted:")
print(df.groupby("country")["isGroup"].count().sort_values(ascending=False))
genres = df.groupby("country")["isGroup"].value_counts().unstack()
genres.plot.bar(figsize=(10, 10), title="Musicians and Bands per Country")

# analyse intruments (exclude groups)
print("\Instrument categories counted and sorted:")
print(
    df[(df["isGroup"] == 0)]
    .groupby("instr")["isGroup"]
    .count()
    .sort_values(ascending=False)
)

# analyse genres
print("\nGenre categories counted and sorted:")
print(df.groupby("genre")["genre"].count().sort_values(ascending=False))

genres = df.groupby("genre")["isGroup"].value_counts().unstack().T
genres.plot.bar(stacked=True, figsize=(10, 10), title="Genres of Musicians and Bands")

genres_band = df.groupby("genre")["isGroup"].value_counts().unstack()
genres_band.plot.bar(
    stacked=True, figsize=(10, 10), title="Split of Musicians and Bands per Genre"
)

# filter top 6 countries
criterion2 = df["country"].isin(["US", "GB", "JM", "CA", "FR", "DE"])
filtered_genre2 = df[criterion2].groupby("genre")["country"].value_counts().unstack().T
filtered_genre2.plot.bar(
    stacked=True, figsize=(10, 10), title="Genres in Top 6 Countries"
)

# filter top 6 countries and top 6 genres
criterion3 = (df["country"].isin(["US", "GB", "JM", "CA", "FR", "DE"])) & (
    df["genre"].isin(["Jazz", "Rock", "Pop", "Electronic", "R&B", "Indie"])
)
filtered_genre3 = df[criterion3].groupby("genre")["country"].value_counts().unstack().T
filtered_genre3.plot.bar(
    stacked=True, figsize=(10, 10), title="Top 5 Genres in Top 6 Countries"
)

# %%
