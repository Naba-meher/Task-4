#Week 4 - Complete Data Analysis Project
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib.ticker import FuncFormatter

# ----- Paths -----
DATA_PATH = os.path.join("data", "sales_data.csv")
VIS_DIR = "visualizations"
os.makedirs(VIS_DIR, exist_ok=True)

# ----- Helpers -----
def currency(x, pos):
    return f"₹{int(x):,}"

def load_and_clean(path=DATA_PATH):
    df = pd.read_csv(path)
    # Standardize column names (just in case)
    df.columns = [c.strip() for c in df.columns]

    # Parse dates
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Coerce numeric types
    for col in ["Quantity", "Price", "Total_Sales"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Compute Total_Sales if missing or inconsistent
    if "Total_Sales" not in df.columns or df["Total_Sales"].isna().sum() > 0:
        if {"Quantity", "Price"}.issubset(df.columns):
            df["Total_Sales"] = df["Quantity"] * df["Price"]

    # Basic cleaning: drop rows with missing critical fields
    critical = ["Date", "Product", "Region", "Quantity", "Price", "Total_Sales"]
    df = df.dropna(subset=[c for c in critical if c in df.columns])

    # Remove duplicates
    df = df.drop_duplicates()

    return df

def descriptive_stats(df):
    stats = {
        "rows": len(df),
        "cols": len(df.columns),
        "total_revenue": float(df["Total_Sales"].sum()),
        "avg_order_value": float(df["Total_Sales"].mean()),
        "median_order_value": float(df["Total_Sales"].median()),
        "std_order_value": float(df["Total_Sales"].std()),
        "top_product": df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False).index[0],
        "top_region": df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False).index[0],
    }
    return stats

def plot_sales_by_product(df):
    agg = df.groupby("Product", as_index=False)["Total_Sales"].sum().sort_values("Total_Sales", ascending=False)
    plt.figure(figsize=(10,6))
    sns.barplot(data=agg, x="Total_Sales", y="Product", palette="Set2")
    plt.title("Total Sales by Product (Jan–Feb 2024)")
    plt.xlabel("Total Sales (INR)")
    plt.gca().xaxis.set_major_formatter(FuncFormatter(currency))
    plt.tight_layout()
    out = os.path.join(VIS_DIR, "sales_by_product.png")
    plt.savefig(out, dpi=150)
    plt.close()
    return out

def plot_monthly_sales_trend(df):
    monthly = df.set_index("Date").resample("M")["Total_Sales"].sum().reset_index()
    plt.figure(figsize=(10,5))
    sns.lineplot(data=monthly, x="Date", y="Total_Sales", marker="o", color=sns.color_palette("Set2")[0])
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales (INR)")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(currency))
    plt.tight_layout()
    out = os.path.join(VIS_DIR, "monthly_sales_trend.png")
    plt.savefig(out, dpi=150)
    plt.close()
    return out

def plot_sales_by_region(df):
    agg = df.groupby("Region", as_index=False)["Total_Sales"].sum().sort_values("Total_Sales", ascending=False)
    plt.figure(figsize=(8,5))
    sns.barplot(data=agg, x="Region", y="Total_Sales", palette="Set2")
    plt.title("Total Sales by Region")
    plt.ylabel("Total Sales (INR)")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(currency))
    plt.tight_layout()
    out = os.path.join(VIS_DIR, "sales_by_region.png")
    plt.savefig(out, dpi=150)
    plt.close()
    return out

def plot_price_distribution_boxplot(df):
    plt.figure(figsize=(10,6))
    sns.boxplot(data=df, x="Product", y="Price", palette="Set2")
    plt.title("Price Distribution by Product")
    plt.tight_layout()
    out = os.path.join(VIS_DIR, "price_distribution_boxplot.png")
    plt.savefig(out, dpi=150)
    plt.close()
    return out

def plot_correlation_heatmap(df):
    numeric = df.select_dtypes(include=[np.number])
    corr = numeric.corr()
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap="vlag", center=0)
    plt.title("Correlation Matrix (numeric features)")
    plt.tight_layout()
    out = os.path.join(VIS_DIR, "correlation_heatmap.png")
    plt.savefig(out, dpi=150)
    plt.close()
    return out

def main():
    df = load_and_clean(DATA_PATH)
    stats = descriptive_stats(df)

    print("=== Summary ===")
    print(f"Rows: {stats['rows']} | Columns: {stats['cols']}")
    print(f"Total Revenue: ₹{int(stats['total_revenue']):,}")
    print(f"Average Order Value: ₹{stats['avg_order_value']:.2f}")
    print(f"Median Order Value: ₹{stats['median_order_value']:.2f}")
    print(f"Std Dev (Order Value): ₹{stats['std_order_value']:.2f}")
    print(f"Top Product by Revenue: {stats['top_product']}")
    print(f"Top Region by Revenue: {stats['top_region']}")

    files = [
        plot_sales_by_product(df),
        plot_monthly_sales_trend(df),
        plot_sales_by_region(df),
        plot_price_distribution_boxplot(df),
        plot_correlation_heatmap(df),
    ]
    print("\nSaved visualizations:")
    for f in files:
        print(" -", f)

if __name__ == "__main__":
    main()
