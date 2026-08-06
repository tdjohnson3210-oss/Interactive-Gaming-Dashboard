# (DSC527) Interactive Local Dashboard with Simulated Real-Time Data – Part 1
Author: Tracey Johnson/
Date: 08-05-2026/
Python version 3.13

# LIVE DASHBOARD APPLICATION LINK:
https://interactive-gaming-dashboard-vioxonhmyw722jerr6arx7.streamlit.app/

## Overview
This project demonstrates how to generate a large synthetic gaming dataset (500K–1M rows) and use it to explore player behavior, game performance metrics, and interactive visualizations. The dashboard simulates real‑time updates, making it easy to examine trends in gameplay, engagement, and in‑game actions.

The project also includes building an interactive Streamlit app powered by the synthetic dataset, featuring dynamic charts, filters, and simulated refresh behavior. The dataset itself mimics realistic gaming telemetry, player sessions, purchases, performance stats, and game attributes, allowing scalable experimentation.

## Installation
To run this notebook, ensure you have Python 3.13 installed along with the following libraries:
- `import pandas as pd`
- `import numpy as np`
- `import plotly.express as px`
- `import streamlit as st`


## Usage
1. Generate or load the synthetic gaming dataset using the provided code.
2. Perform preprocessing, EDA, and visualization using the notebook and Python documents.
3. Use Streamlit to launch the interactive dashboard locally.
4. Deploy the dashboard to Streamlit Cloud for public access.

## Project Structure
- `Overview.py`: Main Streamlit application script for the interactive dashboard.
- `2_Drill_Down.py`: Python script for detailed analysis and drill-down visualizations.
- `Interactive Local Dashboard with Simulated Real-Time Data – Part 1.ipynb`: Jupyter notebook containing code for dataset generation and exploratory analysis.
- `README.md`: Project documentation and instructions.
- `requirements.txt`: List of required Python packages for the project.
- `synthetic_gaming_dataset.csv`: The generated synthetic dataset (if saved).

## Synthetic Dataset Features
Column names and data types:
game_genre                   category
game_theme                   category
player_perspective           category
game_mode                    category
age_rating                      int64
supported_platforms             int64
release_year                    int64
rating_score                  float64
rating_count                    int64
time_stamp             datetime64[us]
dtype: object

## Dashboard Features
- Interactive visualizations of game ratings, genres, and player perspectives.
- Real-time simulation of data updates and refreshes.
- Filters for exploring specific game attributes.

## License
This project uses a synthetic dataset, meaning no external licensing restrictions apply.
