# ------------------------------------------------------------
# Day 4 Intermediate Assignment
# ------------------------------------------------------------
# This file is the intermediate-level task for the candidate.
# It combines data analysis and simple object-oriented design.

# Import pandas for table-based analysis.
import pandas as pd

# Import Path for safe file handling.
from pathlib import Path

# Define a helper function to load the dataset.
# This keeps the code reusable and easy to read.
def load_dataset(file_path: str) -> pd.DataFrame:
    # Convert the string path into a Path object.
    path = Path(file_path)
    # Read the CSV file into a DataFrame.
    data_frame = pd.read_csv(path)
    # Return the DataFrame to the caller.
    return data_frame


# Define a second function to calculate cost per visit.
def add_cost_per_visit(data_frame: pd.DataFrame) -> pd.DataFrame:
    # Copy the DataFrame so the original data stays untouched.
    working_frame = data_frame.copy()
    # Create a new column for average cost per visit.
    working_frame["cost_per_visit"] = working_frame["total_cost"] / working_frame["visits"]
    # Return the updated frame.
    return working_frame


# Define a function to find high-cost patients.
def find_high_cost_patients(data_frame: pd.DataFrame, limit: float) -> pd.DataFrame:
    # Filter the DataFrame using the given limit.
    high_cost = data_frame[data_frame["total_cost"] > limit]
    # Return only the matching rows.
    return high_cost


# Load the dataset from the file.
df = load_dataset("../data/healthcare_assignment_dataset.csv")

# Add the new calculated metric.
df = add_cost_per_visit(df)

# Print the top 10 high-cost records.
high_cost_df = find_high_cost_patients(df, 2000)
print("High-cost patients:")
print(high_cost_df[["patient_id", "condition", "department", "total_cost", "cost_per_visit"]].head(10))

# Group by department and compute average spend.
summary_by_department = df.groupby("department")["total_cost"].mean().sort_values(ascending=False)
print("\nAverage cost by department:")
print(summary_by_department)

# Create a simple class to represent a patient summary record.
class PatientSummary:
    # The constructor stores the patient data.
    def __init__(self, patient_id: int, condition: str, total_cost: float) -> None:
        self.patient_id = patient_id
        self.condition = condition
        self.total_cost = total_cost

    # A method to show whether the patient is expensive.
    def is_expensive(self) -> bool:
        return self.total_cost > 2500


# Create one object from the class.
patient = PatientSummary(1009, "Hypertension", 2100.25)

# Show the object result.
print("\nPatient summary object:")
print("Patient ID:", patient.patient_id)
print("Condition:", patient.condition)
print("Is expensive?", patient.is_expensive())

# Save the summary output to a file.
OUTPUT_PATH = Path("../output/intermediate_summary.csv")
OUTPUT_PATH.parent.mkdir(exist_ok=True)
summary_by_department.to_csv(OUTPUT_PATH)
print("\nIntermediate summary saved to:", OUTPUT_PATH)
