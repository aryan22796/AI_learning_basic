# Lab 2: Healthcare EDA Project

## Overview
This project demonstrates Day 2 Pandas and NumPy fundamentals in a real lab structure. It performs exploratory data analysis (EDA) on a healthcare dataset, including groupby operations, pivot tables, age group analysis, and generates summary reports.

## Folder Structure
```
Lab2_Healthcare_EDA/
├── data/
│   └── healthcare.csv
├── output/
│   ├── healthcare_eda_report.txt
│   ├── condition_summary.csv
│   ├── department_summary.csv
│   ├── age_group_summary.csv
│   └── pivot_condition_department.csv
├── src/
│   ├── reader.py
│   ├── analyzer.py
│   └── main.py
└── README.md
```

## Files Description

### Data
- `data/healthcare.csv`: Sample healthcare dataset with 30 patient records including:
  - Patient demographics (ID, age, gender)
  - Medical information (condition, department)
  - Visit and cost data

### Source Code
- `src/reader.py`: File I/O operations - read CSV, write reports, export results
- `src/analyzer.py`: Core analysis functions:
  - Data cleaning (removing duplicates, handling missing values)
  - GroupBy operations (condition, department, age groups)
  - Pivot table creation
  - Summary statistics
- `src/main.py`: Orchestration script that coordinates the entire EDA workflow

### Output
- `healthcare_eda_report.txt`: Formatted text report with all findings
- `condition_summary.csv`: Summary statistics grouped by medical condition
- `department_summary.csv`: Summary statistics grouped by department
- `age_group_summary.csv`: Summary statistics grouped by age brackets
- `pivot_condition_department.csv`: Cross-tabulation of condition and department

## Setup

### 1. Ensure Virtual Environment
```bash
cd /Users/aryan/Desktop/AI_learning
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install pandas numpy
```

### 3. Run the Project
```bash
cd Lab2_Healthcare_EDA/src
python main.py
```

## Expected Output

The program will:
1. Load the healthcare CSV data
2. Clean the data (remove duplicates, handle missing values)
3. Create age groups (Young, Middle, Senior, Elderly)
4. Perform groupby analysis by:
   - Medical condition
   - Department
   - Age group
5. Create pivot tables for cross-analysis
6. Generate a comprehensive text report
7. Export all summaries to CSV files

Example output locations:
- Text Report: `../output/healthcare_eda_report.txt`
- CSV Exports: `../output/*.csv`

## Learning Goals

- **Data Loading**: Read CSV files with Pandas
- **Data Cleaning**: Remove duplicates, handle missing values
- **GroupBy Operations**: Aggregate data by multiple dimensions
- **Pivot Tables**: Reorganize data for cross-sectional analysis
- **Age Grouping**: Bin continuous variables into categorical groups
- **Summary Statistics**: Calculate meaningful aggregations
- **Data Export**: Write results to CSV and text formats
- **ETL Pattern**: Implement a complete data pipeline

## Key Pandas Concepts Used

| Concept | Example |
|---------|---------|
| `read_csv()` | Load healthcare data |
| `drop_duplicates()` | Remove duplicate records |
| `fillna()` | Handle missing values |
| `groupby().agg()` | Group and aggregate by condition/department |
| `pivot_table()` | Create cross-tabulations |
| `pd.cut()` | Bin ages into groups |
| `select_dtypes()` | Filter columns by data type |
| `to_csv()` | Export results |

## Sample Analysis Questions Answered

1. **Which medical condition has the highest average cost?**
   → See `condition_summary.csv`

2. **Which department sees the most patients?**
   → See `department_summary.csv`

3. **How does patient cost vary by age group?**
   → See `age_group_summary.csv`

4. **Which condition-department combinations are most common?**
   → See `pivot_condition_department.csv`

5. **What is the overall patient cost profile?**
   → See `healthcare_eda_report.txt` (Summary Statistics)
