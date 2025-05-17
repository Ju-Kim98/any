
import pandas as pd
import numpy as np
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python sampling_automation.py <feature_csv>")
    sys.exit(1)

CSV_PATH = sys.argv[1]
if not os.path.exists(CSV_PATH):
    print(f"Error: {CSV_PATH} not found.")
    sys.exit(1)

df = pd.read_csv(CSV_PATH)
xi_column = "Xi_updated" if "Xi_updated" in df.columns else "Xi"

np.random.seed(42)
Xi_values = df[xi_column]
random_thresholds = np.random.uniform(0, Xi_values.max(), len(Xi_values))

df["Random"] = np.round(random_thresholds, 2)
df["SelectedForMeasurement"] = df[xi_column] < df["Random"]

output_path = CSV_PATH.replace(".csv", "_3p_sampled.csv")
df.to_csv(output_path, index=False)
print(f"3P sampling complete. Results saved to {output_path}")
