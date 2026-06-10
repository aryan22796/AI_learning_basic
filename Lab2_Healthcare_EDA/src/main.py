#!/usr/bin/env python3
"""
Healthcare EDA Lab - Main Orchestration
Loads healthcare data, performs EDA, and generates reports
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from reader import read_csv, write_report, export_csv
from analyzer import (
    clean_data,
    group_by_condition,
    group_by_department,
    create_age_groups,
    group_by_age_group,
    pivot_table_condition_dept,
    summary_statistics
)

def main():
    """Main execution function."""
    
    # Define paths
    base_dir = Path(__file__).parent.parent
    data_file = base_dir / 'data' / 'healthcare.csv'
    output_dir = base_dir / 'output'
    
    print("="*60)
    print("HEALTHCARE EXPLORATORY DATA ANALYSIS (EDA) LAB")
    print("="*60)
    
    # 1. Load data
    print("\n[STEP 1] Loading data...")
    df = read_csv(str(data_file))
    if df is None:
        print("[ERROR] Failed to load data. Exiting.")
        return
    
    # 2. Clean data
    print("\n[STEP 2] Cleaning data...")
    df_clean = clean_data(df)
    
    # 3. Create age groups
    print("\n[STEP 3] Creating age groups...")
    df_clean = create_age_groups(df_clean)
    
    # 4. Analyze data
    print("\n[STEP 4] Analyzing data...")
    
    by_condition = group_by_condition(df_clean)
    by_department = group_by_department(df_clean)
    by_age_group = group_by_age_group(df_clean)
    pivot_cond_dept = pivot_table_condition_dept(df_clean)
    summary = summary_statistics(df_clean)
    
    # 5. Generate report
    print("\n[STEP 5] Generating report...")
    
    report = generate_report(summary, by_condition, by_department, by_age_group, pivot_cond_dept)
    
    # 6. Export results
    print("\n[STEP 6] Exporting results...")
    
    report_file = output_dir / 'healthcare_eda_report.txt'
    write_report(str(report_file), report)
    
    # Export CSV summaries
    export_csv(by_condition, str(output_dir / 'condition_summary.csv'))
    export_csv(by_department, str(output_dir / 'department_summary.csv'))
    export_csv(by_age_group, str(output_dir / 'age_group_summary.csv'))
    export_csv(pivot_cond_dept, str(output_dir / 'pivot_condition_department.csv'))
    
    print("\n" + "="*60)
    print("EDA COMPLETE! Reports generated in output/ folder")
    print("="*60)

def generate_report(summary, by_condition, by_department, by_age_group, pivot):
    """Generate formatted report text."""
    
    report_lines = [
        "HEALTHCARE EXPLORATORY DATA ANALYSIS REPORT",
        "=" * 60,
        "",
        "SUMMARY STATISTICS",
        "-" * 60,
    ]
    
    for key, value in summary.items():
        report_lines.append(f"{key}: {value}")
    
    report_lines.extend(["", "", "CONDITION ANALYSIS", "-" * 60])
    report_lines.append(by_condition.to_string())
    
    report_lines.extend(["", "", "DEPARTMENT ANALYSIS", "-" * 60])
    report_lines.append(by_department.to_string())
    
    report_lines.extend(["", "", "AGE GROUP ANALYSIS", "-" * 60])
    report_lines.append(by_age_group.to_string())
    
    report_lines.extend(["", "", "CONDITION vs DEPARTMENT PIVOT", "-" * 60])
    report_lines.append(pivot.to_string())
    
    return "\n".join(report_lines)

if __name__ == "__main__":
    main()
