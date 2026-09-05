# Python 3
# filename: Plot(1_years_old_and_Specific_Women_Age_Range_Population_Ratio)
# Authors: Betty Botian Zhang, bz2443@nyu.edu
# AI Assistant: Gemini
"""This program plot the the ratio of 1 years old and women's Population 
in an Age Range(e.g. 21-51 in this program). In the program, the year are
substracted by 1, because the plot is attempted to show the the ratio of
newborns and the ratio of women's population in an Age Range such as
20 - 50 for the previous year of the measurement.
Why I did not use the data for newborns that are 0 years old? It is because 
there are huge error in the data for China, I am not sure if it is the case
for all other population data. Also, the people before age 60 did not have a
very low suvival rate after 10 years. I decide that the death rate in one 
year is neglectable. I am currently using this method to measure how many
percent of women in reproductive age (such as 20 - 50) give birth to a child
in one year. I find that this is a strong indicator for the population project.
It tells the reason for population ageing, and could help to predict future
population trends. 
"""
## This code is partcially write by my own. I also past some part of the code from "Plot(%of_people_with_selected_sex_slected_year_in_city).py". This code is write by AI(Gemini).

# Import
import pandas as pd
import matplotlib.pyplot as plt

# Set up condition
selected_people = "Japanese"
selected_nation = "Japan"
women_selected_age_starts = 21
women_selected_age_ends = 51

# read file
input_filename = f"{selected_nation} 1 year old and ({women_selected_age_starts}-{women_selected_age_ends}) Women Ratio(Each Year population sensus).csv"
data = pd.read_csv(input_filename,sep=",")

# Decrease the sensus year to the year of this ratio
data["Year"]-=1
df = pd.DataFrame(data)

## This part is copied from file "Plot(%of_people_with_selected_sex_slected_year_in_city).py", and modified
fig, ax = plt.subplots(figsize=(14, 6))

# Right y-axis: Live in Urban Percentage (Line Chart)
color = "tab:orange"
ax.set_ylabel(f"Percentage", color=color, fontsize=12)
ax.plot(
    df["Year"],
    df["Ratio"],
    color=color,
    linewidth=2,
    marker="o",
    markersize=3,
    label="Percentage",
)
ax.tick_params(axis="y", labelcolor=color)
ax.set_ylim(0, 0.17) 

# Title and layout formatting
plt.title(
    f"{selected_nation} ratio between population born(in 1 year) and ({women_selected_age_starts} - {women_selected_age_ends}) Women Population",
    fontsize=14,
    pad=15,
)
fig.tight_layout()

# Display the plot
output_filename = f"{selected_nation} ratio between population born(in 1 year) and ({women_selected_age_starts} - {women_selected_age_ends}) Women Population.pdf"
plt.savefig(output_filename)
