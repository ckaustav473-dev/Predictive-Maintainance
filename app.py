import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Predictive Maintenance Dashboard",
    page_icon="🏭",
    layout="wide"
)

st.title("🏭 Predictive Maintenance & Anomaly Detection")
st.markdown("### 6G Integrated Smart Manufacturing")

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv("final_manufacturing_small.csv")

    # Show column names while debugging
    st.write("Columns:", df.columns.tolist())

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(
            df["Date"],
            format="mixed",
            errors="coerce"
        )

    if "DateTime" in df.columns:
        df["DateTime"] = pd.to_datetime(
            df["DateTime"],
            format="mixed",
            errors="coerce"
        )

    return df
df = load_data()

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

st.sidebar.header("Filters")

machine = st.sidebar.selectbox(
    "Machine",
    ["All"] + sorted(df["Machine_ID"].unique().tolist())
)

operation = st.sidebar.multiselect(
    "Operation Mode",
    sorted(df["Operation_Mode"].unique()),
    default=sorted(df["Operation_Mode"].unique())
)

risk = st.sidebar.multiselect(
    "Maintenance Risk",
    ["Low","Medium","High"],
    default=["Low","Medium","High"]
)

score = st.sidebar.slider(
    "Minimum Anomaly Score",
    0.0,
    1.0,
    0.0
)

# -------------------------------------------------------
# Apply Filters
# -------------------------------------------------------

filtered = df.copy()

if machine != "All":
    filtered = filtered[
        filtered["Machine_ID"] == machine
    ]

filtered = filtered[
    filtered["Operation_Mode"].isin(operation)
]

filtered = filtered[
    filtered["Maintenance_Risk"].isin(risk)
]

filtered = filtered[
    filtered["Anomaly_Score"] >= score
]

# -------------------------------------------------------
# KPIs
# -------------------------------------------------------

total = filtered["Machine_ID"].nunique()

high = filtered[
    filtered["Maintenance_Risk"]=="High"
]["Machine_ID"].nunique()

medium = filtered[
    filtered["Maintenance_Risk"]=="Medium"
]["Machine_ID"].nunique()

low = filtered[
    filtered["Maintenance_Risk"]=="Low"
]["Machine_ID"].nunique()

avg_score = filtered["Anomaly_Score"].mean()

avg_maint = filtered[
    "Predictive_Maintenance_Score"
].mean()

c1,c2,c3,c4,c5,c6 = st.columns(6)

c1.metric("Machines", total)

c2.metric("High Risk", high)

c3.metric("Medium Risk", medium)

c4.metric("Low Risk", low)

c5.metric(
    "Avg Anomaly",
    round(avg_score,3)
)

c6.metric(
    "Maintenance Score",
    round(avg_maint,2)
)

st.divider()

# -------------------------------------------------------
# Risk Distribution
# -------------------------------------------------------

left,right = st.columns(2)

risk_df = (
    filtered["Maintenance_Risk"]
    .value_counts()
    .reset_index()
)

risk_df.columns=[
    "Risk",
    "Count"
]

fig = px.pie(
    risk_df,
    names="Risk",
    values="Count",
    hole=.45,
    title="Maintenance Risk Distribution"
)

left.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------------------------------------
# Efficiency Status
# -------------------------------------------------------

eff = (
    filtered["Efficiency_Status"]
    .value_counts()
    .reset_index()
)

eff.columns=[
    "Efficiency",
    "Count"
]

fig = px.bar(
    eff,
    x="Efficiency",
    y="Count",
    color="Efficiency",
    title="Efficiency Status"
)

right.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# -------------------------------------------------------
# Sensor Overview
# -------------------------------------------------------

sensor = filtered[
[
"Temperature_C",
"Vibration_Hz",
"Power_Consumption_kW",
"Network_Latency_ms",
"Packet_Loss_%"
]
].mean().reset_index()

sensor.columns=[
    "Sensor",
    "Average"
]

