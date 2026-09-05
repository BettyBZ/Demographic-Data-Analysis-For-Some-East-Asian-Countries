#Chinese Population Structure Study
## Betty Botian Zhang
# each age range for 5 years it does not contain people's age "100+"
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
df_filtered = df[(df["Area"]==selected_area)&(df["Sex"]==selected_sex)&(df["Age"].str.contains(" - "))].copy()

# sort the data
def sort_age_ranges(age_str):
    age_str = str(age_str).strip()
    if " - " in age_str:
        try:
            return int(age_str.split(" - ")[0])
        except ValueError:
            return 999
    return 999

# Apply the age sorting order 
df_filtered["Age_Sort"] = df_filtered["Age"].apply(sort_age_ranges)
df_filtered = df_filtered.sort_values("Age_Sort")

# this step fix the sequence after pivoting
sorted_ages_unique = df_filtered["Age"].unique()
df_filtered["Age"] = pd.Categorical(df_filtered["Age"], categories = sorted_ages_unique, ordered=True)
# create the table 
pivot_table = df_filtered.pivot(
    index="Age", columns="Year", values="Value"
)
print(f"\n---- Population Table for {selected_area} Area (5-Year Age Groups) ---")
print(pivot_table.head(10))

output_filename = f"Chinese_Population_{selected_area}_{selected_sex}_(5-Year_Ages).csv"
pivot_table.to_csv(output_filename)
print(f"\nTable successfully saved to {output_filename}")

