import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv("epa-sea-level.csv")

  # Create scatter plot
  plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

  # Create first line of best fit
  line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  x1 = np.arange(df['Year'].min(), 2051)
  y1 = x1 * line1.slope + line1.intercept
  plt.plot(x1, y1)

  # Create second line of best fit
  new_df = df[df['Year'] >= 2000]
  line2 = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
  x2 = np.arange(2000, 2051)
  y2 = x2 * line2.slope + line2.intercept
  plt.plot(x2, y2)

  # Add labels and title
  plt.title("Rise in Sea Level")
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
