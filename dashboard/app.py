import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


# ==================================================
# PAGE CONFIGURATION
# ==================================================
st.set_page_config(
    page_title="NetGuard-AI",
    page_icon="🛡️",
    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top left, #172554 0%, #020617 40%, #020617 100%);
        color: white;
    }

    .hero-box {
        background: linear-gradient(135deg, rgba(30,64,175,0.95), rgba(15,23,42,0.98));
        padding: 38px;
        border-radius: 26px;
        color: white;
        box-shadow: 0px 12px 35px rgba(0,0,0,0.45);
        border: 1px solid rgba(148,163,184,0.25);
        margin-bottom: 25px;
    }

    .hero-title {
        font-size: 50px;
        font-weight: 900;
        margin-bottom: 8px;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        font-size: 18px;
        color: #D1D5DB;
        line-height: 1.7;
        max-width: 1000px;
    }

    .metric-card {
        background: rgba(15,23,42,0.88);
        border: 1px solid rgba(148,163,184,0.25);
        border-radius: 20px;
        padding: 23px;
        text-align: center;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.35);
        min-height: 120px;
    }

    .metric-title {
        color: #94A3B8;
        font-size: 14px;
        margin-bottom: 8px;
    }

    .metric-value {
        color: white;
        font-size: 25px;
        font-weight: 850;
    }

    .section-title {
        font-size: 30px;
        font-weight: 850;
        color: white;
        margin-top: 15px;
        margin-bottom: 12px;
    }

    .info-box {
        background: rgba(15,23,42,0.85);
        border-left: 5px solid #38BDF8;
        padding: 18px;
        border-radius: 14px;
        color: #E5E7EB;
        margin-top: 12px;
        margin-bottom: 18px;
        line-height: 1.6;
    }

    .attack-card {
        background: linear-gradient(135deg, #7F1D1D, #DC2626, #FB7185);
        color: white;
        padding: 30px;
        border-radius: 22px;
        font-size: 28px;
        font-weight: 900;
        text-align: center;
        box-shadow: 0px 12px 35px rgba(220,38,38,0.40);
        border: 1px solid rgba(254,202,202,0.35);
    }

    .normal-card {
        background: linear-gradient(135deg, #064E3B, #059669, #34D399);
        color: white;
        padding: 30px;
        border-radius: 22px;
        font-size: 28px;
        font-weight: 900;
        text-align: center;
        box-shadow: 0px 12px 35px rgba(16,185,129,0.40);
        border: 1px solid rgba(167,243,208,0.35);
    }

    .mini-card {
        background: rgba(15,23,42,0.88);
        border: 1px solid rgba(148,163,184,0.25);
        border-radius: 18px;
        padding: 20px;
        color: #E5E7EB;
        box-shadow: 0px 8px 22px rgba(0,0,0,0.28);
        margin-bottom: 15px;
    }

    .footer-text {
        color: #94A3B8;
        text-align: center;
        font-size: 14px;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# LOAD MODEL
# ==================================================
MODEL_PATH = "models/netguard_model.pkl"
ENCODER_PATH = "models/label_encoder.pkl"
DATA_PATH = "data/raw/network_traffic.csv"

if not os.path.exists(MODEL_PATH):
    st.error("Model not found. Please run: python .\\src\\train_model.py")
    st.stop()

if not os.path.exists(ENCODER_PATH):
    st.error("Label encoder not found. Please run: python .\\src\\train_model.py")
    st.stop()

if not os.path.exists(DATA_PATH):
    st.error("Dataset not found. Please run: python .\\src\\generate_dataset.py")
    st.stop()

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)
df = pd.read_csv(DATA_PATH)


# ==================================================
# HERO SECTION
# ==================================================
st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">🛡️ NetGuard-AI</div>
        <div class="hero-subtitle">
            A visually enhanced AI-powered network anomaly detection dashboard.
            This system classifies traffic as <b>Normal</b> or <b>Attack</b> using
            machine learning and presents security insights through real-time analytics,
            feature analysis, and professional monitoring visuals.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# TOP KPI CARDS
# ==================================================
total_flows = len(df)
attack_count = int((df["label"] == "Attack").sum())
normal_count = int((df["label"] == "Normal").sum())
attack_ratio = round((attack_count / total_flows) * 100, 2)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Total Network Flows</div>
            <div class="metric-value">{total_flows}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with kpi2:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Normal Flows</div>
            <div class="metric-value">{normal_count}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with kpi3:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Attack Flows</div>
            <div class="metric-value">{attack_count}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with kpi4:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">Attack Ratio</div>
            <div class="metric-value">{attack_ratio}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# SIDEBAR
# ==================================================
st.sidebar.title("🧠 Control Panel")
st.sidebar.markdown("Choose a scenario and test the AI detector.")

traffic_profile = st.sidebar.radio(
    "Traffic Profile",
    ["Attack-like traffic", "Normal traffic", "Custom input"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Technology Stack")
st.sidebar.write("Python")
st.sidebar.write("Pandas")
st.sidebar.write("Scikit-learn")
st.sidebar.write("Random Forest")
st.sidebar.write("Plotly")
st.sidebar.write("Streamlit")

st.sidebar.markdown("---")
st.sidebar.markdown("### Model Classes")
st.sidebar.write("Normal")
st.sidebar.write("Attack")


# ==================================================
# DEFAULT INPUT VALUES
# ==================================================
if traffic_profile == "Attack-like traffic":
    default_values = {
        "duration": 0.4,
        "src_bytes": 220.0,
        "dst_bytes": 90.0,
        "packet_count": 210.0,
        "flow_rate": 360.0,
        "error_rate": 0.15
    }
elif traffic_profile == "Normal traffic":
    default_values = {
        "duration": 3.2,
        "src_bytes": 900.0,
        "dst_bytes": 1200.0,
        "packet_count": 28.0,
        "flow_rate": 22.0,
        "error_rate": 0.03
    }
else:
    default_values = {
        "duration": 1.0,
        "src_bytes": 500.0,
        "dst_bytes": 500.0,
        "packet_count": 80.0,
        "flow_rate": 100.0,
        "error_rate": 0.10
    }


# ==================================================
# TABS
# ==================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "🔍 Live Detection",
        "📊 Model Results",
        "🧬 Feature Analysis",
        "📈 Visual Analytics",
        "📁 Project Summary"
    ]
)


# ==================================================
# TAB 1: LIVE DETECTION
# ==================================================
with tab1:
    st.markdown(
        '<div class="section-title">🔍 Live Network Traffic Detection</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">
        Enter network traffic values below. The trained AI model will analyse the flow
        and classify it as either normal traffic or suspicious attack-like behaviour.
        </div>
        """,
        unsafe_allow_html=True
    )

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        duration = st.number_input(
            "Duration",
            min_value=0.0,
            value=default_values["duration"],
            step=0.1,
            key="duration_input"
        )

        src_bytes = st.number_input(
            "Source Bytes",
            min_value=0.0,
            value=default_values["src_bytes"],
            step=10.0,
            key="src_bytes_input"
        )

    with col_b:
        dst_bytes = st.number_input(
            "Destination Bytes",
            min_value=0.0,
            value=default_values["dst_bytes"],
            step=10.0,
            key="dst_bytes_input"
        )

        packet_count = st.number_input(
            "Packet Count",
            min_value=0.0,
            value=default_values["packet_count"],
            step=1.0,
            key="packet_count_input"
        )

    with col_c:
        flow_rate = st.number_input(
            "Flow Rate",
            min_value=0.0,
            value=default_values["flow_rate"],
            step=1.0,
            key="flow_rate_input"
        )

        error_rate = st.number_input(
            "Error Rate",
            min_value=0.0,
            max_value=1.0,
            value=default_values["error_rate"],
            step=0.01,
            key="error_rate_input"
        )

    sample = pd.DataFrame([{
        "duration": duration,
        "src_bytes": src_bytes,
        "dst_bytes": dst_bytes,
        "packet_count": packet_count,
        "flow_rate": flow_rate,
        "error_rate": error_rate
    }])

    st.markdown("### Current Network Flow")
    st.dataframe(sample, width="stretch")

    if st.button("🚀 Run AI Detection", type="primary"):
        prediction = model.predict(sample)[0]
        label = encoder.inverse_transform([prediction])[0]
        probabilities = model.predict_proba(sample)[0]

        probability_df = pd.DataFrame({
            "Class": encoder.classes_,
            "Probability": probabilities
        })

        attack_probability = float(
            probability_df.loc[
                probability_df["Class"] == "Attack",
                "Probability"
            ].values[0]
        )

        st.markdown("### Detection Result")

        if label == "Attack":
            st.markdown(
                """
                <div class="attack-card">
                    ⚠️ ALERT: Suspicious Network Attack Detected
                </div>
                """,
                unsafe_allow_html=True
            )
            st.warning(
                "Suggested action: inspect the source flow, monitor repeated packets, "
                "check abnormal flow rate, and consider blocking or rate-limiting this traffic."
            )
        else:
            st.markdown(
                """
                <div class="normal-card">
                    ✅ SAFE: Normal Network Traffic
                </div>
                """,
                unsafe_allow_html=True
            )
            st.success(
                "Suggested action: no immediate security action is required."
            )

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=attack_probability * 100,
                title={"text": "Attack Probability"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#EF4444"},
                    "steps": [
                        {"range": [0, 35], "color": "#064E3B"},
                        {"range": [35, 70], "color": "#92400E"},
                        {"range": [70, 100], "color": "#7F1D1D"},
                    ],
                },
            )
        )

        gauge.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font={"color": "white"},
            height=330
        )

        st.plotly_chart(gauge, width="stretch")

        st.markdown("### Prediction Confidence")
        fig_prob = px.bar(
            probability_df,
            x="Class",
            y="Probability",
            title="Prediction Confidence by Class",
            text="Probability"
        )
        fig_prob.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="white"
        )
        st.plotly_chart(fig_prob, width="stretch")


# ==================================================
# TAB 2: MODEL RESULTS
# ==================================================
with tab2:
    st.markdown(
        '<div class="section-title">📊 Model Evaluation Results</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">
        This section shows the performance of the trained machine learning model.
        Since this first version uses synthetic data, the result is expected to be very high.
        </div>
        """,
        unsafe_allow_html=True
    )

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("### Confusion Matrix")
        if os.path.exists("results/confusion_matrix.png"):
            st.image("results/confusion_matrix.png")
        else:
            st.info("Confusion matrix not found. Run: python .\\src\\train_model.py")

    with col_right:
        st.markdown("### Classification Report")
        if os.path.exists("results/classification_report.txt"):
            with open("results/classification_report.txt", "r") as f:
                st.code(f.read())
        else:
            st.info("Classification report not found. Run: python .\\src\\train_model.py")


# ==================================================
# TAB 3: FEATURE ANALYSIS
# ==================================================
with tab3:
    st.markdown(
        '<div class="section-title">🧬 Feature Importance Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">
        Feature importance explains which network traffic features were most useful
        for the AI model when separating normal and suspicious traffic.
        </div>
        """,
        unsafe_allow_html=True
    )

    col_f1, col_f2 = st.columns(2)

    with col_f1:
        st.markdown("### Feature Importance Plot")
        if os.path.exists("results/feature_importance.png"):
            st.image("results/feature_importance.png")
        else:
            st.info("Feature importance plot not found. Run training first.")

    with col_f2:
        st.markdown("### Feature Importance Table")
        if os.path.exists("results/feature_importance.csv"):
            importance_df = pd.read_csv("results/feature_importance.csv")
            st.dataframe(importance_df, width="stretch")
        else:
            st.info("Feature importance table not found. Run training first.")

    st.markdown("### Feature Relationship Scatter Plot")

    fig_scatter = px.scatter(
        df,
        x="packet_count",
        y="flow_rate",
        color="label",
        size="error_rate",
        hover_data=["duration", "src_bytes", "dst_bytes"],
        title="Packet Count vs Flow Rate"
    )

    fig_scatter.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white"
    )

    st.plotly_chart(fig_scatter, width="stretch")


# ==================================================
# TAB 4: VISUAL ANALYTICS
# ==================================================
with tab4:
    st.markdown(
        '<div class="section-title">📈 Visual Analytics Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">
        This section makes the project look closer to a real cybersecurity monitoring tool.
        It visualizes traffic distribution, attack patterns, risk levels, and simulated live traffic.
        </div>
        """,
        unsafe_allow_html=True
    )

    visual_col1, visual_col2 = st.columns(2)

    with visual_col1:
        class_counts = df["label"].value_counts().reset_index()
        class_counts.columns = ["Traffic Class", "Count"]

        fig_donut = px.pie(
            class_counts,
            names="Traffic Class",
            values="Count",
            hole=0.55,
            title="Traffic Class Distribution"
        )

        fig_donut.update_traces(textinfo="percent+label")
        fig_donut.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="white"
        )

        st.plotly_chart(fig_donut, width="stretch")

    with visual_col2:
        risk_path = "results/risk_summary.csv"

        if os.path.exists(risk_path):
            risk_df = pd.read_csv(risk_path)
        else:
            risk_df = pd.DataFrame({
                "risk_level": ["Normal", "Low Risk", "Medium Risk", "High Risk"],
                "count": [72, 14, 9, 5]
            })

        fig_risk = px.bar(
            risk_df,
            x="risk_level",
            y="count",
            title="Traffic Risk Summary",
            text="count"
        )

        fig_risk.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="white",
            xaxis_title="Risk Level",
            yaxis_title="Number of Flows"
        )

        st.plotly_chart(fig_risk, width="stretch")

    st.markdown("### Simulated Real-Time Network Traffic")

    timeline_path = "results/live_traffic_timeline.csv"

    if os.path.exists(timeline_path):
        timeline_df = pd.read_csv(timeline_path)
        timeline_df["time"] = pd.to_datetime(timeline_df["time"])
    else:
        np.random.seed(42)
        time_points = pd.date_range(
            start="2026-06-09 10:00",
            periods=120,
            freq="min"
        )
        traffic_volume = np.random.normal(50, 8, 120)
        traffic_volume[20:28] += 70
        traffic_volume[55:65] += 95
        traffic_volume[90:96] += 60

        timeline_df = pd.DataFrame({
            "time": time_points,
            "traffic_volume": traffic_volume
        })

    fig_line = px.line(
        timeline_df,
        x="time",
        y="traffic_volume",
        title="Network Traffic Volume with Suspicious Spikes"
    )

    fig_line.update_traces(line_width=3)

    fig_line.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        xaxis_title="Time",
        yaxis_title="Traffic Volume"
    )

    st.plotly_chart(fig_line, width="stretch")

    st.markdown("### Correlation Heatmap")

    if os.path.exists("results/correlation_heatmap.png"):
        st.image("results/correlation_heatmap.png")
    else:
        st.info("Correlation heatmap not found. Run: python .\\src\\create_visuals.py")


