import os
import json
import pyodbc

# SQL CONNECTION
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-NSAHO9N\\SQLSERVER2019;"
    "DATABASE=phonepe_db;"
    "UID=sa;"
    "PWD=ISS;"
)

cursor = conn.cursor()

BASE = r"D:\phonepe-insights-project\data\pulse-master\data\aggregated\transaction"

def insert_row(row):
    cursor.execute("""
        INSERT INTO aggregated_transaction
        (scope_level, region, year, quarter, category, payment_instrument, count, amount)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, row)

def process_folder(scope_level, region, folder_path):
    """
    Recursively process year -> quarter.json files
    """
    for year in os.listdir(folder_path):
        year_path = os.path.join(folder_path, year)

        if not os.path.isdir(year_path):
            continue

        for qfile in os.listdir(year_path):
            if not qfile.endswith(".json"):
                continue

            qnum = int(qfile.replace(".json", ""))

            with open(os.path.join(year_path, qfile), "r") as f:
                data = json.load(f)

            tdata = data.get("data", {}).get("transactionData", [])

            for t in tdata:
                for pi in t.get("paymentInstruments", []):
                    insert_row((
                        scope_level,
                        region,
                        int(year),
                        qnum,
                        t.get("name"),
                        pi.get("type"),
                        pi.get("count"),
                        pi.get("amount")
                    ))

    conn.commit()

def load_all():
    # Load ALL INDIA (country)
    country_path = os.path.join(BASE, "country", "india")
    print("Loading country: ALL INDIA")
    process_folder("country", "ALL INDIA", country_path)

    # Load ALL states auto-detect
    state_path = os.path.join(BASE, "country", "india", "state")

    print("Loading all states...")
    for state in os.listdir(state_path):
        st_path = os.path.join(state_path, state)
        print("Loading:", state)
        process_folder("state", state, st_path)

    print("All data loaded successfully ✔")

load_all()
conn.close()
