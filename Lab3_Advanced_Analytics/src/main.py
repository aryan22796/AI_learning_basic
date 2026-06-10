#!/usr/bin/env python3
"""
Lab 3: Advanced Analytics Pipeline
Demonstrates enterprise-grade data analysis with statistical testing, 
outlier detection, and comprehensive reporting.
"""

import sys
import pandas as pd
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from data_generator import generate_ecommerce_dataset, save_dataset
from analytics import AdvancedAnalytics

def main():
    """Execute advanced analytics pipeline."""
    
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / 'data'
    output_dir = base_dir / 'output'
    
    print("="*70)
    print("LAB 3: ADVANCED ANALYTICS PIPELINE")
    print("="*70)
    
    # Step 1: Generate dataset
    print("\n[STEP 1] Generating realistic e-commerce dataset...")
    df = generate_ecommerce_dataset(n_records=10000, random_seed=42)
    print(f"[INFO] Generated {len(df):,} records with {len(df.columns)} columns")
    
    # Save dataset
    data_file = data_dir / 'ecommerce_transactions.csv'
    save_dataset(df, str(data_file))
    
    # Step 2: Initialize analytics
    print("\n[STEP 2] Running advanced analytics...")
    analytics = AdvancedAnalytics(df)
    
    # Step 3: Generate reports
    print("\n[STEP 3] Generating analytical reports...")
    
    # Data quality report
    quality_report = analytics.data_quality_report()
    print(f"\n[INFO] Data Quality:")
    print(f"  - Missing values: {sum(quality_report['missing_values'].values())}")
    print(f"  - Duplicates: {quality_report['duplicates']}")
    print(f"  - Memory usage: {quality_report['memory_usage_mb']:.2f} MB")
    
    # Statistical profile
    stats_profile = analytics.statistical_profile()
    print(f"\n[INFO] Statistical Profiling complete for {len(stats_profile)} numeric columns")
    
    # Outlier detection
    outliers = analytics.outlier_detection(method='iqr')
    outlier_count = sum(o['count'] for o in outliers.values())
    print(f"\n[INFO] Outlier Detection: {outlier_count} outliers detected")
    
    # Correlation analysis
    corr_analysis = analytics.correlation_analysis()
    print(f"\n[INFO] Correlation Analysis: {len(corr_analysis['strong_correlations'])} strong correlations found")
    
    # Categorical analysis
    cat_analysis = analytics.categorical_analysis()
    print(f"\n[INFO] Categorical Analysis: {len(cat_analysis)} categorical columns analyzed")
    
    # Segment analysis
    print("\n[STEP 4] Running segment analysis...")
    segment_analysis = analytics.segment_analysis(
        'product_category',
        ['final_price', 'quantity']
    )
    print(f"[INFO] Analyzed {len(segment_analysis)} product category segments")
    
    # Step 5: Generate comprehensive report
    print("\n[STEP 5] Generating comprehensive summary report...")
    summary_report = analytics.generate_summary_report()
    
    # Save reports
    output_dir.mkdir(parents=True, exist_ok=True)
    
    report_file = output_dir / 'advanced_analytics_report.txt'
    with open(report_file, 'w') as f:
        f.write(summary_report)
    print(f"[INFO] Report saved to {report_file}")
    
    # Save statistical profile
    stats_df = pd.DataFrame(stats_profile).T
    stats_df.to_csv(output_dir / 'statistical_profile.csv')
    print(f"[INFO] Statistical profile saved to {output_dir / 'statistical_profile.csv'}")
    
    # Save outlier summary
    outlier_summary = pd.DataFrame([
        {'column': col, 'outlier_count': info['count'], 'percentage': f"{info['percentage']:.2f}%"}
        for col, info in outliers.items() if info['count'] > 0
    ])
    if len(outlier_summary) > 0:
        outlier_summary.to_csv(output_dir / 'outlier_detection.csv', index=False)
        print(f"[INFO] Outlier report saved to {output_dir / 'outlier_detection.csv'}")
    
    # Save correlation analysis
    strong_corr_df = pd.DataFrame(corr_analysis['strong_correlations'])
    if len(strong_corr_df) > 0:
        strong_corr_df.to_csv(output_dir / 'strong_correlations.csv', index=False)
        print(f"[INFO] Correlation report saved to {output_dir / 'strong_correlations.csv'}")
    
    # Save segment analysis
    segment_summary = []
    for segment, metrics in segment_analysis.items():
        row = {'segment': segment}
        for metric, values in metrics.items():
            row[f'{metric}_count'] = values['count']
            row[f'{metric}_mean'] = f"{values['mean']:.2f}"
            row[f'{metric}_sum'] = f"{values['sum']:.2f}"
        segment_summary.append(row)
    
    segment_df = pd.DataFrame(segment_summary)
    segment_df.to_csv(output_dir / 'segment_analysis.csv', index=False)
    print(f"[INFO] Segment analysis saved to {output_dir / 'segment_analysis.csv'}")
    
    print("\n" + "="*70)
    print("ADVANCED ANALYTICS PIPELINE COMPLETE!")
    print("="*70)
    print(f"\nOutput files generated in: {output_dir}")
    print("  - advanced_analytics_report.txt")
    print("  - statistical_profile.csv")
    print("  - outlier_detection.csv (if outliers found)")
    print("  - strong_correlations.csv (if correlations found)")
    print("  - segment_analysis.csv")

if __name__ == "__main__":
    main()
