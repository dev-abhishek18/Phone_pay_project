import os
import json
import pandas as pd
import pyodbc

# ---------------- SQL CONNECTION ----------------
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-NSAHO9N\\SQLSERVER2019;"
    "DATABASE=phonepe_db;"
    "UID=sa;"
    "PWD=ISS;"
)
cursor = conn.cursor()

BASE = r"D:\phonepe-insights-project\data\pulse-master\data\aggregated\transaction"

def clean_region(folder_name):
    return folder_name.lower().strip()   


rows = []

# ---------------- PROCESS JSON FILES ----------------
def process_folder(scope_level, region, folder):
    for year in os.listdir(folder):
        ypath = os.path.join(folder, year)
        if not os.path.isdir(ypath):
            continue

        for qfile in os.listdir(ypath):
            if not qfile.endswith(".json"):
                continue

            q = int(qfile.replace(".json", ""))

            with open(os.path.join(ypath, qfile), "r") as f:
                data = json.load(f)

            tdata = data.get("data", {}).get("transactionData", [])

            for t in tdata:
                for pi in t.get("paymentInstruments", []):
                    rows.append([
                        scope_level,
                        region,
                        int(year),
                        q,
                        t.get("name") or "Unknown",
                        pi.get("type") or "Unknown",
                        int(pi.get("count") or 0),
                        float(pi.get("amount") or 0.0)
                    ])


# ---------------- LOAD INDIA DATA ----------------
print("Loading Country...")
process_folder("country", "all india", os.path.join(BASE, "country", "india"))

print("Loading all states...")
state_dir = os.path.join(BASE, "country", "india", "state")

for state in os.listdir(state_dir):
    region_clean = clean_region(state)
    print("Processing:", region_clean)
    process_folder("state", region_clean, os.path.join(state_dir, state))

# ---------------- CREATE DATAFRAME ----------------
df = pd.DataFrame(rows, columns=[
    "scope_level", "region", "year", "quarter",
    "category", "payment_instrument", "count", "amount"
])

df.drop_duplicates(inplace=True)


# ---------------- SQL INSERT ----------------
query = """
INSERT INTO aggregated_transaction
(scope_level, region, year, quarter, category, payment_instrument, count, amount)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

for row in df.itertuples(index=False):
    cursor.execute(query, row)

conn.commit()
conn.close()

print("\n✔ FINAL ETL COMPLETED SUCCESSFULLY (OLD-STYLE MATCH) ✔")
