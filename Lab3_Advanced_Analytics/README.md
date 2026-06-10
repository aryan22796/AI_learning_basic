# Lab 3: Advanced Analytics & Statistical Testing

## Overview
This project demonstrates enterprise-level data analysis techniques including:
- Realistic data generation with statistical properties
- Comprehensive data quality assessment
- Advanced statistical profiling (skewness, kurtosis, normality)
- Outlier detection using multiple methods (IQR, Z-score)
- Correlation analysis with significance testing
- Segment analysis and comparison
- Comprehensive reporting and visualization preparation

## Folder Structure
```
Lab3_Advanced_Analytics/
├── data/
│   └── ecommerce_transactions.csv (generated)
├── src/
│   ├── data_generator.py      # Dataset generation
│   ├── analytics.py           # Advanced analytics module
│   └── main.py               # Orchestration script
├── output/
│   ├── advanced_analytics_report.txt
│   ├── statistical_profile.csv
│   ├── outlier_detection.csv
│   ├── strong_correlations.csv
│   └── segment_analysis.csv
└── README.md
```

## Features

### Data Generation
- **10,000 realistic e-commerce transactions**
- Temporal patterns (timestamps, day-of-week, seasonal effects)
- Multiple product categories with realistic price distributions
- Customer segments (new vs. returning)
- Device and regional breakdowns
- Missing values and outliers (realistic data quality issues)

### Analytics Capabilities

#### Data Quality Assessment
- Missing value analysis with percentages
- Duplicate detection
- Cardinality analysis
- Memory profiling
- Data type validation

#### Statistical Profiling
- Mean, median, standard deviation
- Quartiles and percentiles
- Skewness (measure of distribution asymmetry)
- Kurtosis (measure of tail heaviness)
- Normality testing with p-values

#### Outlier Detection
- **IQR Method**: Detects extreme values using interquartile range
- **Z-Score Method**: Identifies values >3 standard deviations from mean
- Outlier count and percentage reporting
- Index tracking for investigation

#### Correlation Analysis
- Pearson correlation matrix
- Spearman correlation (non-linear relationships)
- P-value significance testing
- Strong correlation identification (|r| > 0.3)

#### Segment Analysis
- Break down metrics by categorical variables
- Calculate aggregate statistics per segment
- Compare segment performance
- Identify high-value segments

## Setup

### 1. Virtual Environment
```bash
cd /Users/aryan/Desktop/AI_learning
source .venv/bin/activate
```

### 2. Dependencies
```bash
pip install pandas numpy scipy
```

### 3. Run Analysis
```bash
cd Lab3_Advanced_Analytics/src
python3 main.py
```

## Expected Output

The script will:
1. Generate 10,000 realistic transaction records
2. Save the dataset to `data/ecommerce_transactions.csv`
3. Perform comprehensive analysis on:
   - Data quality (missing values, duplicates)
   - Statistical distributions (mean, std, skewness)
   - Outliers (IQR method identifies extreme values)
   - Correlations (finds relationships between variables)
   - Segments (product category, region, customer type)
4. Generate 5 output reports:
   - Text summary with key findings
   - CSV files with detailed statistics
   - Outlier detection results
   - Correlation matrix
   - Segment performance metrics

## Key Concepts Demonstrated

| Concept | Application |
|---------|-------------|
| **Skewness** | Identify if price distribution is right-heavy (more expensive items) |
| **Kurtosis** | Measure if there are extreme outliers in the data |
| **IQR Method** | Detect unusual transaction values for fraud investigation |
| **Z-Score** | Identify statistically extreme observations |
| **Correlation** | Find related metrics (e.g., discount % vs. transaction value) |
| **Segment Analysis** | Compare product category performance, regional differences |
| **Missing Data** | Handle incomplete customer age, discount information |

## Business Questions Answered

1. **What are typical transaction patterns?**
   → Statistical profile shows mean, median, distribution shape

2. **Are there data quality issues?**
   → Data quality report identifies missing values and outliers

3. **Which variables influence each other?**
   → Correlation analysis reveals relationships

4. **Which segments perform best?**
   → Segment analysis breaks down performance by category

5. **Are there suspicious transactions?**
   → Outlier detection flags unusual values for review

## Advanced Techniques Used

- **Exploratory Data Analysis (EDA)**: Comprehensive data exploration
- **Descriptive Statistics**: Mean, median, quartiles, standard deviation
- **Distribution Analysis**: Skewness and kurtosis for shape assessment
- **Anomaly Detection**: IQR and Z-score methods
- **Correlation Analysis**: Identifying relationships between variables
- **Segmentation**: Group-level analysis and comparison
- **Data Profiling**: Systematic assessment of data quality and characteristics
