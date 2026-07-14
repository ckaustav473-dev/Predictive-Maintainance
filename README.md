# 🏭 Predictive Maintenance and Anomaly Detection in 6G-Integrated Smart Manufacturing Systems

## 📌 Project Overview

This project develops an AI-powered predictive maintenance system for 6G-enabled smart manufacturing environments. The system analyzes real-time machine sensor data to detect abnormal operating conditions, identify high-risk machines, and support preventive maintenance decisions before failures occur.

The solution uses **Isolation Forest** for anomaly detection, feature engineering to capture machine behavior, and an interactive **Streamlit dashboard** for visualization and decision support.

---

# 🎯 Objectives

- Detect abnormal machine behavior using machine learning.
- Identify machines requiring preventive maintenance.
- Classify maintenance risk into Low, Medium, and High.
- Visualize machine health using an interactive dashboard.
- Reduce unexpected downtime and maintenance costs.

---

# 📂 Dataset

Dataset Name:

**Thales_Group_Manufacturing.csv**

The dataset contains manufacturing sensor information including:

- Date
- Timestamp
- Machine_ID
- Operation_Mode
- Temperature_C
- Vibration_Hz
- Power_Consumption_kW
- Network_Latency_ms
- Packet_Loss_%
- Quality_Control_Defect_Rate_%
- Production_Speed_units_per_hr
- Predictive_Maintenance_Score
- Error_Rate_%
- Efficiency_Status

---

# ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Streamlit
- Joblib

---

# 📊 Machine Learning Model

Algorithm Used:

**Isolation Forest**

Purpose:

- Detect anomalous machine behavior
- Generate anomaly scores
- Identify high-risk assets
- Support predictive maintenance

---

# 🔧 Feature Engineering

The following engineered features were created:

- Rolling Temperature
- Rolling Vibration
- Rolling Power Consumption
- Rolling Error Rate
- Temperature Deviation
- Vibration Deviation
- Power Deviation
- Error Deviation
- Vibration-to-Power Ratio
- Maintenance Score Decay
- Error Trend
- Production Efficiency

---

# 📈 Dashboard Features

The Streamlit dashboard provides:

### Dashboard Overview

- Total Machines
- High Risk Machines
- Medium Risk Machines
- Low Risk Machines
- Average Anomaly Score
- Average Maintenance Score

### Machine Analysis

- Temperature Trend
- Vibration Trend
- Power Consumption Trend
- Error Rate Trend
- Anomaly Score Trend

### Sensor Analysis

- Temperature vs Vibration
- Power vs Error Rate
- Production Speed Analysis
- Network Latency Distribution
- Packet Loss Distribution

### Maintenance Panel

- High Risk Machine List
- Maintenance Alerts
- Inspection Priority

### Historical Analysis

- Risk Trend
- Maintenance Score Trend
- Top 10 Critical Machines

### Export

- Download Filtered Dataset

---

# 📁 Project Structure

```
Predictive_Maintenance/
│
├── app.py
├── feature_engineering.py
├── train_model.py
├── final_manufacturing.csv
├── processed_manufacturing.csv
├── isolation_forest.pkl
├── requirements.txt
├── README.md
```

---

# 🚀 Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Execute feature engineering:

```bash
python feature_engineering.py
```

Train the model:

```bash
python train_model.py
```

Launch the dashboard:

```bash
streamlit run app.py
```

---

# 📊 Key Performance Indicators (KPIs)

- Anomaly Score
- Maintenance Risk Level
- High Risk Machine Count
- Average Maintenance Score
- Average Anomaly Score
- Downtime Prevention Indicator
- Historical Risk Trend

---

# 💡 Business Benefits

- Early detection of abnormal machine behavior.
- Reduction in unexpected equipment failures.
- Improved maintenance scheduling.
- Lower maintenance costs.
- Increased production efficiency.
- Better utilization of manufacturing resources.

---

# 📚 Future Enhancements

- Autoencoder-based anomaly detection.
- Real-time IoT data streaming.
- Predictive Remaining Useful Life (RUL) estimation.
- Cloud deployment.
- Email and SMS maintenance alerts.
- Integration with enterprise maintenance systems.

---

# 👨‍💻 Author

**Name:** *Kaustav Chakraborty*

Project:
**Predictive Maintenance and Anomaly Detection in 6G-Integrated Smart Manufacturing Systems**

---

# 📄 License

This project was developed for academic and educational purposes.
