import joblib
import pandas as pd


# Load trained model and label encoder
model = joblib.load("models/netguard_model.pkl")
encoder = joblib.load("models/label_encoder.pkl")


# Example 1: Suspicious attack-like traffic
attack_sample = pd.DataFrame([{
    "duration": 0.4,
    "src_bytes": 220,
    "dst_bytes": 90,
    "packet_count": 210,
    "flow_rate": 360,
    "error_rate": 0.15
}])


# Example 2: Normal traffic
normal_sample = pd.DataFrame([{
    "duration": 3.2,
    "src_bytes": 900,
    "dst_bytes": 1200,
    "packet_count": 28,
    "flow_rate": 22,
    "error_rate": 0.03
}])


def predict_traffic(sample, sample_name):
    prediction = model.predict(sample)[0]
    label = encoder.inverse_transform([prediction])[0]

    probabilities = model.predict_proba(sample)[0]

    probability_table = pd.DataFrame({
        "Class": encoder.classes_,
        "Probability": probabilities
    })

    print("\n==============================")
    print(sample_name)
    print("==============================")
    print(sample)

    print("\nPrediction:")
    print(label)

    print("\nPrediction Probabilities:")
    print(probability_table)


predict_traffic(attack_sample, "Attack-like Sample")
predict_traffic(normal_sample, "Normal-like Sample")