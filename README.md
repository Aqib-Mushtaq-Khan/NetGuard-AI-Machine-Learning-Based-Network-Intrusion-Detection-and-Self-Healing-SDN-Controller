# NetGuard-AI: Machine Learning-Based Network Anomaly Detection Dashboard

NetGuard-AI is an AI-powered network security project that detects abnormal network traffic using machine learning and presents the results through a professional Streamlit dashboard.

The project demonstrates how artificial intelligence can support intelligent network monitoring by classifying traffic as either **Normal** or **Attack** based on network flow features such as packet count, flow rate, error rate, byte volume, and duration.

---

## Project Overview

Modern computer networks generate large volumes of traffic every second. Some traffic is legitimate, while other traffic may indicate attacks such as flooding, scanning, brute-force attempts, or abnormal behaviour.

NetGuard-AI provides a beginner-friendly but professional prototype for network anomaly detection. It uses a synthetic network traffic dataset, trains a Random Forest machine learning model, evaluates its performance, and visualizes the results through an interactive cybersecurity-style dashboard.

---

## Key Features

* Synthetic network traffic dataset generation
* Machine learning-based anomaly detection
* Random Forest classification model
* Traffic classification as Normal or Attack
* Model evaluation using accuracy, precision, recall, F1-score, and confusion matrix
* Feature importance analysis
* Correlation heatmap
* Simulated real-time traffic visualization
* Attack probability gauge
* Interactive Streamlit dashboard
* Professional visual analytics for portfolio and GitHub presentation

---

## Technology Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Plotly
* Streamlit
* Joblib
* Git and GitHub

---

## Project Structure

```text
NetGuard-AI/
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── raw/
│       └── network_traffic.csv
│
├── models/
│   ├── netguard_model.pkl
│   └── label_encoder.pkl
│
├── results/
│   ├── classification_report.txt
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   ├── feature_importance.csv
│   ├── correlation_heatmap.png
│   ├── class_distribution.csv
│   ├── live_traffic_timeline.csv
│   └── risk_summary.csv
│
├── src/
│   ├── generate_dataset.py
│   ├── train_model.py
│   ├── predict_sample.py
│   └── create_visuals.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## How the System Works

```text
Synthetic Network Traffic Data
        ↓
Data Cleaning and Feature Preparation
        ↓
Machine Learning Model Training
        ↓
Attack or Normal Traffic Classification
        ↓
Model Evaluation and Visual Analytics
        ↓
Interactive Streamlit Dashboard
```

---

## Dataset

The current version uses a synthetic dataset generated with Python. The dataset includes two traffic classes:

| Class  | Description                                                                                      |
| ------ | ------------------------------------------------------------------------------------------------ |
| Normal | Regular network traffic with stable duration, packet count, flow rate, and low error rate        |
| Attack | Suspicious traffic with high packet count, high flow rate, short duration, and higher error rate |

Features used by the model:

| Feature      | Meaning                              |
| ------------ | ------------------------------------ |
| duration     | Duration of the network flow         |
| src_bytes    | Bytes sent by the source             |
| dst_bytes    | Bytes received by the destination    |
| packet_count | Number of packets in the flow        |
| flow_rate    | Traffic rate or packet sending speed |
| error_rate   | Abnormal or failed traffic ratio     |

---

## Machine Learning Model

The project uses a **Random Forest Classifier** because it is reliable, interpretable, and effective for tabular network traffic data.

The model is trained to classify network flows into:

* Normal
* Attack

Evaluation metrics include:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrix
* Feature importance

---

## Dashboard

The Streamlit dashboard includes:

* Live traffic prediction
* Attack probability gauge
* Prediction confidence chart
* Confusion matrix
* Classification report
* Feature importance visualization
* Traffic class distribution
* Attack vs normal scatter plot
* Simulated real-time network traffic timeline
* Correlation heatmap
* Project summary and future work

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Aqib-Mushtaq-Khan/NetGuard-AI-Machine-Learning-Based-Network-Intrusion-Detection-and-Self-Healing-SDN-Controller.git
cd NetGuard-AI-Machine-Learning-Based-Network-Intrusion-Detection-and-Self-Healing-SDN-Controller
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

### 4. Install Required Libraries

```bash
python -m pip install -r requirements.txt
```

### 5. Generate Dataset

```bash
python .\src\generate_dataset.py
```

### 6. Train the Model

```bash
python .\src\train_model.py
```

### 7. Create Visual Analytics Files

```bash
python .\src\create_visuals.py
```

### 8. Test Sample Prediction

```bash
python .\src\predict_sample.py
```

### 9. Run the Dashboard

```bash
streamlit run .\dashboard\app.py
```

Then open:

```text
http://localhost:8501
```

---

## Current Status

This is **Version 1** of NetGuard-AI.

Implemented:

* Dataset generation
* Machine learning training
* Attack detection
* Model evaluation
* Visual analytics
* Streamlit dashboard

Planned future improvements:

* Integration with real intrusion detection datasets such as CIC-IDS2017 or UNSW-NB15
* Multi-class attack detection including DDoS, PortScan, BruteForce, Botnet, and Web attacks
* Live packet capture using Scapy
* SDN-based simulation using Mininet
* Ryu controller integration
* Automatic mitigation by blocking malicious flows
* Deployment on Streamlit Cloud or Hugging Face Spaces

---

## Future Vision

The long-term goal of NetGuard-AI is to evolve from a machine learning dashboard into a complete AI-based self-healing network security system.

Future versions will aim to connect anomaly detection with Software-Defined Networking, where the system can automatically respond to suspicious traffic by blocking malicious flows, applying rate limits, or rerouting traffic.

---

## Author

**Aqib Mushtaq**
Computer Science and Networking Engineer
Research interests: Wireless Networks, AI for Telecom, Cybersecurity, Network Optimization, SDN, LoRaWAN, and Intelligent Network Monitoring
