import pandas as pd
import scipy.stats as stats

def analyze_picking_bottlenecks():
    print("Loading extracted SQL data...")
    # 1. Load the dataset you exported from MySQL
   # The 'r' before the string is critical in Windows so Python doesn't misinterpret the backslashes
    df = pd.read_csv(r"C:\Users\ANSAF\OneDrive\CV's Projects\SixSigma logistics\Data\extracted_baseline_data.csv") 
    
    # 2. Isolate picking times for each shift
    shift_a_times = df[df['shift'] == 'A']['picking_time_seconds']
    shift_b_times = df[df['shift'] == 'B']['picking_time_seconds']
    
    # 3. Calculate descriptive statistics
    mean_a = shift_a_times.mean()
    mean_b = shift_b_times.mean()
    
    # 4. Execute Welch's T-test (equal_var=False)
    t_stat, p_value = stats.ttest_ind(shift_a_times, shift_b_times, equal_var=False)
    
    print("\n--- STATISTICAL ANALYSIS RESULTS ---")
    print(f"Shift A Mean Picking Time: {mean_a:.2f} seconds")
    print(f"Shift B Mean Picking Time: {mean_b:.2f} seconds")
    print(f"Delta (A - B): {mean_a - mean_b:.2f} seconds faster for Shift B")
    print("-" * 36)
    print(f"Calculated T-Statistic: {t_stat:.4f}")
    print(f"Calculated P-Value: {p_value:.4e}")
    
    return df

# Execute the analysis
df_logistics = analyze_picking_bottlenecks()