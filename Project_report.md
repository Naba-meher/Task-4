# Complete Data Analysis Project — E-commerce Sales (Jan–Feb 2024)

## Project overview
Analyze real sales transactions to find total revenue, best-selling product, regional performance, and trends. Deliver both numbers and charts with a clean, documented pipeline.

## Setup instructions
- Install Python 3.8+
- `pip install -r requirements.txt`
- Place `sales_data.csv` in `data/`
- Run: `python main.py`
- See outputs in `visualizations/`

## Code structure
- **main.py**: Load → Clean → Analyze → Visualize (Seaborn/Matplotlib)
- **analysis.ipynb**: Narrative EDA and insights
- **data/sales_data.csv**: Provided dataset
- **visualizations/**: PNG charts
- **report/**: This document

## Technical details
- **Cleaning**: Parse Date, coerce numeric, compute Total_Sales if missing, drop NA and duplicates.
- **Metrics**:
  - Total revenue
  - Average order value, median, standard deviation
  - Top product by revenue
  - Top region by revenue
- **Charts**:
  - Bar: Total Sales by Product
  - Line: Monthly Sales Trend
  - Bar: Total Sales by Region
  - Box: Price Distribution by Product
  - Heatmap: Correlation (Quantity, Price, Total_Sales)

## Insights (ready to paste)
- **Sales concentration:** Revenue is driven by a few high‑ticket products (e.g., Laptop and Phone), visible in the product bar chart.
- **Temporal trend:** Monthly totals show how Feb compares to Jan; use the line chart to present seasonality or spikes (e.g., promo periods).
- **Regional differences:** One or two regions lead revenue (e.g., North/South vs. West/East), guiding supply and marketing focus.
- **Price variability:** Boxplots reveal wide price ranges for certain products (Phones/Laptops), suggesting tiered offerings.
- **Correlations:** Total_Sales correlates strongly with Quantity by design; weak or mixed relation with Price points to varying price tiers and basket sizes.

## Testing evidence
- Run with provided CSV → generates 5 PNG charts without errors.
- Date parsing tolerates inconsistent formats via `errors="coerce"`.
- Duplicates and missing values are removed to avoid skewed metrics.
- Outputs verified by printing summary stats in console.

## Reflection (what I learned)
- End‑to‑end pipeline design: loading, cleaning, analysis, and visualization.
- Communicating findings with charts and concise text.
- Building reproducible artifacts (requirements, folder structure, saved PNGs).
