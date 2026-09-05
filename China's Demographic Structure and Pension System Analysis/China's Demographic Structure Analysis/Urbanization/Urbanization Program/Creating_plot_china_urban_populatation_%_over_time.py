# Creating a plot of china urban population percentage over time
## This ploting code is written by AI mostly
import pandas as pd
import matplotlib.pyplot as plt

# make "Sex" selection (code write by my own)
selected_sex = "Male"
input_filename = f"Chinese_Population_{selected_sex}(%_live_in_Urban).csv"
df = pd.read_csv(input_filename,sep=",")

#Code past from Gemini starts here with my own revision only at line 13
plt.figure(figsize=(8, 5))
plt.plot(df["Year"], df["live_in_urban_percentage"], marker="o", linestyle="-", color="b", label="Urban Population %")

# Add titles and labels
plt.title(f"China {selected_sex} Urban Population Percentage Over Time")
plt.xlabel("Year")
plt.ylabel("Percentage (%)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
# The past code ends here

# my own code here
# Save the graph
output_filename = f"China {selected_sex} Urban population percentage overtime.pdf"
plt.savefig(output_filename)