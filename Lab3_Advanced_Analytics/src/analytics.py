import pandas as pd
import numpy as np
from scipy import stats
from pathlib import Path

class AdvancedAnalytics:
    """Advanced analytics module for comprehensive EDA."""
    
    def __init__(self, df):
        self.df = df
        self.numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        self.categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    def data_quality_report(self):
        """Generate comprehensive data quality assessment."""
        report = {
            'total_records': len(self.df),
            'total_columns': len(self.df.columns),
            'memory_usage_mb': self.df.memory_usage(deep=True).sum() / 1024**2,
            'missing_values': self.df.isnull().sum().to_dict(),
            'duplicates': self.df.duplicated().sum(),
            'data_types': self.df.dtypes.astype(str).to_dict()
        }
        return report
    
    def statistical_profile(self):
        """Generate statistical profile for numeric columns."""
        profile = {}
        for col in self.numeric_cols:
            data = self.df[col].dropna()
            if len(data) > 0:
                profile[col] = {
                    'count': len(data),
                    'mean': float(data.mean()),
                    'std': float(data.std()),
                    'min': float(data.min()),
                    'q25': float(data.quantile(0.25)),
                    'median': float(data.median()),
                    'q75': float(data.quantile(0.75)),
                    'max': float(data.max()),
                    'skewness': float(stats.skew(data)),
                    'kurtosis': float(stats.kurtosis(data))
                }
        return profile
    
    def outlier_detection(self, method='iqr', multiplier=1.5):
        """Detect outliers using IQR or Z-score method."""
        outliers = {}
        
        for col in self.numeric_cols:
            data = self.df[col].dropna()
            if method == 'iqr':
                Q1, Q3 = data.quantile([0.25, 0.75])
                IQR = Q3 - Q1
                lower = Q1 - multiplier * IQR
                upper = Q3 + multiplier * IQR
                outlier_mask = (data < lower) | (data > upper)
            elif method == 'zscore':
                z_scores = np.abs(stats.zscore(data))
                outlier_mask = z_scores > 3
            
            outliers[col] = {
                'count': int(outlier_mask.sum()),
                'percentage': float(outlier_mask.sum() / len(self.df) * 100),
                'indices': data[outlier_mask].index.tolist()
            }
        
        return outliers
    
    def correlation_analysis(self):
        """Analyze correlations between numeric variables."""
        numeric_df = self.df[self.numeric_cols].dropna()
        corr_matrix = numeric_df.corr(method='pearson')
        
        # Find strong correlations
        strong_corr = []
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                if abs(corr_matrix.iloc[i, j]) > 0.3:
                    strong_corr.append({
                        'var1': corr_matrix.columns[i],
                        'var2': corr_matrix.columns[j],
                        'correlation': float(corr_matrix.iloc[i, j])
                    })
        
        return {
            'correlation_matrix': corr_matrix.to_dict(),
            'strong_correlations': strong_corr
        }
    
    def categorical_analysis(self):
        """Analyze categorical variables."""
        analysis = {}
        for col in self.categorical_cols:
            if col not in ['timestamp', 'date']:
                value_counts = self.df[col].value_counts(dropna=False)
                analysis[col] = {
                    'unique_values': len(value_counts),
                    'distribution': value_counts.to_dict(),
                    'mode': value_counts.index[0] if len(value_counts) > 0 else None
                }
        return analysis
    
    def segment_analysis(self, segment_col, metrics):
        """Analyze metrics by segment."""
        segments = {}
        for segment in self.df[segment_col].unique():
            if pd.notna(segment):
                seg_data = self.df[self.df[segment_col] == segment]
                seg_metrics = {}
                
                for metric in metrics:
                    if metric in self.numeric_cols:
                        seg_metrics[metric] = {
                            'count': len(seg_data),
                            'sum': float(seg_data[metric].sum()),
                            'mean': float(seg_data[metric].mean()),
                            'std': float(seg_data[metric].std())
                        }
                
                segments[segment] = seg_metrics
        
        return segments
    
    def generate_summary_report(self):
        """Generate comprehensive summary report."""
        report_text = []
        report_text.append("="*70)
        report_text.append("ADVANCED ANALYTICS SUMMARY REPORT")
        report_text.append("="*70)
        
        # Data Quality
        quality = self.data_quality_report()
        report_text.append("\n[1] DATA QUALITY ASSESSMENT")
        report_text.append("-"*70)
        report_text.append(f"Total Records: {quality['total_records']:,}")
        report_text.append(f"Total Columns: {quality['total_columns']}")
        report_text.append(f"Memory Usage: {quality['memory_usage_mb']:.2f} MB")
        report_text.append(f"Total Missing Values: {sum(quality['missing_values'].values())}")
        report_text.append(f"Duplicate Rows: {quality['duplicates']}")
        
        # Statistical Profile
        profile = self.statistical_profile()
        report_text.append("\n[2] STATISTICAL PROFILE")
        report_text.append("-"*70)
        for col, stats_dict in list(profile.items())[:5]:
            report_text.append(f"\n{col}:")
            report_text.append(f"  Mean: {stats_dict['mean']:.2f}, Std: {stats_dict['std']:.2f}")
            report_text.append(f"  Min: {stats_dict['min']:.2f}, Max: {stats_dict['max']:.2f}")
            report_text.append(f"  Skewness: {stats_dict['skewness']:.3f}, Kurtosis: {stats_dict['kurtosis']:.3f}")
        
        # Outliers
        outliers = self.outlier_detection()
        report_text.append("\n[3] OUTLIER DETECTION (IQR Method)")
        report_text.append("-"*70)
        for col, outlier_info in outliers.items():
            if outlier_info['count'] > 0:
                report_text.append(f"{col}: {outlier_info['count']} outliers ({outlier_info['percentage']:.2f}%)")
        
        # Correlations
        corr_analysis = self.correlation_analysis()
        report_text.append("\n[4] STRONG CORRELATIONS (|r| > 0.3)")
        report_text.append("-"*70)
        if corr_analysis['strong_correlations']:
            for corr in corr_analysis['strong_correlations'][:5]:
                report_text.append(f"{corr['var1']} <-> {corr['var2']}: {corr['correlation']:.3f}")
        else:
            report_text.append("No strong correlations found.")
        
        report_text.append("\n" + "="*70)
        return "\n".join(report_text)
