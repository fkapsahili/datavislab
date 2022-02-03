#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 22:39:59 2021

@author: philipp

INFO VIS: Individual Artists vs. Musical Bands over Time
"""

# libraries
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV/JSON file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import datetime as dt
from utils.filefinder import find_file

# Calculate year when career started
# For individual artists, we add assumed 20 years to their birthdate
def start_year(lifespan, is_group):
    if is_group == 1:
        if lifespan[0] == "*":
            return dt.datetime.strptime(lifespan[1:5], "%Y").year
        else:
            return dt.datetime.strptime(lifespan[0:4], "%Y").year
    else:
        if lifespan[0] == "*":
            return dt.datetime.strptime(str(int(lifespan[1:5]) + 20), "%Y").year
        else:
            return dt.datetime.strptime(str(int(lifespan[0:4]) + 20), "%Y").year


# load data frame
# Hint: Where necessary fix the file path to match the current working
#       directory of your IDE by removing '../' or using an absolute path.
df = pd.read_json(find_file("famousArtists.json"))  # get dataframe

# data cleansing
print("\nimported records: " + str(len(df)))
df["lifespan"].replace("", np.nan, inplace=True)

# drop records
df.dropna(inplace=True)
print("cleaned lifespan: " + str(len(df)))

# data enhancing: year when career started
df["year"] = df.apply(lambda row: start_year(row.lifespan, row.isGroup), axis=1)
df.info()

# styling
color1 = "#640019"  # bordeau red
color2 = "#fa9600"  # orange
color3 = "#434040"  # dark grey
color4 = "#CCBFBF"  # light grey
colors = [color1, color2]
plt.rcParams["figure.dpi"] = 144

sub = df.groupby("isGroup")["year"].value_counts().unstack().T
fig, ax = plt.subplots(1, 1, figsize=(11, 7))
plt.stackplot(sub.index, sub[0].values, sub[1].values, colors=colors)

# axis labels
plt.xlabel(
    "Year the career was started (assuming at age 20) or the band was founded",
    fontsize=12,
    fontweight="light",
    fontfamily="sans-serif",
    loc="left",
)
plt.ylabel(
    "Count of famous musicians and bands",
    fontsize=12,
    fontweight="light",
    fontfamily="sans-serif",
)

ax.axhline(y=0, color="black", linewidth=1.3, alpha=0.7)

for s in ["top", "right", "bottom"]:
    ax.spines[s].set_visible(False)

ax.grid(False)

ax.set_xlim(1920, 2020)
plt.xticks(np.arange(1920, 2020, 10))
ax.tick_params(axis=u"both", which=u"both", length=0)

# text elements
fig.text(
    0.08,
    0.95,
    "Famous Musicians and Bands over the Last 100 Years",
    fontsize=15,
    fontweight="bold",
    fontfamily="serif",
)
fig.text(
    0.08,
    0.75,
    """We see that from the early years mainly
individual artists are remembered. 

In the 60s music groups such as Pop bands,
Rock groups, and Jazz combos get famous 
as well.
""",
    fontsize=12,
    fontweight="light",
    fontfamily="serif",
)

fig.text(
    0.2,
    0.03,
    "Author: Philipp Ackermann, philipp@metason.net;  Data Source: https://music.metason.net/famousArtists.html",
    fontsize=9,
    fontfamily="sans-serif",
    color=color3,
)


plt.annotate(
    "",
    xy=(1963, 49),
    xycoords="data",
    xytext=(-80, 94),
    textcoords="offset points",
    size=20,
    arrowprops=dict(
        arrowstyle="simple", fc="0.6", ec="none", connectionstyle="arc3,rad=0.3"
    ),
)

fig.text(
    0.27,
    0.19,
    "Individual Artists",
    fontweight="bold",
    fontfamily="serif",
    fontsize=15,
    color="white",
)
fig.text(
    0.49,
    0.5,
    "Music Groups",
    fontweight="bold",
    fontfamily="serif",
    fontsize=15,
    color="black",
)

# annotate
plt.annotate(
    "",
    xy=(2000, 30),
    xycoords="data",
    xytext=(2020, 30),
    textcoords="data",
    arrowprops=dict(arrowstyle="<|-|>", connectionstyle="arc3"),
)
plt.annotate(
    "Career Building Gap", xy=(2001.5, 31), xycoords="data", fontsize=11, weight="bold"
)
fig.text(
    0.74,
    0.52,
    """There is a career building 
gap of ~20 years before  
artists get famous. This is   
the time of releasing new  
albums and going on tours  
to become well-known.
""",
    fontsize=12,
    fontweight="light",
    fontfamily="serif",
)
# plt.arrow( 2011, 41, 0, -5, fc="k", ec="k", head_width=0.9, head_length=2, edgecolor ='green')

plt.annotate(
    "",
    xy=(2003, 33),
    xycoords="data",
    xytext=(-20, 42),
    textcoords="offset points",
    size=20,
    arrowprops=dict(
        arrowstyle="simple", fc="0.5", ec="none", connectionstyle="arc3,rad=0.3"
    ),
)

plt.tight_layout()  # othrwise title is not shown
plt.subplots_adjust(top=0.86, bottom=0.12)  # Add space

plt.savefig("infovis/PNG/artistsOverTime.png")
plt.savefig("infovis/SVG/artistsOverTime.svg")
plt.show()