fig = px.bar(
    sensor,
    x="Sensor",
    y="Average",
    title="Average Sensor Values"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------------------------------------
# Correlation
# -------------------------------------------------------

corr = filtered[
[
"Temperature_C",
"Vibration_Hz",
"Power_Consumption_kW",
"Predictive_Maintenance_Score",
"Error_Rate_%",
"Anomaly_Score"
]
].corr()

fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    title="Correlation Heatmap"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()
# ==========================================================
# MACHINE ANALYSIS
# ==========================================================

st.header("🏭 Machine Analysis Dashboard")

machine_df = filtered.copy()

# ----------------------------------------------------------
# Temperature Trend
# ----------------------------------------------------------

st.subheader("Temperature Trend")

fig = px.line(
    machine_df,
    x="DateTime",
    y="Temperature_C",
    color="Machine_ID",
    title="Machine Temperature"
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------------
# Vibration Trend
# ----------------------------------------------------------

st.subheader("Vibration Trend")

fig = px.line(
    machine_df,
    x="DateTime",
    y="Vibration_Hz",
    color="Machine_ID",
    title="Machine Vibration"
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------------
# Power Consumption
# ----------------------------------------------------------

st.subheader("Power Consumption")

fig = px.line(
    machine_df,
    x="DateTime",
    y="Power_Consumption_kW",
    color="Machine_ID",
    title="Power Consumption"
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------------
# Error Rate
# ----------------------------------------------------------

st.subheader("Error Rate")

fig = px.line(
    machine_df,
    x="DateTime",
    y="Error_Rate_%",
    color="Machine_ID",
    title="Machine Error Rate"
)

st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------------
# Anomaly Score Trend
# ----------------------------------------------------------

st.subheader("Anomaly Score Trend")

fig = px.line(
    machine_df,
    x="DateTime",
    y="Anomaly_Score",
    color="Machine_ID",
    title="Anomaly Score"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# SENSOR COMPARISON
# ==========================================================

st.header("📊 Sensor Comparison")

col1, col2 = st.columns(2)

with col1:

    fig = px.scatter(
        machine_df,
        x="Temperature_C",
        y="Vibration_Hz",
        color="Maintenance_Risk",
        size="Anomaly_Score",
        hover_data=["Machine_ID"],
        title="Temperature vs Vibration"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.scatter(
        machine_df,
        x="Power_Consumption_kW",
        y="Error_Rate_%",
        color="Maintenance_Risk",
        size="Anomaly_Score",
        hover_data=["Machine_ID"],
        title="Power vs Error Rate"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# PRODUCTION ANALYSIS
# ==========================================================

st.header("⚙️ Production Analysis")

fig = px.box(
    machine_df,
    x="Operation_Mode",
    y="Production_Speed_units_per_hr",
    color="Operation_Mode",
    title="Production Speed by Operation Mode"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# NETWORK ANALYSIS
# ==========================================================

st.header("📡 6G Network Performance")

left, right = st.columns(2)

with left:

    fig = px.histogram(
        machine_df,
        x="Network_Latency_ms",
        nbins=30,
        title="Network Latency"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    fig = px.histogram(
        machine_df,
        x="Packet_Loss_%",
        nbins=30,
        title="Packet Loss"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# MACHINE PERFORMANCE TABLE
# ==========================================================

st.header("📋 Machine Performance Summary")

summary = (

    machine_df

    .groupby("Machine_ID")

    .agg({

        "Temperature_C":"mean",

        "Vibration_Hz":"mean",

        "Power_Consumption_kW":"mean",

        "Error_Rate_%":"mean",

        "Anomaly_Score":"mean",

        "Predictive_Maintenance_Score":"mean"

    })

    .reset_index()

)

summary = summary.sort_values(
    "Anomaly_Score",
    ascending=False
)

st.dataframe(
    summary,
    use_container_width=True
)
# ==========================================================
# PART C : Maintenance Alerts & Historical Analysis
# ==========================================================

st.header("🚨 Maintenance Alert Panel")

# ----------------------------------------------------------
# High Risk Machines
# ----------------------------------------------------------

high_risk_df = filtered[
    filtered["Maintenance_Risk"] == "High"
]

if len(high_risk_df) > 0:

    st.error(f"⚠ {high_risk_df['Machine_ID'].nunique()} High-Risk Machines Detected")

    alert_table = high_risk_df[
        [
            "Machine_ID",
            "DateTime",
            "Temperature_C",
            "Vibration_Hz",
            "Power_Consumption_kW",
            "Error_Rate_%",
            "Predictive_Maintenance_Score",
            "Anomaly_Score",
            "Maintenance_Risk"
        ]
    ].sort_values("Anomaly_Score", ascending=False)

    st.dataframe(alert_table, use_container_width=True)

else:
    st.success("✅ No High Risk Machines Found")

st.divider()

# ==========================================================
# TOP 10 CRITICAL MACHINES
# ==========================================================

st.header("🏆 Top 10 Critical Machines")

top10 = (

    filtered

    .groupby("Machine_ID")["Anomaly_Score"]

    .mean()

    .sort_values(ascending=False)

    .head(10)

    .reset_index()

)

fig = px.bar(
    top10,
    x="Machine_ID",
    y="Anomaly_Score",
    color="Anomaly_Score",
    title="Top 10 High-Risk Machines"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# HISTORICAL RISK ANALYSIS
# ==========================================================

st.header("📈 Historical Risk Analysis")

risk_history = (

    filtered

    .groupby("Date")["Anomaly_Score"]

    .mean()

    .reset_index()

)

fig = px.line(
    risk_history,
    x="Date",
    y="Anomaly_Score",
    markers=True,
    title="Average Anomaly Score Over Time"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# MAINTENANCE SCORE TREND
# ==========================================================

maint = (

    filtered

    .groupby("Date")["Predictive_Maintenance_Score"]

    .mean()

    .reset_index()

)

fig = px.line(
    maint,
    x="Date",
    y="Predictive_Maintenance_Score",
    markers=True,
    title="Maintenance Score Trend"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# TEMPERATURE DISTRIBUTION
# ==========================================================

st.header("🌡 Temperature Distribution")

fig = px.histogram(
    filtered,
    x="Temperature_C",
    nbins=40,
    color="Maintenance_Risk",
    title="Temperature Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# VIBRATION DISTRIBUTION
# ==========================================================

fig = px.histogram(
    filtered,
    x="Vibration_Hz",
    nbins=40,
    color="Maintenance_Risk",
    title="Vibration Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# DOWNLOAD DATASET
# ==========================================================

st.header("📥 Download Filtered Dataset")

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="Filtered_Manufacturing_Data.csv",
    mime="text/csv"
)

st.divider()

# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

st.header("📄 Executive Summary")

st.markdown(f"""
### Project Insights

- **Total Machines:** {total}
- **High Risk Machines:** {high}
- **Medium Risk Machines:** {medium}
- **Low Risk Machines:** {low}

### Recommendations

- Prioritize inspection of High-Risk machines.
- Monitor increasing anomaly scores to prevent unexpected failures.
- Track temperature and vibration jointly for early warning.
- Review machines with declining predictive maintenance scores.
- Use anomaly trends to schedule preventive maintenance and reduce downtime.

""")

st.success("🎉 Predictive Maintenance Dashboard Loaded Successfully!")
