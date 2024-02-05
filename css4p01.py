# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 23:43:09 2024

@author: sammi
"""

import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/sammi/OneDrive/Documents/2024/CHPC/movie_dataset.csv")

# Display basic information about the dataset
print(df.info())

# Handle missing values
# You can choose to fill missing values or drop columns/rows based on your analysis
# Example of filling missing values with mean for numeric columns
df.fillna(df.mean(), inplace=True)

# Rename columns to remove spaces
df.columns = df.columns.str.replace(' ', '_')

# Perform exploratory data analysis (EDA)
# Example: Display summary statistics
print(df.describe())

# Example: Display unique values in the 'Genre' column
print(df['Genre'].unique())

# Example: Plot a histogram of the IMDb ratings
df['IMDb_Rating'].plot(kind='hist', bins=20, title='IMDb Ratings Histogram')

# Save the cleaned dataset if needed
# df.to_csv("cleaned_movie_dataset.csv", index=False)

highest_rated_movie = df.loc[df['Rating'].idxmax()]

# Print the details of the highest-rated movie
print("Highest Rated Movie:")
print(highest_rated_movie)

# Assuming 'Revenue' is the column containing the revenue information
# Fill missing values with 0 before calculating the average
average_revenue = df['Revenue'].fillna(0).mean()

# Print the average revenue
print("Average Revenue of All Movies:", average_revenue)



