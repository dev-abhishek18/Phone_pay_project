import streamlit as st
import pandas as pd
import pyodbc
import plotly.express as px
import json
import seaborn as sns
import matplotlib.pyplot as plt

# FULL SCREEN CONFIG
st.set_page_config(layout="wide")

st.markdown("""
<style>
    .block-container { max-width: 100% !important; }
    .kpi-card {
        background: #f7f7f7;
        padding: 14px;
        border-radius: 10px;
        text-align: center;
    }
    .kpi-value {
        font-size: 26px;
        font-weight: bold;
        margin-top: -8px;
    }
</style>
""", unsafe_allow_html=True)

# TITLE
st.title("📱 PhonePe Transaction Insights Dashboard")

# SQL CONNECTION
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-NSAHO9N\\SQLSERVER2019;"
    "DATABASE=phonepe_db;"
    "UID=sa;"
    "PWD=ISS;"
)

df = pd.read_sql("SELECT * FROM aggregated_transaction", conn)

# LOAD GEOJSON
with open("dashboard/india_state.geojson", "r") as f:
    india_geo = json.load(f)

for f in india_geo["features"]:
    f["properties"]["NAME_1"] = f["properties"]["NAME_1"].upper()

# STATE NAME MAPPING
state_fix = {
    "andaman-&-nicobar-islands": "ANDAMAN AND NICOBAR",
    "andhra-pradesh": "ANDHRA PRADESH",
    "arunachal-pradesh": "ARUNACHAL PRADESH",
    "assam": "ASSAM",
    "bihar": "BIHAR",
    "chandigarh": "CHANDIGARH",
    "chhattisgarh": "CHHATTISGARH",
    "dadra-&-nagar-haveli-&-daman-&-diu": "DADRA AND NAGAR HAVELI",
    "delhi": "DELHI",
    "goa": "GOA",
    "gujarat": "GUJARAT",
    "haryana": "HARYANA",
    "himachal-pradesh": "HIMACHAL PRADESH",
    "jammu-&-kashmir": "JAMMU AND KASHMIR",
    "jharkhand": "JHARKHAND",
    "karnataka": "KARNATAKA",
    "kerala": "KERALA",
    "ladakh": "LADAKH",
    "lakshadweep": "LAKSHADWEEP",
    "madhya-pradesh": "MADHYA PRADESH",
    "maharashtra": "MAHARASHTRA",
    "manipur": "MANIPUR",
    "meghalaya": "MEGHALAYA",
    "mizoram": "MIZORAM",
    "nagaland": "NAGALAND",
    "odisha": "ODISHA",
    "puducherry": "PUDUCHERRY",
    "punjab": "PUNJAB",
    "rajasthan": "RAJASTHAN",
    "sikkim": "SIKKIM",
    "tamil-nadu": "TAMIL NADU",
    "telangana": "TELANGANA",
    "tripura": "TRIPURA",
    "uttar-pradesh": "UTTAR PRADESH",
    "uttarakhand": "UTTARAKHAND",
    "west-bengal": "WEST BENGAL"
}

# ------------------ FILTERS -------------------
filter_col, map_col = st.columns([1.2, 5])

with filter_col:
    years = sorted(df["year"].unique())
    selected_year = st.selectbox("Select Year", years)

    quarters = [1, 2, 3, 4]
    selected_quarter = st.selectbox("Select Quarter", quarters)

# ------------------ FILTER DATA -------------------
df_filtered = df[(df["year"] == selected_year) & (df["quarter"] == selected_quarter)]

# ------------------ KPI CARDS -------------------
st.markdown("### ⭐ Key Metrics")

k1, k2, k3, k4 = st.columns(4)

total_txn = df_filtered["count"].sum()
total_amt = df_filtered["amount"].sum()
avg_val = total_amt / total_txn if total_txn else 0
states = df_filtered['region'].nunique()

