#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 22:39:59 2021

@author: philipp

INFO VIS: Top Countries where famous musicians are coming from
"""

# libraries
import pandas as pd  # data processing, CSV/JSON file I/O (e.g. pd.read_csv)
import numpy as np
import matplotlib.pyplot as plt
from utils.filefinder import find_file

# styling
color1 = "#640019"  # bordeau red
color2 = "#fa9600"  # orange
color3 = "#434040"  # dark grey
color4 = "#CCBFBF"  # light grey
plt.rcParams["figure.dpi"] = 144

# load data frame
# Hint: Where necessary fix the file path to match the current working
#       directory of your IDE by removing '../' or using an absolute path.
df = pd.read_json(find_file("famousArtists.json"))  # get dataframe

print("Analyze famousArtists.json")
print("==========================")
df.info()

first50 = df.head(50)
print("\nFirst 50 entries:")
print(first50)

# Cleanup of multiple-values
df["genre"] = str(df["genres"]).split(", ")[0]
df["intr"] = str(df["instrs"]).split(", ")[0]

# misssing data?
print("\nMisssing data:")
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
print("\nimported records: " + str(len(df)))
df["country"].replace("", np.nan, inplace=True)
# drop records
df.dropna(inplace=True)
print("cleaned countries:  " + str(len(df)))

# helper column for plot
df["count"] = 1

#
data = df.groupby("country")["count"].sum().sort_values(ascending=False)[:10]

# plot
color_map = [color1 for _ in range(10)]
color_map[0] = color_map[1] = color_map[2] = color2  # color highlight

fig, ax = plt.subplots(1, 1, figsize=(11, 7))
ax.bar(
    data.index, data, width=0.5, edgecolor="darkgray", linewidth=0.6, color=color_map
)

# annotations
for i in data.index:
    ax.annotate(
        f"{data[i]}",
        xy=(i, data[i] + 150),  # i like to change this to roughly 5% of the highest cat
        va="center",
        ha="center",
        fontweight="light",
        fontfamily="sans-serif",
    )

# remove border from plot
for s in ["top", "left", "right"]:
    ax.spines[s].set_visible(False)

# tick labels
ax.set_xticklabels(data.index, fontfamily="sans-serif", rotation=0)

# title and sub-title
fig.text(
    0.09,
    0.95,
    "Top 10 Countries Where Famous Musicians Are Coming From",
    fontsize=15,
    fontweight="bold",
    fontfamily="serif",
)
fig.text(
    0.09,
    0.91,
    "The three most dominant countries highlighted are: United States of America, Great Britain, and Jamaika.",
    fontsize=12,
    fontweight="light",
    fontfamily="serif",
)
fig.text(
    0.2,
    0.03,
    "Author: Philipp Ackermann, philipp@metason.net;  Data Source: https://music.metason.net/famousArtists.html",
    fontsize=10,
    fontfamily="sans-serif",
    color=color3,
)

# insight text
fig.text(0.375, 0.63, "Insights", fontsize=12, fontweight="bold", fontfamily="serif")
fig.text(
    0.375,
    0.363,
    """
The most famous musicians and 
bands are, primarily, from
the USA, with GB and Jamaika
a significant distance behind.

It is at no surprise, that the
first two are native English-
speaking countries, as it is
the world-dominant language. 
""",
    fontsize=11,
    fontweight="light",
    fontfamily="serif",
)

ax.grid(axis="y", linestyle="-", alpha=0.4)
grid_y_ticks = np.arange(0, 2500, 500)  # y ticks, min, max, then step
ax.set_yticks(grid_y_ticks)
ax.set_axisbelow(True)

# axis labels
plt.xlabel(
    "Country the artist was born or the band was founded",
    fontsize=12,
    fontweight="light",
    fontfamily="sans-serif",
    loc="left",
    y=-1.5,
)
plt.ylabel(
    "Count of famous musicians and bands",
    fontsize=12,
    fontweight="light",
    fontfamily="sans-serif",
)
# plt.legend(loc='upper right')

# thicken the bottom line
plt.axhline(y=0, color="black", linewidth=1.3, alpha=0.7)
ax.tick_params(axis="both", which="major", labelsize=12)

# remove x axis ticks
ax.tick_params(axis="both", which="both", length=0)

plt.tight_layout()  # othrwise title is not shown
plt.subplots_adjust(top=0.86, bottom=0.13)  # Add space

plt.savefig("infovis/PNG/artistsTopCountries.png")
plt.savefig("infovis/SVG/artistsTopCountries.svg")
plt.show()
