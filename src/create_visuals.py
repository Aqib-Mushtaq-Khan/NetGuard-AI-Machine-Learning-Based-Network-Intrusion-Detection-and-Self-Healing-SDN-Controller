import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create folders
os.makedirs("results", exist_ok=True)

# Load dataset
DATA_PATH = "data/raw/network_traffic.csv"

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(
        "Dataset not found. Please run: python .\\src\\generate_dataset.py"
    )

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully.")
print(df.head())

# ==================================================
# 1. Correlation Heatmap
# ==================================================
numeric_df = df.drop(columns=["label"])
correlation = numeric_df.corr()

plt.figure(figsize=(9, 7))
plt.imshow(correlation, interpolation="nearest")
plt.colorbar(label="Correlation Strength")

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45,
    ha="right"
)
plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Network Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig("results/correlation_heatmap.png", dpi=300)
plt.close()

print("Saved: results/correlation_heatmap.png")

# ==================================================
# 2. Simulated Live Traffic Timeline CSV
# ==================================================
np.random.seed(42)

time_points = pd.date_range(
    start="2026-06-09 10:00",
    periods=120,
    freq="min"
)

traffic_volume = np.random.normal(50, 8, 120)

# Add attack spikes to make it look realistic
traffic_volume[20:28] += 70
traffic_volume[55:65] += 95
traffic_volume[90:96] += 60

timeline_df = pd.DataFrame({
    "time": time_points,
    "traffic_volume": traffic_volume
})

timeline_df.to_csv("results/live_traffic_timeline.csv", index=False)

print("Saved: results/live_traffic_timeline.csv")

# ==================================================
# 3. Risk Summary CSV
# ==================================================
risk_summary = pd.DataFrame({
    "risk_level": ["Normal", "Low Risk", "Medium Risk", "High Risk"],
    "count": [72, 14, 9, 5]
})

risk_summary.to_csv("results/risk_summary.csv", index=False)

print("Saved: results/risk_summary.csv")

# ==================================================
# 4. Class Distribution CSV
# ==================================================
class_distribution = df["label"].value_counts().reset_index()
class_distribution.columns = ["class", "count"]
class_distribution.to_csv("results/class_distribution.csv", index=False)

print("Saved: results/class_distribution.csv")

print("\nAll creative visual files created successfully.")