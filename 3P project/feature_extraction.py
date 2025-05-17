
import pandas as pd
import numpy as np
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python feature_extraction.py <input_detection_csv>")
    sys.exit(1)

CSV_PATH = sys.argv[1]
if not os.path.exists(CSV_PATH):
    print(f"Error: {CSV_PATH} not found.")
    sys.exit(1)

df = pd.read_csv(CSV_PATH)

def estimate_dbh(width, scaling_factor=0.3):
    return round(width * scaling_factor, 2)

def estimate_height(height, calibration_factor=0.5):
    return round(height * calibration_factor, 2)

df["DBH_cm"] = df["width"].apply(lambda w: estimate_dbh(w))
df["TreeHeight_m"] = df["height"].apply(lambda h: estimate_height(h))

def estimate_volume_from_features(dbh_cm, height_m):
    return round((dbh_cm ** 2 * height_m) * 0.0001, 2)

df["Xi_updated"] = df.apply(lambda row: estimate_volume_from_features(row["DBH_cm"], row["TreeHeight_m"]), axis=1)

output_path = CSV_PATH.replace(".csv", "_with_features.csv")
df.to_csv(output_path, index=False)
print(f"Feature extraction complete. Saved to {output_path}")
