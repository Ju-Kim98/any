
# 🌲 3P Tree Sampling Automation Pipeline

This project automates the process of estimating tree volume and selecting trees for measurement based on the 3P (Probability Proportional to Prediction) sampling technique using aerial drone imagery.

---

## 📁 Folder Structure

```
3p-tree-sampling/
│
├── analyze_lab_images_and_build_db.py        # Step 1: Analyze lab images and create database
├── real_time_analysis.py                     # Step 2: Real-time inference with YOLOv8 via Roboflow
├── feature_extraction.py                     # Step 3: Estimate DBH and Height from bounding boxes
├── sampling_automation.py                    # Step 4: Apply 3P sampling logic
├── geospatial_mapping.py                     # Step 5: Visualize results on a GPS map using Folium
│
├── lab_images/                               # Folder for lab images used for model training
├── output/                                   # Folder for storing CSV and map results
└── README.md                                 # Project overview and usage instructions
```

---

## 🔧 Requirements

Install dependencies:
```bash
pip install roboflow pandas numpy folium
```

---

## 🚀 Workflow Overview

### Step 1: Analyze Lab Images
Extract bounding boxes using Roboflow and estimate initial volume.

```bash
python analyze_lab_images_and_build_db.py
```

---

### Step 2: Real-Time Detection
Run inference on new aerial images and generate bounding boxes with estimated volume (`Xi`).

```bash
python real_time_analysis.py path/to/drone_image.jpg
```

---

### Step 3: Feature Extraction
Estimate DBH (cm) and Tree Height (m) using bounding box size.

```bash
python feature_extraction.py path/to/image_realtime_results.csv
```

---

### Step 4: Sampling Automation (3P Logic)
Select trees for manual measurement based on estimated `Xi`.

```bash
python sampling_automation.py path/to/image_with_features.csv
```

---

### Step 5: Geospatial Mapping
Visualize sampled and non-sampled trees on an interactive map.

```bash
python geospatial_mapping.py path/to/gps_tagged_3p_sampled.csv
```

> Ensure your CSV includes `latitude` and `longitude` columns.

---

## 📌 Notes

- `Xi` values represent an estimated proxy for tree volume.
- All calculations are performed per image and saved to `.csv`.
- Trees selected for measurement are color-coded in green on the final map.
- Bounding box-to-feature scaling factors can be adjusted in `feature_extraction.py`.

