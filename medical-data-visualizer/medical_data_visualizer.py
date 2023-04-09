import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = np.where(df['weight'] / (df['height'] / 100)**2 > 25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = np.where(df["cholesterol"] == 1, 0, 1)
df["gluc"] = np.where(df["gluc"] == 1, 0, 1)


# Draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(df,
                   id_vars="cardio",
                   var_name="variable",
                   value_vars=[
                     'active', 'alco', 'cholesterol', 'gluc', 'overweight',
                     'smoke'
                   ])

  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

  # Draw the catplot with 'sns.catplot()'
  fig = sns.catplot(data=df_cat,
                    x="variable",
                    kind="count",
                    hue="value",
                    col="cardio").set_axis_labels("variable", "total")

  # Get the figure for the output
  fig = fig.fig

  # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
  # Clean the data
  df_heat = df[(df['ap_lo'] <= df['ap_hi'])
               & (df['height'] >= df['height'].quantile(0.025)) &
               (df['height'] <= df['height'].quantile(0.975)) &
               (df['weight'] >= df['weight'].quantile(0.025)) &
               (df['weight'] <= df['weight'].quantile(0.975))]

  # Calculate the correlation matrix
  corr = df_heat.corr()

  # Generate a mask for the upper triangle
  mask = np.triu(corr)

  # Set up the matplotlib figure
  fig, ax = plt.subplots(figsize=(11, 9))

  # Draw the heatmap with 'sns.heatmap()'
  sns.heatmap(corr,
              mask=mask,
              fmt='.1f',
              vmax=.3,
              linewidths=.5,
              square=True,
              cbar_kws={'shrink': 0.5},
              annot=True,
              center=0)

  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig
