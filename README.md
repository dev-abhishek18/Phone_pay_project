# PhonePe Transaction Insights Dashboard

> **End-to-end Data Analytics project using Python, SQL Server, Streamlit and Plotly to analyze digital payment activity across India.**

## 📌 Project Overview

This project analyzes the **PhonePe Pulse** dataset to understand how digital payment activity changes across Indian states, years, quarters and transaction categories.

The project demonstrates a practical Data Analyst workflow:

**Raw JSON Data → ETL → SQL Server → Analysis → Interactive Dashboard → Business Insights**

The final application allows users to explore transaction volume, transaction value, state-level performance and category-level patterns through interactive filters and visualizations.

---

## 🎯 Business Problem

Digital-payment platforms generate large volumes of geographically distributed transaction data. Business teams need an easy way to understand:

- Which states contribute the most transaction value?
- How does payment activity change over time?
- Which transaction categories contribute most to total value?
- How does average transaction value vary by state?
- How do selected years and quarters affect the market picture?

This project converts structured PhonePe Pulse data into an interactive analytical dashboard to answer these questions.

---

## 🔎 Key Analytical Questions

1. What is the total transaction volume for a selected year and quarter?
2. What is the total transaction amount for the selected period?
3. What is the average transaction value?
4. How many states are represented in the selected period?
5. Which states contribute the highest transaction amounts?
6. How does transaction value change year over year?
7. How does a selected state's transaction value change over time?
8. Which transaction categories contribute the most value?
9. What does the distribution of transaction amounts look like?
10. What relationships exist among transaction count, amount, year and quarter?

---

## 🛠️ Tech Stack

| Area | Tools |
|---|---|
| Data Source | PhonePe Pulse JSON dataset |
| Programming | Python |
| Data Processing | Pandas |
| Database | Microsoft SQL Server |
| Database Connectivity | PyODBC |
| Dashboard | Streamlit |
| Visualization | Plotly, Matplotlib, Seaborn |
| Geographic Visualization | GeoJSON + Plotly Choropleth |
| Version Control | Git, GitHub |

---

## 📊 Dataset

The project uses the **PhonePe Pulse** dataset stored in the repository under `data/pulse-master`.

The dashboard reads the `aggregated_transaction` table from SQL Server. The analytical fields used by the application include:

- `year`
- `quarter`
- `region`
- `count`
- `amount`
- `category`

These fields support time-series, geographic, category and KPI analysis.

---

## 🔄 End-to-End Data Workflow

```text
PhonePe Pulse JSON Data
        ↓
Data Extraction / ETL
        ↓
SQL Server
        ↓
Aggregated Transaction Data
        ↓
Python + Pandas Analysis
        ↓
Streamlit + Plotly Dashboard
        ↓
Business Insights
```

### 1. Data Collection

The repository contains PhonePe Pulse JSON data organized by year and quarter. These source files provide the foundation for the transaction analysis.

### 2. ETL & SQL Storage

The project uses Python and SQL Server to organize the source data into structured analytical tables. The dashboard consumes transaction-level aggregates from SQL Server.

### 3. Data Preparation

The application performs analysis using Pandas and includes state-name standardization so that state data can be matched correctly with the India GeoJSON map.

### 4. Dashboard Development

Streamlit provides the interactive application layer, while Plotly is used for the map and charts.

---

## 📈 Dashboard Features

### KPI Cards

For the selected **Year + Quarter**, the dashboard calculates:

- **Total Transactions**
- **Total Transaction Amount**
- **Average Transaction Value**
- **States Covered**

### 🗺️ India State-Level Map

An interactive choropleth map displays transaction amount by state for the selected year and quarter.

Hover details include:

- State
- Total transactions
- Total amount
- Average transaction value

### 📊 Yearly Trend Analysis

Users can select **All India** or an individual state to compare transaction amount across years.

### 🏷️ Category Analysis

The dashboard aggregates transaction amount by category to show how different payment categories contribute to overall transaction value.

### 🧪 EDA Section

The application includes four exploratory-analysis views:

- Transaction amount distribution
- Transaction count distribution
- Category-wise transaction amount
- Correlation heatmap for count, amount, year and quarter

---

## 💡 Business Insights the Dashboard Supports

The analysis can be used to identify:

- Geographic concentration of digital-payment activity
- Growth or decline in transaction value over time
- High-value states and categories
- Differences between transaction volume and transaction value
- Period-specific changes across quarters
- Relationships between transaction count and transaction amount

> **Note:** Exact KPI values are intentionally not hard-coded into this README because they depend on the selected dashboard filters.

---

## 🧠 Data Analyst Skills Demonstrated

This project showcases practical skills relevant to Data Analyst roles:

- Data extraction and ETL
- JSON data handling
- Data cleaning and transformation
- State-name standardization
- Pandas analysis
- KPI calculation
- Aggregation and grouping
- Time-series analysis
- Geographic analysis
- Category-level analysis
- Exploratory Data Analysis
- Correlation analysis
- Interactive dashboard development
- Data visualization
- Business question framing
- Data storytelling
- SQL Server integration
- Git/GitHub documentation

---

## 📁 Project Structure

```text
Phone_pay_project/
│
├── dashboard/
│   ├── app.py                 # Streamlit dashboard
│   └── india_state.geojson    # India state boundaries
│
├── data/
│   └── pulse-master/          # PhonePe Pulse source data
│
├── config.toml
├── README.md
└── README_backup_2026-09-05.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/dev-abhishek18/Phone_pay_project.git
cd Phone_pay_project
```

### 2. Create a virtual environment

```bash
python -m venv env
```

### 3. Activate the environment on Windows

```bash
env\Scripts\activate
```

### 4. Install dependencies

```bash
pip install streamlit pandas pyodbc plotly seaborn matplotlib
```

### 5. Configure SQL Server

Before running the dashboard, configure the SQL Server connection used by `dashboard/app.py` for your local environment and make sure the required `phonepe_db` database/table is available.

### 6. Start the dashboard

```bash
streamlit run dashboard/app.py
```

---

## ⚠️ Security & Reproducibility Note

The current dashboard source contains a local SQL Server connection configuration. For a production-ready project, database credentials should **not** be stored directly in source code.

Recommended approach:

- Use environment variables or Streamlit secrets
- Keep local database settings outside the repository
- Add secret/config files to `.gitignore`

---

## 🚀 Future Improvements

- Add district-level analysis
- Add merchant, peer-to-peer and recharge category filters where supported by the dataset
- Add multi-page dashboard navigation
- Add year-over-year growth KPIs
- Add ranking tables for states and categories
- Add automated data-quality checks
- Add forecasting for transaction amount and volume
- Improve deployment configuration

---

## 📌 Conclusion

**PhonePe Transaction Insights Dashboard** demonstrates an end-to-end analytics workflow for a real-world digital-payment dataset.

It combines **Python, Pandas, SQL Server, Streamlit, Plotly and GeoJSON** to transform raw payment data into an interactive business-analysis experience.

The project is designed to showcase practical **Data Analyst capabilities in ETL, data cleaning, KPI analysis, visualization, geographic analysis and data storytelling**.

---

## 👤 Portfolio

**Abhishek Pal** — Data Analyst | SQL | Python | Power BI | Excel

Explore this repository along with the other analytics projects in my GitHub portfolio.