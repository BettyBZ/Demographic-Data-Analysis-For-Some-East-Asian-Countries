
# Chinese Population Structure Study
# The graph for each single year age group
## Betty Botian Zhang
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("Chinese Population Original Data(from UN).csv",sep=",")

df.columns = df.columns.str.strip()

#Test Code
# Print out Available Data
# print("Available Years:",sorted([str(year) for year in df["Year"].dropna().unique()]),)
# print("Available Area:",df["Area"].unique())
# print("Available Age Groups (sample):",df["Age"].unique()[:10])

# set up conditions 
selected_area = "Total"
selected_sex = "Both Sexes"

# create the filter
df_filtered = df[(df["Area"]==selected_area)&(df["Sex"]==selected_sex)&(~df["Age"].str.contains(" - "))&(~df["Age"].isin(["Unknown", "Total"]))].copy()

# sort the data
def sort_age(age_str):
    age_str = str(age_str).strip()
    if age_str.endswith("+"):
        return int(age_str[:-1])
    try:
        return int(age_str)
    except ValueError:
        return 999

# Apply the age sorting order 
df_filtered["Age_Sort"] = df_filtered["Age"].apply(sort_age)
df_filtered = df_filtered.sort_values("Age_Sort")

# this step fix the sequence after pivoting
sorted_ages_unique = df_filtered["Age"].unique()
df_filtered["Age"] = pd.Categorical(df_filtered["Age"], categories = sorted_ages_unique, ordered=True)
# create the table 
pivot_table = df_filtered.pivot(
    index="Age", columns="Year", values="Value"
)
print(f"\n---- Population Table for {selected_area} Area (Single Age Groups) ---")
print(pivot_table.head(15))

output_filename = f"Chinese_Population_{selected_area}_{selected_sex}_(Single_Year_Ages).csv"
pivot_table.to_csv(output_filename)
print(f"\nTable successfully saved to {output_filename}")
