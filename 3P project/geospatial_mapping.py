
import pandas as pd
import folium
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python geospatial_mapping.py <gps_tagged_csv>")
    sys.exit(1)

CSV_PATH = sys.argv[1]
if not os.path.exists(CSV_PATH):
    print(f"Error: {CSV_PATH} not found.")
    sys.exit(1)

df = pd.read_csv(CSV_PATH)

if not {"latitude", "longitude"}.issubset(df.columns):
    print("Error: CSV must contain 'latitude' and 'longitude' columns.")
    sys.exit(1)

lat_center = df["latitude"].mean()
lon_center = df["longitude"].mean()
tree_map = folium.Map(location=[lat_center, lon_center], zoom_start=17)

for _, row in df.iterrows():
    color = "green" if row.get("SelectedForMeasurement", False) else "blue"
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=4,
        color=color,
        fill=True,
        fill_opacity=0.6,
        popup=folium.Popup(f"Tree: {row.get('tree_id', 'N/A')}<br>Xi: {row.get('Xi', row.get('Xi_updated', ''))}", max_width=200)
    ).add_to(tree_map)

map_path = CSV_PATH.replace(".csv", "_map.html")
tree_map.save(map_path)
print(f"✅ Map created and saved to {map_path}")
