import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(8, 8))

    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope_from_1880, intercept_from_1880, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_from_1880_to_2050 = np.arange(df['Year'].min(), 2051)
    predicted_sea_level_since_1880 = slope_from_1880 * years_from_1880_to_2050 + intercept_from_1880

    ax.plot(
        years_from_1880_to_2050,
        predicted_sea_level_since_1880,
        color='red'
    )

    # Create second line of best fit
    df_from_2000 = df[df['Year'] >= 2000]
    slope_from_2000, intercept_from_2000, _, _, _ = linregress(df_from_2000['Year'], df_from_2000['CSIRO Adjusted Sea Level'])
    years_from_2000_to_2050 = np.arange(df_from_2000['Year'].min(), 2051)
    predicted_sea_level_since_2000 = slope_from_2000 * years_from_2000_to_2050 + intercept_from_2000

    ax.plot(
        years_from_2000_to_2050,
        predicted_sea_level_since_2000,
        color='purple'
    )

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()