# Create table for the percentage of Chinese people live in city for each year
# This code in write by my own and revised by AI(Gemini). I learn the pandas system with AI ( Gemini).

# Import
import pandas as pd

# Read file
df = pd.read_csv("Chinese Population Original Data(from UN).csv",sep=",")
df.columns = df.columns.str.strip()

# Set up conditions
selected_sex = "Female"

# Create filter
df_filtered = df[(df["Age"]=="Total")&(df["Sex"]==selected_sex)&(df["Area"].isin(["Urban","Total"]))].copy()

# check and make population numeric
value_col = "Value" if "Value" in df_filtered.columns else df_filtered.columns[-1]
df_filtered[value_col] = pd.to_numeric(df_filtered[value_col],errors="coerce")

# Sort the "Year"
def sort_year(year_str):
    year_str = str(year_str).strip()
    try:
        return int(year_str)
    except ValueError:
        return 999

df_filtered["Year_Sort"] = df_filtered["Year"].apply(sort_year)

# create pivot table
pivot_df = df_filtered.pivot_table(
    index=["Year", "Year_Sort"],
    columns = "Area",
    values=value_col,
    aggfunc="sum"
).reset_index()

# Sort by year
pivot_df = pivot_df.sort_values("Year_Sort")

# create DataFrame
result_df = pd.DataFrame()
result_df["Year"] = pivot_df["Year"]

# set up values and calculations
urban_pop = pivot_df["Urban"] if "Urban" in pivot_df.columns else 0
total_pop = pivot_df["Total"] if "Total" in pivot_df.columns else 1

result_df["Urban_population"] = urban_pop
result_df["Total_population"] = total_pop
result_df["live_in_urban_percentage"] = result_df["Urban_population"]/result_df["Total_population"]

# Create Table
file_name = f"Chinese_Population_{selected_sex}(%_live_in_Urban).csv"
result_df.to_csv(file_name,index=False)
print(f"successfully save to {file_name}")