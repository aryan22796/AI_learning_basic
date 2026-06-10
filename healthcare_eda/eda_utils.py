import pandas as pd
import numpy as np
from pathlib import Path

def load_data(filepath):
    \"\"\"Load healthcare data from CSV.\"\"\"
    df = pd.read_csv(filepath)
    return df

def clean_data(df):
    \"\"\"Clean healthcare data: remove duplicates, handle missing values.\"\"\"
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Fill missing values in numerical columns with median
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    for col in numerical_cols:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].median(), inplace=True)
    
    # Fill missing values in categorical columns with mode
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].mode()[0], inplace=True)
    
    return df

def analyze_by_condition(df):
    \"\"\"Group by condition and calculate statistics.\"\"\"
    analysis = df.groupby('condition').agg({
        'patient_id': 'count',
        'age': ['mean', 'min', 'max'],
        'total_cost': ['sum', 'mean', 'max'],
        'visits': ['mean', 'sum']
    }).round(2)
    
    analysis.columns = ['_'.join(col).strip() for col in analysis.columns]
    return analysis

def analyze_by_department(df):
    \"\"\"Group by department and calculate statistics.\"\"\"
    analysis = df.groupby('department').agg({
        'patient_id': 'count',
        'total_cost': ['sum', 'mean'],
        'visits': 'mean',
        'age': 'mean'
    }).round(2)
    
    analysis.columns = ['_'.join(col).strip() for col in analysis.columns]
    return analysis

def create_age_groups(df):
    \"\"\"Create age group categories.\"\"\"
    age_bins = [0, 30, 45, 60, 100]
    age_labels = ['Young (0-30)', 'Middle (31-45)', 'Senior (46-60)', 'Elderly (60+)']
    df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)
    return df

def analyze_by_age_group(df):
    \"\"\"Group by age group and calculate statistics.\"\"\"
    analysis = df.groupby('age_group').agg({
        'patient_id': 'count',
        'total_cost': 'mean',
        'visits': 'mean'
    }).round(2)
    
    analysis.columns = ['patient_count', 'avg_cost', 'avg_visits']
    return analysis

def pivot_condition_department(df):
    \"\"\"Create pivot table: condition vs department (patient count).\"\"\"
    pivot = df.pivot_table(
        index='condition',
        columns='department',
        values='patient_id',
        aggfunc='count',
        fill_value=0
    )
    return pivot

def pivot_cost_by_condition_department(df):
    \"\"\"Create pivot table: average cost by condition and department.\"\"\"
    pivot = df.pivot_table(
        index='condition',
        columns='department',
        values='total_cost',
        aggfunc='mean'
    ).round(2)
    return pivot

def generate_summary_report(df):
    \"\"\"Generate a summary report of the healthcare data.\"\"\"
    report = {
        'total_patients': df['patient_id'].nunique(),
        'total_records': len(df),
        'avg_age': round(df['age'].mean(), 1),
        'total_cost': round(df['total_cost'].sum(), 2),
        'avg_cost_per_patient': round(df['total_cost'].mean(), 2),
        'avg_visits': round(df['visits'].mean(), 2),
        'conditions': list(df['condition'].unique()),
        'departments': list(df['department'].unique()),
        'top_conditions': df['condition'].value_counts().head(3).to_dict(),
        'top_departments_by_cost': df.groupby('department')['total_cost'].sum().sort_values(ascending=False).head(3).to_dict()
    }
    return report

def export_summary(df, output_dir):
    \"\"\"Export summary statistics to CSV files.\"\"\"
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Export condition summary
    condition_summary = analyze_by_condition(df)
    condition_summary.to_csv(output_path / 'condition_summary.csv')
    
    # Export department summary
    dept_summary = analyze_by_department(df)
    dept_summary.to_csv(output_path / 'department_summary.csv')
    
    # Export age group summary
    age_group_summary = analyze_by_age_group(df)
    age_group_summary.to_csv(output_path / 'age_group_summary.csv')
    
    # Export pivot tables
    pivot_cond_dept = pivot_condition_department(df)
    pivot_cond_dept.to_csv(output_path / 'pivot_condition_department.csv')
    
    pivot_cost = pivot_cost_by_condition_department(df)
    pivot_cost.to_csv(output_path / 'pivot_cost_condition_department.csv')
    
    return [
        'condition_summary.csv',
        'department_summary.csv',
        'age_group_summary.csv',
        'pivot_condition_department.csv',
        'pivot_cost_condition_department.csv'
    ]
