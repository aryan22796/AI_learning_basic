import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta

def generate_ecommerce_dataset(n_records=10000, random_seed=42):
    """Generate a realistic e-commerce transactional dataset."""
    np.random.seed(random_seed)
    
    # Date range
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(hours=np.random.randint(0, 8760)) for _ in range(n_records)]
    
    # Generate data
    data = {
        'transaction_id': range(1, n_records + 1),
        'customer_id': np.random.randint(1000, 3000, n_records),
        'timestamp': dates,
        'product_category': np.random.choice(
            ['Electronics', 'Clothing', 'Home', 'Beauty', 'Sports', 'Books', 'Toys'],
            n_records, 
            p=[0.25, 0.25, 0.15, 0.15, 0.1, 0.07, 0.03]
        ),
        'product_price': np.maximum(np.random.exponential(scale=80, size=n_records) + 15, 10),
        'quantity': np.maximum(np.random.poisson(lam=1.5), 1),
        'discount_pct': np.random.choice([0, 5, 10, 15, 20, 25], n_records, p=[0.45, 0.2, 0.15, 0.1, 0.07, 0.03]),
        'customer_age': np.clip(np.random.normal(38, 13, n_records), 18, 75).astype(int),
        'is_returning': np.random.choice([True, False], n_records, p=[0.35, 0.65]),
        'device_type': np.random.choice(['Mobile', 'Desktop', 'Tablet'], n_records, p=[0.65, 0.25, 0.1]),
        'region': np.random.choice(['North', 'South', 'East', 'West', 'Central'], n_records, p=[0.2, 0.22, 0.28, 0.18, 0.12]),
        'payment_method': np.random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Apple Pay', 'Google Pay'], n_records, p=[0.4, 0.25, 0.2, 0.1, 0.05])
    }
    
    df = pd.DataFrame(data)
    
    # Calculate derived columns
    df['total_price'] = df['product_price'] * df['quantity']
    df['final_price'] = df['total_price'] * (1 - df['discount_pct'] / 100)
    df['date'] = df['timestamp'].dt.date
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.day_name()
    df['month'] = df['timestamp'].dt.month
    df['week'] = df['timestamp'].dt.isocalendar().week
    
    # Add some realistic missing values
    missing_indices = np.random.choice(n_records, size=int(0.015 * n_records), replace=False)
    df.loc[missing_indices[:n_records//200], 'customer_age'] = np.nan
    df.loc[missing_indices[n_records//200:], 'discount_pct'] = np.nan
    
    # Add some outliers
    outlier_indices = np.random.choice(n_records, size=max(1, n_records//500), replace=False)
    df.loc[outlier_indices, 'product_price'] = df.loc[outlier_indices, 'product_price'] * np.random.uniform(5, 15, len(outlier_indices))
    
    return df

def save_dataset(df, output_path):
    """Save dataset to CSV."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"[INFO] Dataset saved to {output_path}")
    return True
