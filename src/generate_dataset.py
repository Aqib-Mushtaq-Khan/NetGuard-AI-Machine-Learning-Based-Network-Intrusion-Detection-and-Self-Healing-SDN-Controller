import os
import numpy as np
import pandas as pd

np.random.seed(42)

def make_data():
    normal = pd.DataFrame({
        "duration": np.random.normal(3, 1, 1000).clip(0.1, 10),
        "src_bytes": np.random.normal(800, 250, 1000).clip(40, 3000),
        "dst_bytes": np.random.normal(1200, 300, 1000).clip(40, 4000),
        "packet_count": np.random.normal(25, 8, 1000).clip(1, 80),
        "flow_rate": np.random.normal(20, 8, 1000).clip(1, 80),
        "error_rate": np.random.normal(0.03, 0.02, 1000).clip(0, 0.2),
        "label": "Normal"
    })

    attack = pd.DataFrame({
        "duration": np.random.normal(0.5, 0.2, 1000).clip(0.01, 3),
        "src_bytes": np.random.normal(200, 100, 1000).clip(20, 1000),
        "dst_bytes": np.random.normal(100, 50, 1000).clip(10, 800),
        "packet_count": np.random.normal(180, 45, 1000).clip(50, 400),
        "flow_rate": np.random.normal(320, 80, 1000).clip(100, 650),
        "error_rate": np.random.normal(0.15, 0.06, 1000).clip(0, 0.5),
        "label": "Attack"
    })

    df = pd.concat([normal, attack], ignore_index=True)
    df = df.sample(frac=1, random_state=42)

    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/network_traffic.csv", index=False)

    print("Dataset created successfully.")
    print(df.head())
    print(df["label"].value_counts())

if __name__ == "__main__":
    make_data()