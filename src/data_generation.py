import pandas as pd
import numpy as np
from datetime import timedelta, date

def generate_raw_csvs():
    n_records = 45000
    overall_defect_rate = 0.048
    total_defects = int(n_records * overall_defect_rate) # 2160
    shift_size = n_records // 2 
    
    # Engineer defects (80% in Shift B)
    shift_b_defects = int(total_defects * 0.8)
    shift_a_defects = total_defects - shift_b_defects
    
    status_a = np.ones(shift_size, dtype=int)
    status_a[:shift_a_defects] = 0
    np.random.shuffle(status_a)
    
    status_b = np.ones(shift_size, dtype=int)
    status_b[:shift_b_defects] = 0
    np.random.shuffle(status_b)
    
    # Engineer picking times
    time_a = np.random.normal(loc=120, scale=15, size=shift_size).clip(min=30)
    time_b = np.random.normal(loc=95, scale=20, size=shift_size).clip(min=30)
    
    start_date = date(2026, 5, 1)
    dates = [str(start_date + timedelta(days=int(np.random.randint(0, 30)))) for _ in range(n_records)]
    order_ids = [f"ORD-{i:06d}" for i in range(1, n_records + 1)]
    
    # Build Orders Table
    df_orders = pd.DataFrame({
        'order_id': order_ids,
        'operational_date': dates,
        'shift': ['A'] * shift_size + ['B'] * shift_size,
        'picking_time_seconds': np.round(np.concatenate([time_a, time_b]), 2)
    }).sample(frac=1).reset_index(drop=True)
    
    # Build Quality Table
    status_map = dict(zip(df_orders[df_orders['shift'] == 'A']['order_id'], status_a))
    status_map.update(dict(zip(df_orders[df_orders['shift'] == 'B']['order_id'], status_b)))
    
    df_quality = pd.DataFrame({
        'order_id': order_ids,
        'packing_accuracy_status': [status_map[oid] for oid in order_ids]
    })
    
    # Export to CSV
    df_orders.to_csv('raw_orders.csv', index=False)
    df_quality.to_csv('raw_quality.csv', index=False)
    print("Generated raw_orders.csv and raw_quality.csv successfully.")

generate_raw_csvs()