# ==================================================
# TAB 5: PROJECT SUMMARY
# ==================================================
with tab5:
    st.markdown(
        '<div class="section-title">📁 Project Summary</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">
        <b>NetGuard-AI</b> is a machine learning project for intelligent network security.
        It demonstrates how network traffic features can be used to detect suspicious behaviour
        and present the result through a professional cybersecurity dashboard.
        </div>
        """,
        unsafe_allow_html=True
    )

    s1, s2, s3 = st.columns(3)

    with s1:
        st.markdown(
            """
            <div class="mini-card">
            <h3>🎯 Goal</h3>
            Detect abnormal network flows using AI and machine learning.
            </div>
            """,
            unsafe_allow_html=True
        )

    with s2:
        st.markdown(
            """
            <div class="mini-card">
            <h3>🧠 Method</h3>
            Train a Random Forest classifier using network traffic features.
            </div>
            """,
            unsafe_allow_html=True
        )

    with s3:
        st.markdown(
            """
            <div class="mini-card">
            <h3>🛡️ Output</h3>
            Classify traffic as Normal or Attack and visualize the result.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### Features Used by the Model")

    features = pd.DataFrame({
        "Feature": [
            "duration",
            "src_bytes",
            "dst_bytes",
            "packet_count",
            "flow_rate",
            "error_rate"
        ],
        "Meaning": [
            "How long the network flow lasts",
            "Bytes sent by the source",
            "Bytes received by the destination",
            "Number of packets in the flow",
            "Traffic speed or packet sending rate",
            "Abnormal or failed traffic ratio"
        ]
    })

    st.dataframe(features, width="stretch")

    st.markdown("### Future Improvements")

    future_work = pd.DataFrame({
        "Next Step": [
            "Real dataset integration",
            "Multi-class attack detection",
            "Live packet capture",
            "SDN controller integration",
            "Automatic mitigation",
            "Cloud deployment"
        ],
        "Description": [
            "Use CIC-IDS2017 or UNSW-NB15",
            "Detect DDoS, PortScan, BruteForce, Botnet",
            "Capture live packets using Scapy",
            "Use Mininet and Ryu controller",
            "Automatically block suspicious flows",
            "Deploy dashboard online"
        ]
    })

    st.dataframe(future_work, width="stretch")


st.markdown(
    """
    <div class="footer-text">
    Built by Aqib Mushtaq | Networking | AI | Cybersecurity | Data Analysis
    </div>
    """,
    unsafe_allow_html=True
)