import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def build_six_sigma_p_chart():
    print("Loading clean data for Control Chart visualization...")
    # Relying on clean relative pathing
    df = pd.read_csv(r"C:\Users\ANSAF\OneDrive\CV's Projects\SixSigma logistics\Data\extracted_baseline_data.csv")
    df.columns = [col.lower().strip() for col in df.columns]
    
    # 1. Data Preparation
    df['operational_date'] = pd.to_datetime(df['operational_date'])
    
    # Convert accuracy status to a binary defect flag (0 = Defect in original data, so we map it to 1)
    df['is_defect'] = (df['packing_accuracy_status'] == 0).astype(int)
    
    # Aggregate daily volumes and defect counts
    daily = df.groupby('operational_date').agg(
        total_orders=('order_id', 'count'),
        defects=('is_defect', 'sum')
    ).reset_index()
    
    daily['daily_defect_rate'] = daily['defects'] / daily['total_orders']
    
    # 2. Six Sigma Calculations (p-chart math)
    p_bar = daily['defects'].sum() / daily['total_orders'].sum()
    
    # Standard error for proportion: sqrt((p * (1-p)) / n)
    standard_error = np.sqrt((p_bar * (1 - p_bar)) / daily['total_orders'])
    
    daily['ucl'] = p_bar + (3 * standard_error)
    daily['lcl'] = p_bar - (3 * standard_error)
    daily['lcl'] = daily['lcl'].clip(lower=0) 
    
    out_of_control = daily[(daily['daily_defect_rate'] > daily['ucl']) | 
                           (daily['daily_defect_rate'] < daily['lcl'])]
    
    # 3. Matplotlib Visualization
    plt.figure(figsize=(14, 7))
    
    plt.plot(daily['operational_date'], daily['daily_defect_rate'], 
             marker='o', color='#2c3e50', label='Daily Defect Rate', linewidth=2)
    
    plt.axhline(p_bar, color='#27ae60', linestyle='-', linewidth=2, 
                label=f'Center Line (Baseline: {p_bar:.2%})')
    
    plt.plot(daily['operational_date'], daily['ucl'], color='#c0392b', 
             linestyle='--', linewidth=1.5, label='UCL / LCL (±3 Sigma)')
    plt.plot(daily['operational_date'], daily['lcl'], color='#c0392b', 
             linestyle='--', linewidth=1.5)
    
    if not out_of_control.empty:
        plt.scatter(out_of_control['operational_date'], out_of_control['daily_defect_rate'], 
                    color='#e74c3c', s=150, zorder=5, label='Out of Control (>3σ)', edgecolors='black')
    
    # Formatting
    plt.title('Six Sigma p-Chart: Daily Outbound Picking Defects', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Operational Date', fontsize=12, fontweight='bold')
    plt.ylabel('Defect Proportion', fontsize=12, fontweight='bold')
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.1%}'.format(y)))
    
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend(loc='upper right', framealpha=0.9, edgecolor='black')
    plt.tight_layout()
    
    plt.savefig('six_sigma_p_chart_portfolio.png', dpi=300)
    print(f"Chart generated and saved locally. Baseline verified at: {p_bar:.2%}")
    
    plt.show()

build_six_sigma_p_chart()