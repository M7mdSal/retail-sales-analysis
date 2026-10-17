# Retail Sales Analysis — University-Level Data Analytics Project

A beginner-friendly, **fully reproducible** portfolio project using university-level Python, Pandas, Matplotlib, and SQL.

> **Data disclosure:** `data/sales_sample.csv` contains 600 **synthetically generated** sales transactions for demonstration. It is not real customer or company data. All financial amounts are fictional, in unspecified currency units. No model training or predictive AI is involved.

## Questions answered
- How much revenue and profit did the store generate?
- Which months have the highest revenue?
- Which product categories generate the most revenue?
- Which products sell the most units?
- Which cities contribute the most revenue?

## Skills demonstrated
Python, Pandas, data cleaning, descriptive statistics, `groupby`, data visualization, MySQL SQL queries, GitHub documentation.

## Project structure
```
retail-sales-analysis/
├── data/sales_sample.csv       # synthetic data
├── notebooks/sales_analysis.ipynb
├── src/analysis.py
├── sql/queries.sql
├── reports/figures/            # generated after running
├── requirements.txt
└── README.md
```

## Setup (Windows PowerShell)
```powershell
cd retail-sales-analysis
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m src.analysis
jupyter notebook notebooks/sales_analysis.ipynb
```
If PowerShell blocks activation, run `.venv\Scripts\python.exe -m pip install -r requirements.txt` and `.venv\Scripts\python.exe -m src.analysis` directly.

## Outputs
- Terminal: transaction count, units sold, revenue, profit, monthly/category/product tables.
- `reports/figures/`: monthly revenue, category revenue, top products, city revenue PNG charts.
- Notebook: step-by-step exploration and charts.

## SQL
Open `sql/queries.sql` in MySQL Workbench. Execute the `CREATE DATABASE` and `CREATE TABLE` statements, then import `data/sales_sample.csv` into the `retail_sales.sales` table using the Workbench CSV Import Wizard. Run the remaining SELECT statements.

## Data dictionary
`order_id` unique order identifier; `date` transaction date; `product` item name; `category` item group; `quantity` units; `unit_price` selling price per unit before discount; `unit_cost` cost per unit; `discount` fractional discount; `city` city of sale.

Revenue = quantity × unit_price × (1 − discount). Profit = revenue − quantity × unit_cost. **Profit excludes overhead, tax, and shipping.** Each synthetic row is one order containing one product.

## Limitations and next steps
This synthetic sample is intended to demonstrate techniques, **not** support real-world business decisions. Replace with an appropriately licensed real dataset, add documented data validation, and report actual findings after running the analysis. Dataset must retain the column schema above.
