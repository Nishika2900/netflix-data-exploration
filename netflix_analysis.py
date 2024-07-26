#!/usr/bin/env python
# coding: utf-8

import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/000/940/original/netflix.csv')

# Display the first few rows of the dataset
print(data.head())

# Display data description
print(data.describe(include='all'))

# Value counts of 'duration'
print(data['duration'].value_counts())

# Value counts of 'country'
print(data['country'].value_counts())

# Count of empty values
print(data.isnull().sum())

# Drop rows with missing 'country' values
country_data = data.dropna(subset=['country'], how='any')
print(country_data.isnull().sum())  # no empty country values

# Rating counts
ratings = country_data.groupby('rating').size().reset_index(name='count')
print(ratings)

# Duration counts
duration = country_data.groupby(['duration']).size().reset_index(name='count')
print(duration)

# Separate data for seasons
season_data = duration[duration['duration'].str.contains('Season')]
print(season_data)

# Separate data for durations in minutes
min_data = duration[~duration['duration'].str.contains('Season')]
min_data['time'] = min_data['duration'].str.split(' min').str[0].astype(int)
print(min_data)

# Convert 'release_year' to datetime and extract year
data['release_year'] = pd.to_datetime(data['release_year'], errors='coerce').dt.year
print(data.head())

# Separate data for TV Shows and Movies
shows = data[data['type'] == 'TV Show']
movies = data[data['type'] == 'Movie']

# Check for missing values in shows and movies
print(shows.isnull().sum())
print(movies.isnull().sum())

# Number of TV Shows and Movies
print(f"Number of TV Shows: {shows.shape[0]}")
print(f"Number of Movies: {movies.shape[0]}")

# FacetGrid plot by release year and director
g = sns.FacetGrid(data, col="release_year", hue="director")
g.map(sns.lineplot, "type", "release_year", alpha=1)
g.add_legend()

# Convert 'date_added' to datetime
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
print(data.head())

# Sort and count values by release year and country
print(data.sort_values(by='release_year').value_counts('country'))

# Value counts of directors
print(data['director'].value_counts())
