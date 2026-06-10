# ------------------------------------------------------------
# Day 4 Basic Assignment
# ------------------------------------------------------------
# This file is the beginner-level task for the candidate.
# The goal is to load the dataset and perform simple analysis.

# Import pandas to work with table-style data.
import pandas as pd

# Import Path from pathlib so file paths work reliably.
from pathlib import Path

# Build the full path to the dataset.
# This uses the project folder structure of this workspace.
DATA_PATH = Path("../data/healthcare_assignment_dataset.csv")

# Load the CSV file into a DataFrame.
# A DataFrame is like an Excel table in Python.
df = pd.read_csv(DATA_PATH)

# Print a short message to tell the user what is happening.
print("Basic assignment started.")

# Display the first 5 rows of the dataset.
print(df.head())

# Print the number of rows and columns in the dataset.
print("Shape:", df.shape)

# Calculate average age of all patients.
avg_age = df["age"].mean()
print("Average age:", round(avg_age, 2))

# Calculate average cost per patient.
avg_cost = df["total_cost"].mean()
print("Average total cost:", round(avg_cost, 2))

# Create a new column called cost_per_visit.
# This shows how much each patient spends on average per visit.
df["cost_per_visit"] = df["total_cost"] / df["visits"]

# Print the updated dataset with the new column.
print(df[["patient_id", "condition", "visits", "total_cost", "cost_per_visit"]].head())

# Save the updated table into a new CSV file.
OUTPUT_PATH = Path("../output/basic_report.csv")
OUTPUT_PATH.parent.mkdir(exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)

# Print the saved file location.
print("Basic report saved to:", OUTPUT_PATH)
