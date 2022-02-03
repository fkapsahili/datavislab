#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 22:39:59 2021

@author: philipp

INFO VIS: Ratio of Individual Artists vs. Musical Bands
"""

# libraries
import pandas as pd  # data processing, CSV/JSON file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from utils.filefinder import find_file

# load data frame
df = pd.read_json(find_file("famousArtists.json"))  # get dataframe

# styling
color1 = "#640019"  # bordeau red
color2 = "#fa9600"  # orange
color3 = "#434040"  # dark grey
color4 = "#CCBFBF"  # light grey
plt.rcParams["figure.dpi"] = 144

# artist vs band ratio
x = df.groupby(["isGroup"])["isGroup"].count()
y = len(df)
r = ((x / y)).round(3)
ab_ratio = pd.DataFrame(r).T
print(ab_ratio)

# visualize
fig, ax = plt.subplots(1, 1, figsize=(6.25, 2.25))

ax.barh(ab_ratio.index, ab_ratio[0], color=color1, alpha=0.9, label="Artist")
ax.barh(
    ab_ratio.index, ab_ratio[1], left=ab_ratio[0], color=color2, alpha=0.9, label="Band"
)

ax.set_xlim(0, 1)
ax.set_xticks([])
ax.set_yticks([])

# distribution percentage
for i in ab_ratio.index:
    ax.annotate(
        f"{round(ab_ratio[0][i]*100)}%",
        xy=(ab_ratio[0][i] / 2, i),
        va="center",
        ha="center",
        fontsize=40,
        fontweight="light",
        fontfamily="serif",
        color="white",
    )

    ax.annotate(
        "Individual Artists",
        xy=(ab_ratio[0][i] / 2, -0.25),
        va="center",
        ha="center",
        fontsize=15,
        fontweight="light",
        fontfamily="serif",
        color="white",
    )

for i in ab_ratio.index:
    ax.annotate(
        f"{round(ab_ratio[1][i]*100)}%",
        xy=(ab_ratio[0][i] + ab_ratio[1][i] / 2, i),
        va="center",
        ha="center",
        fontsize=40,
        fontweight="light",
        fontfamily="serif",
        color="black",
    )
    ax.annotate(
        "Music Groups",
        xy=(ab_ratio[0][i] + ab_ratio[1][i] / 2, -0.25),
        va="center",
        ha="center",
        fontsize=15,
        fontweight="light",
        fontfamily="serif",
        color="black",
    )

# title & subtitle
fig.text(
    0.0275,
    0.86,
    "Artists versus Bands",
    fontfamily="serif",
    fontsize=15,
    fontweight="bold",
)
fig.text(
    0.0275,
    0.74,
    "Individual musicians get more likely famous than bands.",
    fontfamily="serif",
    fontsize=12,
)
fig.text(
    0.2,
    0.03,
    "Data Source: https://music.metason.net/famousArtists.html",
    fontsize=9,
    fontfamily="sans-serif",
    color=color3,
)

for s in ["top", "left", "right", "bottom"]:
    ax.spines[s].set_visible(False)

# Removing legend due to labelled plot
ax.legend().set_visible(False)

plt.tight_layout()  # othrwise title is not shown
plt.subplots_adjust(top=0.7, bottom=0.1)  # Add space
plt.savefig("infovis/PNG/artistsBands.png")
plt.savefig("infovis/SVG/artistsBands.svg")
plt.show()
