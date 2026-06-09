# NetGuard-AI: Machine Learning-Based Network Intrusion Detection and Self-Healing SDN Controller

NetGuard-AI is an end-to-end AI-powered network security system that detects abnormal network traffic using machine learning and performs automatic mitigation in a Software-Defined Networking environment.

The project combines network traffic analysis, intrusion detection, SDN simulation, and real-time dashboard visualization. It is designed to demonstrate how artificial intelligence can support intelligent, adaptive, and self-healing network infrastructures.

NetGuard-AI/
│
├── README.md
├── requirements.txt
├── LICENSE
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_model_evaluation.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── predict_traffic.py
│   └── feature_engineering.py
│
├── sdn_controller/
│   ├── ryu_controller.py
│   ├── mitigation_engine.py
│   └── flow_monitor.py
│
├── mininet_topology/
│   ├── topology.py
│   └── attack_simulation.py
│
├── dashboard/
│   └── app.py
│
├── models/
│   └── trained_model.pkl
│
├── results/
│   ├── confusion_matrix.png
│   ├── model_comparison.png
│   └── attack_detection_results.csv
│
└── report/
    └── NetGuard_AI_Report.pdf




Project architecture

Network Traffic Dataset
        ↓
Data Cleaning and Feature Engineering
        ↓
Machine Learning Model Training
        ↓
Attack Detection Model
        ↓
SDN Controller
        ↓
Automatic Mitigation
        ↓
Dashboard and Report


    ## Key Features

- Network traffic preprocessing and feature engineering
- Machine learning-based attack detection
- Comparison of multiple ML models
- SDN-based network simulation using Mininet
- Ryu controller integration
- Automatic blocking of malicious IP addresses
- Real-time dashboard for monitoring alerts and predictions
- Performance evaluation using accuracy, precision, recall, F1-score, and confusion matrix
