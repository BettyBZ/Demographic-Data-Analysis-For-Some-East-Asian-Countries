# Man : Women in Urban Area
import pandas as pd
df = pd.read_csv("Chinese Population Original Data(from UN).csv",sep=",")
df.columns = df.columns.str.strip()

# create table
selected_area = "Urban"
selected_year = "1982"
df_filtered = df[(df["Area"]==selected_area)&(df["Sex"].isin(["Male","Female"]))&(df["Age"].str.contains(" - "))&(df["Year"]==selected_year)]
pivot_table = df_filtered.pivot_log = df_filtered.pivot(
    index="Age", columns="Sex", values="Value"
)

print(f"\n---- Male VS Female in {selected_area} Area {selected_year} 5-year Age Group ----")
print(pivot_table.head())
output_filename = f"Chinese_Population_{selected_area}_{selected_year}_Male:Female_(5-Year_Ages).csv"
pivot_table.to_csv(output_filename)
print(f"\nTable successfully saved to {output_filename}")