# Create a Table that shows the % of people live in city for each age group in slected Year
# The code is revised by AI, but write by my own. 

# This part of code is write by me.
# Import
import pandas as pd

# Read file
df = pd.read_csv("Chinese Population Original Data(from UN).csv",sep=",")
df.columns = df.columns.str.strip()

# Only This part from AI(Gemini), the revision is here. 
for col in ["Sex", "Area", "Year"]:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()

# start the part I write the code by my own, it is a revision of by program "Table (%of_people_with_selected_sex_in_City_Each_Year).py"
# Set up conditions
selected_sex = "Both Sexes"
selected_year = "1982"

# Create filter
df_filtered = df[(df["Year"]==selected_year)&(df["Sex"]==selected_sex)&(df["Area"].isin(["Urban","Total"]))&(~df["Age"].str.contains(r" - |Total", regex=True))].copy()

# check and make population numeric
value_col = "Value" if "Value" in df_filtered.columns else df_filtered.columns[-1]
df_filtered[value_col] = pd.to_numeric(df_filtered[value_col],errors="coerce")

# Sort the "Year"
def sort_age(age_str):
    age_str = str(age_str).strip()
    if age_str.endswith("+"):
            return int(age_str[:-1])
    try:
        return int(age_str)
    except ValueError:
        return 999

df_filtered["Age_Sort"] = df_filtered["Age"].apply(sort_age)

# create pivot table
pivot_df = df_filtered.pivot_table(
    index=["Age", "Age_Sort"],
    columns = "Area",
    values=value_col, 
    aggfunc="sum"
).reset_index()

# Sort by year
pivot_df = pivot_df.sort_values("Age_Sort")

# create DataFrame
result_df = pd.DataFrame()
result_df["Age"] = pivot_df["Age"]

# set up values and calculations
urban_pop = pivot_df["Urban"] if "Urban" in pivot_df.columns else 0
total_pop = pivot_df["Total"] if "Total" in pivot_df.columns else 1

result_df["Urban_population"] = urban_pop
result_df["Total_population"] = total_pop
result_df["live_in_urban_percentage"] = result_df["Urban_population"]/result_df["Total_population"]

# Create Table
file_name = f"Chinese_Population_{selected_year}_{selected_sex}(%_live_in_Urban).csv"
result_df.to_csv(file_name,index=False)
print(f"successfully save to {file_name}")