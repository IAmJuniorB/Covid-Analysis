import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('filtered_deaths.csv')

# Convert 'Data As Of' column to datetime and set date
df['Data As Of'] = pd.to_datetime(df['Data As Of'])
current_date = df['Data As Of'].max()
df = df[df['Data As Of'] <= current_date]

# Pivot the DataFrame to have months as rows, years as columns, and Influenza Deaths as values
pivot_df = df.pivot('Month', 'Year', 'Influenza Deaths')

# Sort columns
pivot_df = pivot_df.reindex(sorted(pivot_df.columns), axis=1)

# Convert indices to strings
pivot_df.index = pivot_df.index.astype(str)
pivot_df.columns = pivot_df.columns.astype(str)

# Generate a custom colormap
colors = sns.color_palette("YlOrRd", n_colors=9)
cmap = sns.color_palette(colors, as_cmap=True)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Generate the heatmap
sns.heatmap(pivot_df, annot=True, fmt='.0f', cmap=cmap, xticklabels='auto', yticklabels='auto',
            cbar=True, ax=ax, annot_kws={"size": 10, "weight": "bold", "color": "black"})

# Title
cbar = ax.collections[0].colorbar
cbar.set_label('Influenza Deaths', rotation=270, labelpad=20)

# Highest number of Influenza deaths
max_value = pivot_df.max().max()
max_indices = pivot_df.stack().idxmax()
max_month, max_year = max_indices[0], max_indices[1]

# Highlight highest number of Influenza deaths
ax.add_patch(plt.Rectangle((pivot_df.columns.get_loc(max_year), pivot_df.index.get_loc(max_month)), 1, 1,
                            fill=False, edgecolor='blue', lw=2))

# Customize axis labels
ax.set_xlabel('Year')
ax.set_ylabel('Month')

# Customize grid
ax.grid(True, linewidth=0.5, linestyle='dashed', color='gray')

# Title and subtitle
ax.set_title(f'Monthly Influenza Deaths as of {current_date.strftime("%m/%d/%Y")}', fontsize=16, pad=30)
ax.text(0.5, 1.02, f'Highest Monthly Influenza Deaths: {int(max_value)} in {max_month} {max_year}',
        ha='center', va='center', fontsize=12, transform=ax.transAxes)

# Future months
for i, month in enumerate(pivot_df.index):
    for j, year in enumerate(pivot_df.columns):
        if datetime(int(year), int(month), 1) > current_date:
            ax.text(j + 0.5, i + 0.5, 'Future', ha='center', va='center', fontsize=12, color='gray')

# Total deaths
total_deaths = pivot_df.sum().sum()
ax.text(len(pivot_df.columns) + -2, 14.0, f'Total Deaths: {int(total_deaths)}',
        ha='center', va='bottom', fontsize=8, color='black')

# Name and sources
ax.text(4.0, 14.5, 'Joe Bonfanti Jr', ha='center', fontsize=8)
ax.text(4.0, 14.75, 'Source:', ha='center', fontsize=6)
ax.text(4.0, 15.0, 'CDC: https://data.cdc.gov/NCHS/Provisional-COVID-19-Deaths-by-Sex-and-Age/9bhg-hcku', ha='center', fontsize=6)

plt.xticks(rotation=45)
plt.yticks(rotation=0)

plt.tight_layout()
plt.show()
