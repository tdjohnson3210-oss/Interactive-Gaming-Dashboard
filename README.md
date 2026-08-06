# (DSC527) Interactive Local Dashboard with Simulated Real-Time Data – Part 1
Author: Tracey Johnson/
Date: 08-05-2026/
Python version 3.13

## Overview
This project demonstrates how to handle large datasets through loading, exploratory data analysis, and visualization. The goal is to choose a large dataset (500K–1M rows) and identify meaningful trends. This notebook will use libraries and data formats designed to reduce time and memory usage, allowing for more efficient processing and creative analytical applications.

Part 2 of this project focuses on measuring the efficiency of loading large datasets in different formats (CSV vs Parquet) and performing exploratory data analysis (EDA) on the NBA dataset. In addition, the notebook will include profiling of load times, CPU usage, and memory usage for both formats, as well as visualizations to uncover insights from the data.

## Installation
To run this notebook, ensure you have Python 3.13 installed along with the following libraries:
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import kagglehub as kh

## Usage
1. download the dataset from Kaggle and place it in the appropriate directory.
2. create a parquet version of the dataset using the provided code.
3. preprocess the data, perform EDA, and generate visualizations as demonstrated in the notebook.
4. analyze the efficiency profiling results to compare CSV and Parquet formats.

# Features
id_cols = ["game_id", "teamname", "playername"]
binary_cols = ["dnp_flag", "starter_flag"]
stat_cols = [
    "mp", "fg", "fga", "3p", "3pa", "ft", "fta",
    "orb", "drb", "trb", "ast", "stl", "blk",
    "tov", "pf", "pts", "+/-"
]

## License
The NBA dataset is sourced from Kaggle and is subject to its licensing terms. Please refer to the original dataset source for any usage restrictions.

Source: https://www.kaggle.com/datasets/patrickhallila1994/nba-data-from-basketball-reference/data