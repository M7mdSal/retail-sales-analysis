from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "sales_sample.csv"
FIGURES = ROOT / "reports" / "figures"


def load_and_clean(path=DATA_PATH):
    df = pd.read_csv(path)
    required = {"order_id", "date", "product", "category", "quantity", "unit_price", "unit_cost", "discount", "city"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    df = df.drop_duplicates(subset="order_id").copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    for col in ["quantity", "unit_price", "unit_cost", "discount"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["date", "product", "category", "city", "quantity", "unit_price", "unit_cost", "discount"])
    df = df[(df["quantity"] > 0) & (df["unit_price"] >= 0) & (df["unit_cost"] >= 0) & df["discount"].between(0, 1)].copy()
    df["revenue"] = df["quantity"] * df["unit_price"] * (1 - df["discount"])
    df["profit"] = df["revenue"] - df["quantity"] * df["unit_cost"]
    df["month"] = df["date"].dt.to_period("M").astype(str)
    return df


def analyze(df):
    summary = {"orders": int(df["order_id"].nunique()), "units_sold": int(df["quantity"].sum()),
               "revenue": float(df["revenue"].sum()), "profit": float(df["profit"].sum())}
    by_month = df.groupby("month", as_index=False)[["revenue", "profit"]].sum().sort_values("month")
    by_category = df.groupby("category", as_index=False)[["revenue", "profit"]].sum().sort_values("revenue", ascending=False)
    by_product = df.groupby("product", as_index=False)["quantity"].sum().sort_values("quantity", ascending=False)
    by_city = df.groupby("city", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
    return summary, by_month, by_category, by_product, by_city


def create_charts(by_month, by_category, by_product, by_city):
    FIGURES.mkdir(parents=True, exist_ok=True)
    plots = [
        (by_month, "month", "revenue", "Monthly Revenue", "monthly_revenue.png", "line"),
        (by_category, "category", "revenue", "Revenue by Category", "category_revenue.png", "bar"),
        (by_product.head(10), "product", "quantity", "Top Products by Units Sold", "top_products.png", "bar"),
        (by_city, "city", "revenue", "Revenue by City", "city_revenue.png", "bar"),
    ]
    for frame, x, y, title, filename, kind in plots:
        fig, ax = plt.subplots(figsize=(9, 5))
        if kind == "line":
            ax.plot(frame[x], frame[y], marker="o")
        else:
            ax.bar(frame[x], frame[y])
        ax.set_title(title)
        ax.set_ylabel(y.title())
        ax.tick_params(axis="x", rotation=35)
        fig.tight_layout()
        fig.savefig(FIGURES / filename, dpi=150)
        plt.close(fig)


def main():
    df = load_and_clean()
    summary, by_month, by_category, by_product, by_city = analyze(df)
    print("=== Retail Sales Analysis ===")
    for key, value in summary.items():
        print(f"{key}: {value:,.2f}" if isinstance(value, float) else f"{key}: {value}")
    print("\nMonthly sales:\n", by_month.to_string(index=False))
    print("\nRevenue by category:\n", by_category.to_string(index=False))
    print("\nTop products:\n", by_product.head().to_string(index=False))
    create_charts(by_month, by_category, by_product, by_city)
    print(f"\nCharts saved in: {FIGURES}")


if __name__ == "__main__":
    main()
