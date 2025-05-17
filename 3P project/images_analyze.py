
from roboflow import Roboflow
import pandas as pd
import numpy as np
import os

ROBOFLOW_API_KEY = "your_api_key_here"
PROJECT_NAME = "your-project-name"
VERSION = "version-number"
IMAGE_DIR = "lab_images/"

rf = Roboflow(api_key=ROBOFLOW_API_KEY)
project = rf.workspace().project(PROJECT_NAME)
model = project.version(VERSION).model

def estimate_volume(height):
    return round((height ** 1.5) * 0.05, 2)

results = []

for filename in os.listdir(IMAGE_DIR):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        filepath = os.path.join(IMAGE_DIR, filename)
        print(f"🔍 Processing {filename}")
        preds = model.predict(filepath).json()

        for i, obj in enumerate(preds["predictions"]):
            result = {
                "image": filename,
                "tree_id": f"{filename}_{i+1}",
                "x": obj["x"],
                "y": obj["y"],
                "width": obj["width"],
                "height": obj["height"],
                "Xi": estimate_volume(obj["height"])
            }
            results.append(result)

df = pd.DataFrame(results)
df.to_csv("output/tree_db_lab_images.csv", index=False)
print("✅ Saved: output/tree_db_lab_images.csv")
