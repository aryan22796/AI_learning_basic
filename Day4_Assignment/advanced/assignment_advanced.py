# ------------------------------------------------------------
# Day 4 Advanced Assignment
# ------------------------------------------------------------
# This file is the advanced-level task for the candidate.
# It uses OOP, type hints, and a small analytics pipeline.

# Import pandas for advanced analytics work.
import pandas as pd

# Import Path for safe path management.
from pathlib import Path

# Import dataclass to create cleaner record-style classes.
from dataclasses import dataclass


# Define a singleton-like configuration object for the pipeline.
class PipelineConfig:
    # Keep one shared instance for the output folder and file encoding.
    _instance = None

    def __new__(cls):
        # If no object exists, create one.
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.output_dir = "../output"
            cls._instance.encoding = "utf-8"
        # Return the same object every time.
        return cls._instance


# Define a dataclass for patient analytics records.
@dataclass
class PatientAnalyticsRecord:
    # Type hints define what each field stores.
    patient_id: int
    condition: str
    department: str
    total_cost: float
    risk_score: int

    # A method to mark risk level.
    def risk_level(self) -> str:
        # Use a simple threshold to decide the risk label.
        if self.risk_score >= 80:
            return "High"
        if self.risk_score >= 50:
            return "Medium"
        return "Low"


# Define a base class for analytics.
class BaseAnalytics:
    # Constructor stores the file path.
    def __init__(self, file_path: str) -> None:
        self.file_path = Path(file_path)

    # A method to load the dataset.
    def load(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path)


# Define a subclass that adds business rules.
class PatientAnalytics(BaseAnalytics):
    # Constructor calls the parent constructor.
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    # A method to compute cost per visit.
    def add_cost_per_visit(self, data_frame: pd.DataFrame) -> pd.DataFrame:
        working_frame = data_frame.copy()
        working_frame["cost_per_visit"] = working_frame["total_cost"] / working_frame["visits"]
        return working_frame

    # A method to create a summary by department.
    def department_summary(self, data_frame: pd.DataFrame) -> pd.DataFrame:
        summary = data_frame.groupby("department").agg(
            patients=("patient_id", "count"),
            avg_cost=("total_cost", "mean"),
            avg_risk=("risk_score", "mean"),
        )
        return summary.sort_values("avg_cost", ascending=False)

    # A method to export the summary as CSV.
    def export_summary(self, summary: pd.DataFrame, filename: str) -> None:
        config = PipelineConfig()
        output_dir = Path(config.output_dir)
        output_dir.mkdir(exist_ok=True)
        output_file = output_dir / filename
        summary.to_csv(output_file)
        print("Advanced report exported to:", output_file)


# Create the analytics object.
analytics = PatientAnalytics("../data/healthcare_assignment_dataset.csv")

# Load the data.
raw_df = analytics.load()

# Add the cost per visit metric.
prepared_df = analytics.add_cost_per_visit(raw_df)

# Create the summary table.
summary_df = analytics.department_summary(prepared_df)
print("Department summary:")
print(summary_df)

# Build one dataclass-based analytics row.
record = PatientAnalyticsRecord(1020, "Asthma", "Pulmonology", 1900.25, 45)
print("\nDataclass record:")
print(record)
print("Risk level:", record.risk_level())

# Export the final summary.
analytics.export_summary(summary_df, "advanced_department_summary.csv")
