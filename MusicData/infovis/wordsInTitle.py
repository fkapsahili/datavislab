#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 22:39:59 2021

@author: philipp

INFO VIS: WORDS IN ALBUM TITLES
"""

# libraries
# Word Cloud from https://github.com/amueller/word_cloud
from wordcloud import WordCloud
import pandas as pd  # data processing, CSV/JSON file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import matplotlib.colors as clrs

# load data frame
df = pd.read_json("data/recomAlbums.json")  # get dataframe

# styling
color1 = "#640019"  # bordeau red
color2 = "#fa9600"  # orange
color3 = "#434040"  # dark grey
color4 = "#CCBFBF"  # light grey
plt.rcParams["figure.dpi"] = 144

# custom color map
cmap = clrs.LinearSegmentedColormap.from_list("", [color1, color2])

# grab text from title and clean it
text = (
    str(list(df["title"]))
    .replace(",", "")
    .replace("[", "")
    .replace("'", "")
    .replace("]", "")
    .replace(".", "")
    .replace("Edition", "")
    .replace("Vol ", "")
    .replace("Volume", "")
)

# create world cloud
wordcloud = WordCloud(
    background_color="white", width=840, height=620, colormap=cmap, max_words=170
).generate(text)

plt.figure(figsize=(8.4, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)
plt.title(
    "Most Used Words in Title of Recommended Albums",
    fontweight="bold",
    fontfamily="serif",
    fontsize=16,
    color="black",
)
plt.text(
    25,
    645,
    "Author: Philipp Ackermann, philipp@metason.net;  Data Source: https://music.metason.net/greatRecords.html",
    fontsize=9,
    fontfamily="sans-serif",
    color=color3,
)

plt.tight_layout()  # othrwise title is not shown
plt.subplots_adjust(top=0.95, bottom=0.05)  # Add space

plt.savefig("infovis/PNG/wordsInTitle.png")
plt.savefig("infovis/SVG/wordsInTitle.svg")
plt.show()
