import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Define a color palette suitable for academic papers
# Use colors that are colorblind-friendly and have good contrast

sns.set_style("whitegrid")  # Add grid to the plot
# plt.yticks([0, 20, 40, 60, 80, 100])  # Ensure grid lines are shown at all 5 values

sns.set_palette(sns.color_palette(["#1f77b4", "#ff7f0e"]))  # Blue and Orange
#these values are added by manually looking at the number of rows in the csv files
data = {
    'Name': ['All Paper', 'Machine Learning', 'Neural Networks', 'TinyML'],
    'Value_local': [(1942 / 1942) * 100, (801 / 1942) * 100, (466 / 1942) * 100, (32 / 1942) * 100],
    'Value_international': [(4684 / 4684) * 100, (1815 / 4684) * 100, (1360 / 4684) * 100, (596 / 4684) * 100]
}
# sns.set_palette(sns.color_palette(['b', 'r']))  # Set colors using shorthand notation
# sns.set_palette(sns.color_palette(["#3498db", "#e74c3c"]))  # Set custom colors for the bars
df = pd.DataFrame(data)
# Add a new legend entry
legend_labels = {'Value_local': 'Local Conferences', 'Value_international': 'International Conferences'}
df.rename(columns=legend_labels, inplace=True)
plt.figure(figsize=(10, 6))
df_melted = df.melt(id_vars='Name', var_name='Category', value_name='Value')
# Add edge around the bars
sns.barplot(data=df_melted, x='Name', y='Value', hue='Category', edgecolor='black')
# Map specific colors to each category
# category_colors = {'Local Conferences': '#3498db', 'International Conferences': '#e74c3c'}

# df_melted['Color'] = df_melted['Category'].map(category_colors)

# sns.barplot(data=df_melted, x='Name', y='Value', hue='Category')
plt.title('Distribution of research papers in Local and International Conferences since 2020')
plt.xlabel('Type of Paper')
plt.ylabel('Number of Papers (Normalized)')
plt.legend()
plt.show()
a =1
