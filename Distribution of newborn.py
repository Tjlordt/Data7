#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 11:56:04 2023

@author: tj
"""

import numpy as np
import matplotlib.pyplot as plt

# Read data from the CSV file into an array
datafile = 'data7.csv'
df_new_born = np.loadtxt(datafile, delimiter=',')

# Create another array representing the distribution of newborn weights
# Here we'll use a normal distribution with mean and standard deviation equal to the sample mean and standard deviation
mu = np.mean(df_new_born)
sigma = np.std(df_new_born)
df_normal = np.random.normal(mu, sigma, len(df_new_born))

# Calculate the average weight and the 75th percentile weight
avg_weight = np.mean(df_new_born)
pct_75_weight = np.percentile(df_new_born, 75)

# Calculate the fraction of newborns with a weight greater than or equal to the average weight
X = np.sum(df_new_born >= avg_weight) / len(df_new_born)

# Print the calculated values
print(f"Average Weight: {avg_weight:.2f} kg")
print(f"75th Percentile Weight: {pct_75_weight:.2f} kg")

# Create a histogram of newborn weights
plt.hist(df_new_born, bins='auto', edgecolor='black', color='lightblue', label='Newborn Weights')
plt.xlabel('Newborn Weight (kg)')
plt.ylabel('Frequency')
plt.title('Distribution of Newborn Weights')

# Add vertical lines for average weight and 75th percentile weight
plt.axvline(avg_weight, color='red', linestyle='dashed', linewidth=1, label=f'Average Weight = {avg_weight:.2f} kg')
plt.axvline(pct_75_weight, color='green', linestyle='dashed', linewidth=1, label=f'75th Percentile Weight = {pct_75_weight:.2f} kg')

# Add vertical line for fraction X
plt.axvline(avg_weight * 1.1, color='none', linestyle='dashed', linewidth=1, label=f'Fraction std(X) = {X:.2f}')

# Add a legend and show the plot
plt.legend(loc='upper left')
plt.show()