k1.markdown(f"<div class='kpi-card'>Total Transactions<br><div class='kpi-value'>{total_txn:,}</div></div>", unsafe_allow_html=True)
k2.markdown(f"<div class='kpi-card'>Total Amount<br><div class='kpi-value'>₹{total_amt:,.0f}</div></div>", unsafe_allow_html=True)
k3.markdown(f"<div class='kpi-card'>Avg Txn Value<br><div class='kpi-value'>₹{avg_val:,.0f}</div></div>", unsafe_allow_html=True)
k4.markdown(f"<div class='kpi-card'>States Covered<br><div class='kpi-value'>{states}</div></div>", unsafe_allow_html=True)

# ------------------ MAP DATA -------------------
df_summary = df_filtered.groupby("region").agg(
    total_txn=("count", "sum"),
    total_amount=("amount", "sum")
).reset_index()

df_summary["avg_txn_value"] = df_summary["total_amount"] / df_summary["total_txn"]
df_summary["region_map"] = df_summary["region"].str.lower().map(state_fix)

# ------------------ INDIA MAP -------------------
st.markdown(f"### 🗺️ India Map — Year {selected_year}, Q{selected_quarter}")

fig_map = px.choropleth(
    df_summary,
    geojson=india_geo,
    locations="region_map",
    featureidkey="properties.NAME_1",
    color="total_amount",
    color_continuous_scale="Purples",
    hover_name="region",
    hover_data=["total_txn", "total_amount", "avg_txn_value"]
)

fig_map.update_geos(fitbounds="locations", visible=False)
fig_map.update_layout(height=650, margin=dict(l=0, r=0, t=0, b=0))

st.plotly_chart(fig_map, use_container_width=True)

# ------------------ YEARLY TREND -------------------
st.markdown("### 📊 Yearly Trend by State")

state_list = ["ALL INDIA"] + sorted(df["region"].unique())
selected_state = st.selectbox("Select State", state_list)

if selected_state == "ALL INDIA":
    df_chart = df.groupby("year").agg({"amount": "sum"}).reset_index()
else:
    df_chart = df[df["region"] == selected_state].groupby("year").agg({"amount": "sum"}).reset_index()

fig_bar = px.bar(
    df_chart, x="year", y="amount", text_auto=True,
    title=f"Yearly Transaction Trend — {selected_state}"
)

st.plotly_chart(fig_bar, use_container_width=True)

# ------------------ EDA SECTION -------------------
st.markdown("## 🧪 Exploratory Data Analysis (EDA)")
st.write("Explore distribution, category analysis, and correlations in the dataset.")

eda_tab1, eda_tab2, eda_tab3, eda_tab4 = st.tabs([
    "Amount Distribution",
    "Transaction Count Distribution",
    "Category-wise Analysis",
    "Correlation Heatmap"
])

# 1 — Amount Distribution
with eda_tab1:
    st.subheader("📦 Distribution of Transaction Amount")
    fig = px.histogram(df, x="amount", nbins=50, color_discrete_sequence=["#6A5ACD"])
    st.plotly_chart(fig, use_container_width=True)

# 2 — Transaction Count Distribution
with eda_tab2:
    st.subheader("📊 Distribution of Transaction Count")
    fig = px.histogram(df, x="count", nbins=50, color_discrete_sequence=["#20B2AA"])
    st.plotly_chart(fig, use_container_width=True)

# 3 — Category-wise Analysis
with eda_tab3:
    st.subheader("🏷️ Category-wise Transaction Amount")
    df_cat = df.groupby("category")["amount"].sum().reset_index()
    fig = px.bar(
        df_cat, x="category", y="amount", text_auto=True,
        color="category", color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig, use_container_width=True)

# 4 — Correlation Heatmap
with eda_tab4:
    st.subheader("🔥 Correlation Heatmap")
    corr = df[["count", "amount", "year", "quarter"]].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="Purples", ax=ax)
    st.pyplot(fig)
