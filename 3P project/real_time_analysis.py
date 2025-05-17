
from roboflow import Roboflow
import pandas as pd
import numpy as np
import sys
import os

ROBOFLOW_API_KEY = "your_api_key_here"
PROJECT_NAME = "your-project-name"
VERSION = "version-number"

if len(sys.argv) != 2:
    print("Usage: python real_time_analysis.py <image_path>")
    sys.exit(1)

IMAGE_PATH = sys.argv[1]
if not os.path.exists(IMAGE_PATH):
    print(f"Error: {IMAGE_PATH} not found.")
    sys.exit(1)

rf = Roboflow(api_key=ROBOFLOW_API_KEY)
project = rf.workspace().project(PROJECT_NAME)
model = project.version(VERSION).model

def estimate_volume(height):
    return round((height ** 1.5) * 0.05, 2)

print(f"📸 Running detection on {IMAGE_PATH} ...")
preds = model.predict(IMAGE_PATH).json()

results = []
for i, obj in enumerate(preds["predictions"]):
    h = obj["height"]
    result = {
        "image": os.path.basename(IMAGE_PATH),
        "tree_id": f"tree_{i+1}",
        "x": obj["x"],
        "y": obj["y"],
        "width": obj["width"],
        "height": h,
        "Xi": estimate_volume(h)
    }
    results.append(result)

df = pd.DataFrame(results)
csv_path = IMAGE_PATH.replace(".jpg", "_realtime_results.csv").replace(".png", "_realtime_results.csv")
df.to_csv(f"output/{os.path.basename(csv_path)}", index=False)
print(f"✅ Detection complete. Results saved to output/{os.path.basename(csv_path)}")
