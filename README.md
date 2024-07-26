# Netflix Data Exploration and Visualization

A comprehensive analysis and visualization of Netflix data using Python libraries. This project includes data cleaning, exploratory data analysis, and various visualizations to uncover trends and patterns in the Netflix dataset up to 2021.

## Table of Contents
- [Introduction](#introduction)
- [Data Source](#data-source)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Results](#results)

## Introduction
This project aims to explore the Netflix dataset to uncover insights and trends. The analysis involves data cleaning, exploratory data analysis (EDA), and creating visualizations to represent the findings.

## Data Source
The dataset used in this project is sourced from [Scaler](https://www.scaler.com).

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Features
- Data Cleaning
- Exploratory Data Analysis
- Visualization of Trends and Patterns

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/netflix-data-exploration.git
    ```
2. Navigate to the project directory:
    ```sh
    cd netflix-data-exploration
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Results

### Insights

#### Movie/Show Ratings
Based on the interpretation of the data, the distribution of movie/show ratings is as follows:
- **TV-MA**: 1822
- **TV-14**: 1214
- **R**: 778
- **PG-13**: 470
- **TV-PG**: 431
- **PG**: 275
- **TV-G**: 84
- **TV-Y**: 76
- **TV-Y7**: 76
- **NR**: 58
- **G**: 40
- **TV-Y7-FV**: 3
- **UR**: 3
- **NC-17**: 2

#### Unique Directors
The dataset contains 4528 unique directors. Some of the most prolific directors are:
- **Rajiv Chilaka**: 19
- **Raúl Campos, Jan Suter**: 18
- **Marcus Raboy**: 16
- **Suhas Kadav**: 16
- **Jay Karas**: 14

#### Unique Shows and Movies
- **Number of Unique Shows**: 2676
- **Number of Unique Movies**: 6131

#### Production by Country (in order of year released)
The number of shows/movies produced by a country, ordered by the year they were released:
- **United States**: 2818
- **India**: 972
- **United Kingdom**: 419
- **Japan**: 245
- **South Korea**: 199
  
#### Popular Durations in Shows/Movies
The most common durations for shows/movies are:
- **1 Season**: 1793
- **2 Seasons**: 425
- **3 Seasons**: 199
- **90 min**: 152
- **94 min**: 146

#### Most Movie/Show Producing Countries
Countries that produce the most shows/movies:
- **United States**: 2818
- **India**: 972
- **United Kingdom**: 419
- **Japan**: 245
- **South Korea**: 199

