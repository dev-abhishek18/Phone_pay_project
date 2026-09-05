# PhonePe Transaction Insights Dashboard

This project is based on the PhonePe Pulse dataset, where I have taken the raw JSON files, cleaned them, stored them into SQL Server, and finally created an interactive dashboard using Streamlit and Plotly.  
The main purpose of the project is to understand how digital payments (UPI) are growing across different states in India over the years.

---

## Project Goal

The aim of the project is:

- To collect and organize PhonePe Pulse data  
- To load the data into a SQL database  
- To analyze yearly and quarterly transaction trends  
- To visualize the data on an India map  
- To understand which states contribute the most to digital transactions  

This dashboard helps users easily explore UPI payment patterns across India.

---

## Technologies Used

- **Python 3**
- **Streamlit** – for creating the dashboard  
- **Plotly** – for charts and India map  
- **Pandas** – for data cleaning  
- **SQL Server** – for storing structured data  
- **GeoJSON** – for drawing the India state map  

---

## Project Structure

```
phonepe-insights-project/
│── dashboard/
│   ├── app.py
│   ├── india_state.geojson
│
│── etl/
│   ├── load_json_to_sql.py
│
│── data/
│   ├── Raw PhonePe Pulse JSON files
│
│── phonepe_db/
│── env/
│── README.md
```

---

## How I Built This Project

### 1. Data Collection  
I downloaded the PhonePe Pulse dataset from GitHub. These files were in JSON format and needed cleaning before use.

### 2. Data Loading (ETL)  
I wrote a Python script (`load_json_to_sql.py`) to read each JSON file and insert the data into SQL Server tables.

### 3. Data Cleaning  
Inside SQL and Pandas, I cleaned issues such as:

- Missing values  
- Inconsistent state names  
- Format conversions  

### 4. Building the Dashboard  
Using Streamlit, I built an interactive dashboard that includes:

- A choropleth map of India  
- Filters for Year and Quarter  
- KPI cards (Total Transactions, Total Amount, Avg Value, etc.)  
- A yearly bar chart  

The map automatically changes based on selected year/quarter.

---

## How to Run the Project

### Step 1: Create Virtual Environment

```
python -m venv env
```

### Step 2: Activate It

```
env\Scripts\activate
```

### Step 3: Install Required Packages

```
pip install streamlit pandas pyodbc plotly
```

### Step 4: Run the Dashboard

```
streamlit run dashboard/app.py
```

---

## Understanding the Dashboard

### ✔ Filters  
You can choose any **year** and **quarter**, and the map + KPIs will update automatically.

### ✔ India Map  
Shows state-wise transaction amount.  
Hovering your mouse shows more details like:

- Total amount  
- Total transactions  
- Average transaction value  

### ✔ KPI Section  
Shows overall information for the selected period.

### ✔ Yearly Trend Chart  
Shows how the UPI transactions changed every year for:

- All India, or  
- A selected state  

---

## Why This Project Is Useful

- Helps understand UPI growth in India  
- Good practice in Data Analysis + Visualization  
- Shows ETL + SQL + Dashboard skills  
- Similar to a real industry analytics project  

---

## Future Improvements

- District-level charts  
- Category filters (merchant, peer-to-peer, recharge)  
- Multi-page dashboard  
- Add forecasting using ML  

---

## Conclusion

This project helped me understand how to work with real-world data, perform ETL, and create an interactive dashboard.  
It combines everything: Python, SQL, data cleaning, and a front-end visualization layer.
