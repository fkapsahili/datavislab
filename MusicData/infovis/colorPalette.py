#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 16:34:09 2021

@author: philipp

INFO VIS: COLOR PALETTE
"""

import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib.cbook import get_sample_data
import seaborn
from pathlib import Path

script_dir = Path(__file__).resolve().parent

# styling
color1 = "#640019"  # bordeau red
color2 = "#fa9600"  # orange
color3 = "#434040"  # dark grey
color4 = "#CCBFBF"  # light grey
plt.rcParams["figure.dpi"] = 144

# list predefined styles
print(plt.style.available)

# show my color palette
seaborn.palplot(
    [color1, color2, "black", color3, color4, "white", "white", "white"], size=1.6
)

plt.text(
    -0.5, -1.1, "Color Palette ", fontfamily="serif", fontweight="bold", fontsize=14
)
plt.text(
    -0.5,
    -0.72,
    "Colors from CI/CD of Metason and its ArtistInfo App",
    fontsize=14,
    fontweight="light",
    fontfamily="serif",
)
plt.text(
    -0.5,
    0.86,
    u"Author: Philipp Ackermann, philipp@metason.net;  Data Source: https://www.metason.net",
    fontsize=9,
    fontfamily="sans-serif",
    color=color3,
)
plt.tight_layout()
plt.subplots_adjust(top=0.6, bottom=0.2, left=0.02, right=0.95)  # Add space

ax = plt.subplot(111)
ax.set_xticks([])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)

# add company logo
fn1 = get_sample_data(
    script_dir.joinpath("images/metason.png"),
    asfileobj=False,
)
logoimg = plt.imread(fn1, format="png")
imagebox = OffsetImage(logoimg, zoom=0.4)
xy = [6.1, -0.33]  # coordinates to position this image

ab1 = AnnotationBbox(
    imagebox,
    xy,
    xybox=(0.0, 0.0),
    xycoords="data",
    boxcoords="offset points",
    frameon=False,
)
ax.add_artist(ab1)

# add app logo
fn2 = get_sample_data(
    script_dir.joinpath("images/ArtistInfo.png"),
    asfileobj=False,
)
appimg = plt.imread(fn2, format="png")
imagebox2 = OffsetImage(appimg, zoom=0.265)
xy2 = [7.3, -0.33]  # coordinates to position this image

ab2 = AnnotationBbox(
    imagebox2,
    xy2,
    xybox=(0.0, 0.0),
    xycoords="data",
    boxcoords="offset points",
    frameon=False,
)
ax.add_artist(ab2)


plt.savefig(script_dir.joinpath("PNG/colorPalette.png").as_posix())
plt.savefig(script_dir.joinpath("SVG/colorPalette.svg").as_posix())
plt.show()
