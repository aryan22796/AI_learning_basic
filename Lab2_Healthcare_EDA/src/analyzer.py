import pandas as pd
import numpy as np

def clean_data(df):
    """Clean healthcare data: remove duplicates, handle missing values."""
    print("[INFO] Cleaning data...")
    
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
    
    print(f"[INFO] Data cleaned. Shape: {df.shape}")
    return df

def group_by_condition(df):
    """Group by condition and calculate statistics."""
    print("[INFO] Grouping by condition...")
    
    grouped = df.groupby('condition').agg({
        'patient_id': 'count',
        'age': ['mean', 'min', 'max'],
        'total_cost': ['sum', 'mean'],
        'visits': 'mean'
    }).round(2)
    
    grouped.columns = ['_'.join(col).strip() for col in grouped.columns]
    return grouped

def group_by_department(df):
    """Group by department and calculate statistics."""
    print("[INFO] Grouping by department...")
    
    grouped = df.groupby('department').agg({
        'patient_id': 'count',
        'total_cost': ['sum', 'mean'],
        'visits': 'mean',
        'age': 'mean'
    }).round(2)
    
    grouped.columns = ['_'.join(col).strip() for col in grouped.columns]
    return grouped

def create_age_groups(df):
    """Create age group categories."""
    print("[INFO] Creating age groups...")
    
    age_bins = [0, 30, 45, 60, 100]
    age_labels = ['Young (0-30)', 'Middle (31-45)', 'Senior (46-60)', 'Elderly (60+)']
    df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)
    return df

def group_by_age_group(df):
    """Group by age group and calculate statistics."""
    grouped = df.groupby('age_group').agg({
        'patient_id': 'count',
        'total_cost': ['mean', 'sum'],
        'visits': 'mean'
    }).round(2)
    
    grouped.columns = ['_'.join(col).strip() for col in grouped.columns]
    return grouped

def pivot_table_condition_dept(df):
    """Create pivot: condition vs department (patient count)."""
    print("[INFO] Creating pivot table (condition vs department)...")
    
    pivot = df.pivot_table(
        index='condition',
        columns='department',
        values='patient_id',
        aggfunc='count',
        fill_value=0
    )
    return pivot

def summary_statistics(df):
    """Generate summary statistics."""
    print("[INFO] Generating summary statistics...")
    
    summary = {
        'Total Unique Patients': df['patient_id'].nunique(),
        'Total Records': len(df),
        'Average Age': round(df['age'].mean(), 2),
        'Total Cost': round(df['total_cost'].sum(), 2),
        'Average Cost per Patient': round(df['total_cost'].mean(), 2),
        'Average Visits per Patient': round(df['visits'].mean(), 2),
        'Total Visits': int(df['visits'].sum()),
        'Max Cost': round(df['total_cost'].max(), 2),
        'Min Cost': round(df['total_cost'].min(), 2),
    }
    return summary
