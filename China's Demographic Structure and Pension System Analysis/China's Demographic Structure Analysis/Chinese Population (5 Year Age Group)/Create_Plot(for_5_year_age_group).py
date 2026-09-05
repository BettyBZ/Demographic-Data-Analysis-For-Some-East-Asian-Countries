
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("Chinese_Population_Total_(5-Year_Ages).csv",sep=",")

## Plot the graph
df.columns = df.columns.str.strip()
df = df.fillna(0)

# Set 'Age' as the index for plotting
df.set_index("Age", inplace=True)

# Convert all population columns to numeric (in case of commas or types)
df = df.apply(pd.to_numeric, errors="coerce").fillna(0)

# Plotting a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 12))

# Horizontal bar plotting
df.plot(kind="barh", ax=ax, width=0.8, colormap="viridis")

# Formatting the graph
ax.set_title("Population Distribution by Age Group and Year", fontsize=16, pad=15)
ax.set_xlabel("Population Value", fontsize=12)
ax.set_ylabel("Age Group", fontsize=12)

# Invert y-axis so younger age groups (0-4) appear at the top
ax.invert_yaxis()

# Add legend and grid
ax.legend(title="Year", bbox_to_anchor=(1.05, 1), loc="upper left")
ax.grid(axis="x", linestyle="--", alpha=0.7)

plt.tight_layout()
plot_filename = f"China_Population_1982-2020_Statistic_Comparision_Plote.pdf"
plt.savefig(plot_filename)
print(f"\nTable successfully saved to {plot_filename}")