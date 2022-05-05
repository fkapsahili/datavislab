"""
Created on Thu Apr 28 14:44:02 2022

@author: Fabio Kapsahili

POPULAR GENRES OVER TIME
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime


import json

json_path = "../data/recomAlbums.json"
data = None

with open(json_path, "r") as j:
    data = json.loads(j.read())


dates = []
names = []
for item in data:
    if len(item["year"]) > 0:
        dates.append(item["year"])
        genre = item["genres"].split(",")[0]
        names.append(genre)
dates = [datetime.strptime(d, "%Y") for d in dates]


# Choose some nice levels
levels = np.tile([-5, 5, -3, 3, -1, 1], int(np.ceil(len(dates) / 6)))[: len(dates)]

# Create figure and plot a stem plot with the date
fig, ax = plt.subplots(constrained_layout=True)
ax.set(title="Popular genres over time")

ax.vlines(dates, 0, levels, color="tab:red")  # vertical lines
ax.plot(dates, np.zeros_like(dates), "o", color="tab:red")  # markers


# annotate lines
for d, l, r in zip(dates, levels, names):
    ax.annotate(
        r,
        xy=(d, l),
        xytext=(-3, np.sign(l) * 1),
        textcoords="offset points",
        horizontalalignment="right",
        verticalalignment="bottom" if l > 0 else "top",
    )


# format xaxis with 5 year intervals
ax.xaxis.set_major_locator(mdates.YearLocator(5))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

ax.set_ylim(bottom=0)
# ax.yaxis.set_visible(False)

ax.spines[["left", "top", "right"]].set_visible(False)
ax.margins(y=0.1)

plt.show()
