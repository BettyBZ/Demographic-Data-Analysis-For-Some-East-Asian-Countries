# Table(1_years_old_and_(21-51)_Women_ratio)
"""In this study, we are trying to measure the change of 
women's likelyhood of giving birth in one year when they
are at the age that is likely to give birth.
We intentionally use the data of people that was one years 
old when taking the population sensus. This is Because the 
number more acuratly measures the people that is born in one
 year. As a consequence, the result would be the ratio for 
 the year before population sensus.
Then, we assume that women are likely to give birth between
20 to 50 year old. As a result, we need to add up the 
women's population between 21 and 51 years old in the 
population sensus.
"""
# This code is write by my own. AI(Gemini) fixed the problem of not reading values on line 67. 

# Import
import pandas as pd

#Set up conditions
selected_people = "Chinese"
selected_nation = "China"
women_selected_age_starts = 21
women_selected_age_ends = 46


## Create table for people that is 1 years old in each of the stastic year
#read file
input_filename = f"{selected_people} Population Original Data(from UN).csv"
df = pd.read_csv(input_filename,sep=",")

#create filter for 1 years old population
df_filtered_table1= df[(df["Sex"]=="Both Sexes")&(df["Age"]=="1")&(df["Area"]=="Total")].copy()

# create Table 1
pivot_table_1= df_filtered_table1.pivot_table(
    index="Year",columns="Age",values="Value"
)

# Save the table to CSV form
output_filename_1 = f"{selected_nation} 1 Years Old in Population Sensus(Each Year).csv"
pivot_table_1.to_csv(output_filename_1)
print(f"\nSucessfully Save file {output_filename_1}")

## Create table for women's age between selected age range for each of the stastic year.(Also, show sum in this table). 
df["Age"] = pd.to_numeric(df["Age"], errors = "coerce")
df_filtered_table2 = df[(df["Sex"]=="Female")&(df["Area"]=="Total")&(df["Age"]>women_selected_age_starts-1)&(df["Age"]<women_selected_age_ends+1)].copy()

# Create Table 2
pivot_table_2 = df_filtered_table2.pivot_table(
    index = "Year", columns="Age", values = "Value"
)

#Save the table to CSV form
output_filename_2 = f"{selected_nation} Women population in ({women_selected_age_starts}-{women_selected_age_ends}) group(Each Year population sensus).csv"
pivot_table_2.to_csv(output_filename_2)
print(f"\nSucessfully Save file {output_filename_2}")

# Create Data Frame for Table 2
result_df_2 = pd.DataFrame()
result_df_2["Year"] = pivot_table_2.index
result_df_2["1 years old"] = pivot_table_1["1"].values
result_df_2["Population Sum"]= 0
# Put the women bwteen 21 to 51 into new data frame for Table 2
for num in range(women_selected_age_starts,women_selected_age_ends+1,1):
    if num in pivot_table_2.columns:
        result_df_2["Population Sum"]+=pivot_table_2[num].fillna(0).values

result_df_2["Ratio"] = result_df_2["1 years old"]/result_df_2["Population Sum"]
output_filename_3 = f"{selected_nation} 1 year old and ({women_selected_age_starts}-{women_selected_age_ends}) Women Ratio(Each Year population sensus).csv"
result_df_2.to_csv(output_filename_3)
print(f"\nSucessfully Save file {output_filename_2}")
